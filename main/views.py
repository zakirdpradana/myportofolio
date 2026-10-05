import os
import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST

from main.models import Experience
from main.models import Education   

from main.forms import ExperienceForm
from main.forms import EducationForm

from django.core import serializers
from django.core.exceptions import PermissionDenied      

from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, redirect, render

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Muhammad Zaki Radipradana",
        "npm": "2506599541",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia with a solid foundation in mathematics and a keen interest in cybersecurity. "
            "I enjoy solving problems using a logical and creative approach. I'm eager to learn, grow, and contribute to projects that "
            "create innovative solutions to real-world problem."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Zaki Radipradana",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    title_query = request.GET.get("title", "").strip()
    is_editor = request.user.is_authenticated and request.user.groups.filter(name='Editor').exists()

    context = {
        "name": "Muhammad Zaki Radipradana",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": EducationForm(),
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    context = {
        "name": "Muhammad Zaki Radipradana",
        "form": form,
    }

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")

    return render(request, "experience_form.html", context)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()
    
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
    
    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "thumbnail": experience.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = EducationForm(request.POST or None)

    context = {
        "name": "Muhammad Zaki Radipradana",
        "form": form,
    }

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_education")

    return render(request, "education_form.html", context)

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pendidikan."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Pendidikan berhasil ditambahkan.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        return redirect("main:show_education")
    
    return redirect("main:show_education")

@require_POST
def delete_education_ajax(request, education_id):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menghapus data."},
            status=403,
        )

    education = get_object_or_404(Education, pk=education_id)
    education.delete()
    return JsonResponse({"message": "Data pendidikan berhasil dihapus!"}, status=200)

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.prefetch_related('starred_by').all()
    
    if title_query:
        educations = educations.filter(institution_name__icontains=title_query)

    data = []
    for edu in educations:
        starred_users = edu.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(edu.id),
            "fields": {
                "institution_name": edu.institution_name,
                "description": edu.description,
                "thumbnail": edu.thumbnail,
                "started_at": edu.started_at.strftime("%Y-%m-%d") if edu.started_at else None,
                "ended_at": edu.ended_at.strftime("%Y-%m-%d") if edu.ended_at else None,
                "is_ongoing": edu.is_ongoing,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def update_education(request, education_id):
    if not(request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_education")

    context = {
        "name": "Muhammad Zaki Radipradana",
        "form": form,
        "education": education,
    }
    return render(request, "education_update_form.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Muhammad Zaki Radipradana",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Muhammad Zaki Radipradana",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_education")