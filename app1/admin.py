from django.contrib import admin

# Register your models here.
from app1.models import Department,HOD,Professor,Student


class Department_admin(admin.ModelAdmin):
    list_display = ['name','code']
admin.site.register(Department,Department_admin)

class HOD_admin(admin.ModelAdmin):
    list_display = ['department','name','email']
admin.site.register(HOD,HOD_admin)

class Professor_admin(admin.ModelAdmin):
    list_display = ['hod','department','name','email']
admin.site.register(Professor,Professor_admin)

class Student_admin(admin.ModelAdmin):
    list_display = ['professor','department','name','roll_no','email']
admin.site.register(Student,Student_admin)
