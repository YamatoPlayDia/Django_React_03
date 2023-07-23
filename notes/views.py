from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Note, Comment
from .serializers import NoteSerializer, CommentSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.filter(deleted_at=None)
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        note = self.get_object()
        note.deleted_at = timezone.now()
        note.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(deleted_at=None)
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.deleted_at = timezone.now()
        comment.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

