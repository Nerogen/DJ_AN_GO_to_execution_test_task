import pyshorteners
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreationForm

short_urls = []


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/users/shortener')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def logout_user(request):
    short_urls.clear()
    logout(request)
    return redirect('/users/shortener')


def cutting_url(request):
    if request.method == 'GET':
        return render(request=request, template_name='shortener.html')

    if request.method == 'POST':
        url = request.POST.get('processing-link')
        shorter = pyshorteners.Shortener()
        short_url = shorter.tinyurl.short(url)
        short_urls.append(short_url)
        context = {
            'short_url': short_url,
            'short_urls': short_urls
        }
        return render(request=request, template_name='shortener.html', context=context)
