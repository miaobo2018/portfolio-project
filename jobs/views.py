from django.shortcuts import render

from .models import Job


def home(request):
    jobs = Job.objects  # test transform the database type to python type
    return render(request, 'jobs/home.html', {'jobs': jobs})
