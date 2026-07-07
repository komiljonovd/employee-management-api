from employeeapp.serializers.employee_serializer import EmployeeSerializer,Employee
from rest_framework import generics,permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from employeeapp.permissions.admin_staff import IsAdminOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class EmployeeListCreateApi(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated,IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['department']
    search_fields = ['first_name','last_name']

    @method_decorator(cache_page(60*15,key_prefix='employee_list'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class EmployeeDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated,IsAdminOrReadOnly]

    @method_decorator(cache_page(60*15,key_prefix='employee_retrieve'))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    
    
