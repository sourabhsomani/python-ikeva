from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','Contact_Number','Gender')
    list_editable = ('Gender',)