from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import Quiz, Question, Choice, QuizResult
from .forms import ContactForm, CustomUserCreationForm


# ---------------- Signup ---------------- #

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in new user
            return redirect("quiz_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


# ---------------- Quiz List (with search) ---------------- #

def quiz_list(request):
    query = request.GET.get("q", "")  
    if query:
        quizzes = Quiz.objects.filter(title__icontains=query) 
    else:
        quizzes = Quiz.objects.all()

    return render(request, "quiz/quiz_list.html", {
        "quizzes": quizzes,
        "query": query
    })


# ---------------- Quiz Detail ---------------- #

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == "POST":
        results = []
        score = 0

        for question in questions:
            selected_id = request.POST.get(f"question_{question.id}")
            if selected_id:
                selected_choice = get_object_or_404(Choice, id=selected_id)
                correct_choice = question.choices.filter(is_correct=True).first()
                is_correct = selected_choice.is_correct

                if is_correct:
                    score += 1

                results.append({
                    "question": question,
                    "selected": selected_choice,
                    "correct": correct_choice,
                    "is_correct": is_correct,
                })


        # Save result in DB

        QuizResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=questions.count()
        )

        return render(request, "quiz/result.html", {
            "quiz": quiz,
            "results": results,
            "score": score,
            "total": questions.count(),
        })

    return render(request, "quiz/quiz_detail.html", {
        "quiz": quiz,
        "questions": questions,
    })


# ---------------- Quiz History ---------------- #

@login_required
def quiz_history(request):
    history = QuizResult.objects.filter(user=request.user).order_by("-date")
    return render(request, "quiz/quiz_history.html", {"history": history})


# ---------------- About ---------------- #

def about_view(request):
    return render(request, "quiz/about.html")


# ---------------- Contact ---------------- #

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)

            # Send email
            subject = f"New Contact Message from {contact.name}"
            message = f"""
            Name: {contact.name}
            Email: {contact.email}

            Message:
            {contact.message}
            """
            send_mail(
                subject,
                message,
                "no-reply@quizapp.com",  # From
                ["support@quizapp.com"],  # To
                fail_silently=False,
            )

            contact.save()
            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "quiz/contact.html", {"form": form})


