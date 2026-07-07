from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from employeeapp.models import Department

User = get_user_model()


class DepartmentAPITestCase(APITestCase):

    def setUp(self) -> None:

        self.regular_user = User.objects.create_user(
            username="regular_worker",
            password="password123",
            is_staff=False
        )
        self.admin_user = User.objects.create_user(
            username="hr_admin",
            password="adminpassword123",
            is_staff=True
        )

        self.it_department = Department.objects.create(name="IT Bo'limi")

        self.list_create_url = reverse("department-list-create")
        self.detail_url = reverse("department-detail", kwargs={"pk": self.it_department.pk})


    def test_anonymous_user_cannot_access_departments(self) -> None:

        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_regular_user_can_list_but_cannot_create(self) -> None:

        self.client.force_authenticate(user=self.regular_user)

        get_response = self.client.get(self.list_create_url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        data = {"name": "Marketing Bo'limi"}
        post_response = self.client.post(self.list_create_url, data, format="json")
        self.assertEqual(post_response.status_code, status.HTTP_403_FORBIDDEN)


    def test_admin_can_create_department(self) -> None:
       
        self.client.force_authenticate(user=self.admin_user)

        data = {"name": "HR Bo'limi"}
        response = self.client.post(self.list_create_url, data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Department.objects.filter(name="HR Bo'limi").exists())

    def test_admin_can_update_department(self) -> None:
        self.client.force_authenticate(user=self.admin_user)

        data = {"name": "IT Infrastructure"}
        response = self.client.put(self.detail_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.it_department.refresh_from_db()
        self.assertEqual(self.it_department.name, "IT Infrastructure")

    def test_admin_can_delete_department(self) -> None:
        self.client.force_authenticate(user=self.admin_user)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), 0)


    def test_duplicate_department_name_validation(self) -> None:
        
        self.client.force_authenticate(user=self.admin_user)

        
        data = {"name": "IT Bo'limi"}
        response = self.client.post(self.list_create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)