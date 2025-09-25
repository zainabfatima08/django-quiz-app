from django.contrib import admin
from .models import Quiz, Question, Choice


# Inline choices inside question form

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2    # show 2 empty slots by default

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "quiz")
    inlines = [ChoiceInline]

class QuizAdmin(admin.ModelAdmin):
    list_display = ("title",)

# Register in admin

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)


