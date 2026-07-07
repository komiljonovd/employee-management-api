from django.apps import AppConfig


class EmployeeappConfig(AppConfig):
    name = 'employeeapp'
    verbose_name = 'Management'
    

    def ready(self):
        from . import signals
