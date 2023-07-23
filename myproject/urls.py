from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from notes import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
