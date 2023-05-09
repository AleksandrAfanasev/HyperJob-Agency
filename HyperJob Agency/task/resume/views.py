from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.http import HttpResponseRedirect, HttpResponseForbidden

# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resume.html', context={'resumes': Resume.objects.all()})


class NewResumeView(View):
    def post(self, request):
        if request.user.is_authenticated:
            resume = Resume.objects.create(
                author=request.user,
                description=request.POST.get("description", "")
            )
            resume.save()
            return redirect("/resumes")
        else:
            return HttpResponseForbidden()