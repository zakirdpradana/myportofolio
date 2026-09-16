from django.shortcuts import render
from django.contrib import messages

from main.models import Experience
from main.models import Education   

from main.forms import ExperienceForm

from django.core import serializers

from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect, render


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
    context = {
        "name": "Muhammad Zaki Radipradana",
        "experience_list": Experience.objects.all(),
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

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Muhammad Zaki Radipradana",
        "form": form,
    }
    return render(request, "experience_form.html", context)
