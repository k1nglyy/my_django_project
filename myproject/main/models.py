from django.db import models
from django.contrib.auth.models import User

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class StringRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_string = models.TextField()
    word_count = models.IntegerField()
    char_count = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()