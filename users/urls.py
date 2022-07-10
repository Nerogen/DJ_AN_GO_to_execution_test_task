from django.urls import path, include

from users.views import Register, cutting_url

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('shortener/', cutting_url, name='shortener')
]
