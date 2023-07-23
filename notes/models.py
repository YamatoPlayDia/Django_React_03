from django.db import models
from django.contrib.auth.models import User, Group, Permission

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.created_at} - {self.created_by.username} - {self.content[:50]}"

class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.created_at} - {self.created_by.username} - {self.content[:50]}"

