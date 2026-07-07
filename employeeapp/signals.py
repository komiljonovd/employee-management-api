from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Department,Employee

@receiver([post_save,post_delete],sender=Department)
def delete_department_cache(sender,instance,**kwargs):
    cache.delete_pattern('*department_list*')
    cache.delete_pattern('*department_retrieve*')


@receiver([post_save,post_delete],sender=Employee)
def delete_employee_cache(sender,instance,**kwargs):
    cache.delete_pattern('*employee_list*')
    cache.delete_pattern('*employee_retrieve*')

