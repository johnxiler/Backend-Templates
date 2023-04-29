from django.db import models

# Create your models here.


class SurveyRating(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_objectives = models.IntegerField()
    delivering_material = models.IntegerField()
    engaging_students = models.IntegerField()
    responding_questions = models.IntegerField()
    providing_feedback = models.IntegerField()
    inclusive_environment = models.IntegerField()
    using_technology = models.IntegerField()
    promoting_critical_thinking = models.IntegerField()
    challenging_students = models.IntegerField()
    overall_satisfaction = models.IntegerField()

# Create a model with a field to store the chosen option as an integer


class CourseEvaluation(models.Model):
    faculty_member = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    year = models.IntegerField()
    communication = models.IntegerField()
    delivery = models.IntegerField()
    engagement = models.IntegerField()
    responsiveness = models.IntegerField()
    feedback = models.IntegerField()
    inclusiveness = models.IntegerField()
    technology = models.IntegerField()
    critical_thinking = models.IntegerField()
    motivation = models.IntegerField()
    satisfaction = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course_title} - {self.faculty_member} ({self.semester} {self.year})"
