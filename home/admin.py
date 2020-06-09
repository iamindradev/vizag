from django.contrib import admin
from .models import student, mark ,teacher, login

# Register your models here.
admin.site.register(login)
admin.site.register(mark)
admin.site.register(teacher)
admin.site.register(student)