from django.contrib import admin
from .models import newuser,course,problems,reply
# Register your models here.
admin.site.register(newuser)
admin.site.register(course)
admin.site.register(problems)
admin.site.register(reply)