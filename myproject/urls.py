from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from notes import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # 変更
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))  # 変更
]
