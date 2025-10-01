from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.student_id})"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class TopicSubmission(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.teacher.name} - {self.topic}"
