from django.contrib import admin
from employeeapp.models import Employee,Department

# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = ['id','name','created_at','updated_at']
    search_fields = ['id','name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    
    list_display = ['id','department__name','first_name','last_name','email','created_at','updated_at']
    search_fields =['id','department__name','first_name','last_name','email']
    
