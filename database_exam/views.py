from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.utils.timezone import datetime
from .forms import *


class Index(View):
    def get(self, request, *args, **kwargs):
        form = ExamForm()
        return render(request, 'database_exam/post.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        
        form = ExamForm(request.POST, request.FILES)
            
        if form.is_valid():
                form.save()
                return render(request, 'database_exam/validation.html')
        else:
                print(form.errors)
                form = ExamForm()
        return render(request, 'database_exam/post.html', {'form': form})

   
        