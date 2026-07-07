from django.urls import path
from employeeapp.views import department_views,employee_views
from employeeapp.views.user_views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 


urlpatterns = [
    path('department/',department_views.DepartmentListCreateApi.as_view(),name='department-list-create'),
    path('department/<int:pk>',department_views.DepartmentDetailApi.as_view(),name='department-detail'),

    path('employee/',employee_views.EmployeeListCreateApi.as_view(),name='employee-list-create'),
    path('employee/<int:pk>',employee_views.EmployeeDetailApi.as_view(),name='employee-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view(),name='register')
    
    
    
    ]