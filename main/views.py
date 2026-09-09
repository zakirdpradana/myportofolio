from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Muhammad Zaki Radipradana",
        "npm": "2506599541",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia with a solid foundation in mathematics and a keen interest in cybersecurity."
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