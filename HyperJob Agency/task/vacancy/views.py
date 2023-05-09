from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden


# Create your views here.

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'vacancy/login.html'


def MyLogoutView(request):
    return render(request, 'vacancy/base.html')

class SingupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'vacancy/sign_up.html'


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancy.html', context={'vacancy': Vacancy.objects.all()})


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/base.html')




class NewVacancyView(View):
    def post(self, request):
        username = request.user
        description = request.POST.get("description")
        if request.user.is_staff:
            post = Vacancy(author=username, description=description)
            post.save()
            return HttpResponseRedirect("/")
        return HttpResponseForbidden()
