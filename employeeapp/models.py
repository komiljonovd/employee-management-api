from django.db import models

# Create your models here.




class Department(models.Model):

    name = models.CharField(max_length=128,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['-created_at']  


class Employee(models.Model):

    department = models.ForeignKey(Department,on_delete=models.PROTECT,related_name='employees')
    first_name = models.CharField(max_length=128,db_index=True)
    last_name = models.CharField(max_length=128,db_index=True)
    email = models.EmailField(unique=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'Employee'
        verbose_name ='Employee'
        verbose_name_plural = 'Employees'
        ordering = ['-created_at']  