from django.db import models
from django.contrib.auth.models import User


# Stores the result of a user taking a quiz

class QuizResult(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, related_name="results")
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score}/{self.total_questions})"


# ✅ Represents a quiz

class Quiz(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Represents a single question in a quiz

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


# Represents a possible answer choice for a question

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


# Stores contact form messages (from Contact Us page)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)   # Sender’s name
    email = models.EmailField()               # Sender’s email
    message = models.TextField()              # The actual message
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


