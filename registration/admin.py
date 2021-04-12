from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class StudentRegistration(admin.ModelAdmin):
    list_display=('name','email','password','id')
