from django.db import models

# Create your models here.
class Exam_txt(models.Model):
    name = models.CharField(max_length=100)
    date_ajout = models.DateTimeField(auto_now_add=True)
    exam_file = models.FileField(upload_to='exam')
    
    
    def __str__(self):
        return self.name