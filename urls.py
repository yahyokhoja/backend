# В urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("✅ Django работает! Это главная")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', lambda request: HttpResponse("🩺 Всё хорошо!")),  # для /health
    path('', index),  # главная страница — /
]
