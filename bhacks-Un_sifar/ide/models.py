from django.db import models

# Create your models here.
class code(models.Model):
    problem_id = models.CharField(max_length=255)
    problem_content = models.TextField()
    lang = models.CharField(max_length=255)
    code_input = models.TextField()
    compile_status= models.CharField(max_length=255)
    run_status_status=models.CharField(max_length=255)