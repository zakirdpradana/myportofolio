from django.urls import path

from main.views import show_main, show_experience, show_education
from main.views import create_experience, get_experience_json, delete_experience, create_experience_ajax
from main.views import create_education, delete_education, get_education_json, update_education, create_education_ajax, delete_education_ajax
from main.views import register, login_user, logout_user
from main.views import toggle_star, toggle_star_education

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/star/",toggle_star,name="toggle_star"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("education/<uuid:education_id>/delete-ajax/", delete_education_ajax, name="delete_education_ajax"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/edit/",update_education,name="update_education"),
    path("education/<uuid:education_id>/star/",toggle_star_education,name="toggle_star_education"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]