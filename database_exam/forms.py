from django import forms
from .models import Exam_txt

#creating a form
class ExamForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Exam_txt
  
        # specify fields to be used
        fields = ('name', 'exam_file')
