from rest_framework import serializers
from .models import Note, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class NoteSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'favorite', 'created_at', 'updated_at', 'created_by']

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    note = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all())
    class Meta:
        model = Comment
        fields = ['id', 'note', 'created_at', 'created_by', 'content']