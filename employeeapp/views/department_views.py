from employeeapp.serializers.department_serializer import DepartmentSerializer,Department
from rest_framework import generics,permissions
from employeeapp.permissions.admin_staff import IsAdminOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class DepartmentListCreateApi(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated,IsAdminOrReadOnly]

    @method_decorator(cache_page(60*15,key_prefix='department_list'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DepartmentDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated,IsAdminOrReadOnly]

    @method_decorator(cache_page(60*15,key_prefix='department_retrieve'))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
