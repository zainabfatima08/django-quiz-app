from django.urls import path
from . import views


urlpatterns = [
     path("signup/", views.signup_view, name="signup"),
    path('', views.quiz_list, name="quiz_list"),  # list of all quizzes
    path('<int:quiz_id>/', views.quiz_detail, name="quiz_detail"),  # specific quiz
    path("history/", views.quiz_history, name="quiz_history"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("quizzes/", views.quiz_list, name="quiz_list"),

]
