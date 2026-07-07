from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from employeeapp.models import Department, Employee

User = get_user_model()

class EmployeeAPITestCase(APITestCase):
    def setUp(self):

        self.hr_user = User.objects.create_superuser(username='hr', password='pw')
        self.regular_user = User.objects.create_user(username='emp', password='pw')
        
        self.dept1 = Department.objects.create(name="Development")
        self.dept2 = Department.objects.create(name="Design")
        
        Employee.objects.all().delete()
        
        self.emp1 = Employee.objects.create(department=self.dept1, first_name="E1", last_name="L1", email="e1@test.com")
        self.emp2 = Employee.objects.create(department=self.dept2, first_name="E2", last_name="L2", email="e2@test.com")
        
        self.url = reverse('employee-list-create')

    def test_create_employee_by_hr(self):
        self.client.force_authenticate(user=self.hr_user)
        data = {
            "department": self.dept1.id,
            "first_name": "Dilshod",
            "last_name": "Coder",
            "email": "dev777@company.com"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_by_regular_user_fails(self):
        self.client.force_authenticate(user=self.regular_user)
        data = {
            "department": self.dept1.id, 
            "first_name": "Test", 
            "last_name": "User", 
            "email": "test@test.com"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_employee_by_department(self):
        self.client.force_authenticate(user=self.hr_user)
        
        response = self.client.get(f"{self.url}?department={self.dept1.id}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        results = response.data.get('results', response.data)
        
        employee_ids = [emp['id'] for emp in results]
        
        self.assertIn(self.emp1.id, employee_ids)
        self.assertNotIn(self.emp2.id, employee_ids)