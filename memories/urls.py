from django.urls import path
from .views import upload_memory, success, gallery, gallery_login

urlpatterns = [
    path('', upload_memory),
    path('success/', success),
    path('gallery/', gallery),
    path('gallery-login/', gallery_login),
]