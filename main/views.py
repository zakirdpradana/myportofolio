import os
from django.shortcuts import render
from django.contrib import messages

from main.models import Experience
from main.models import Education   

from main.forms import ExperienceForm

from django.core import serializers

from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect, render

SECRET_ADMIN_KEY = os.getenv("SECRET_ADMIN_KEY", "rahasia123")

def show_main(request):
    context = {
        "name": "Muhammad Zaki Radipradana",
        "npm": "2506599541",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia with a solid foundation in mathematics and a keen interest in cybersecurity. "
            "I enjoy solving problems using a logical and creative approach. I'm eager to learn, grow, and contribute to projects that "
            "create innovative solutions to real-world problem."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experiences_data = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences_data]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Zaki Radipradana",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Muhammad Zaki Radipradana",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    context = {
        "name": "Muhammad Zaki Radipradana",
        "form": form,
    }

    if request.method == "POST" and form.is_valid():
        header_key = request.headers.get("X-Secret-Key")
        form_key = request.POST.get("secret_key")

        if header_key != SECRET_ADMIN_KEY and form_key != SECRET_ADMIN_KEY:
            messages.error(request, "Kode rahasia salah! Kamu tidak diizinkan menambah data.")
            return redirect("main:show_experience")

        if form.is_valid():
            form.save()
            messages.success(request, "Pengalaman baru berhasil ditambahkan!")
            return redirect("main:show_experience")

    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
    
    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        header_key = request.headers.get("X-Secret-Key")
        form_key = request.POST.get("secret_key")

        if header_key != SECRET_ADMIN_KEY and form_key != SECRET_ADMIN_KEY:
            messages.error(request, "Kode rahasia salah! Gagal menghapus pengalaman.")
            return redirect("main:show_experience")

        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")
