from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.views import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json


class BaseEmployeeTest(APITestCase):

    def setUp(self):
        self.arnaldo = Employee.objects.create(
            name="Arnaldo Pereira",
            email="arnaldo@luizalabs.com",
            department="Architecture"
        )
        self.renato = Employee.objects.create(
            name="Renato Pedigoni",
            email="renato@luizalabs.com",
            department="E-commerce"
        )
        self.thiago = Employee.objects.create(
            name="Thiago Catoto",
            email="catoto@luizalabs.com",
            department="Mobile"
        )
        self.valid_payload = {
            "name": "Arnaldo Pereira",
            "email": "arnaldopereira@luizalabs.com",
            "department": "Architecture"
        }

        self.invalid_payload = {
            "name": "",
            "email": "arnaldo@luizalabs.com",
            "department": "Architecture"
        }
        self.valid_partial_payload = {
            "department": "Web"
        }
        self.invalid_partial_payload = {
            "department": ""
        }
        self.user = User.objects.create_user("user", "user@email.com", "pass")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

class GetAllEmployeesTest(BaseEmployeeTest):

    def test_get_all_employees(self):
        response = self.client.get(
            reverse("employee-all")
        )

        expected = EmployeeSerializer(Employee.objects.all(), many=True)
        self.assertEquals(response.data, expected.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class GetSingleEmployeeTest(BaseEmployeeTest):

    def test_get_valid_single_employee(self):
        response = self.client.get(
            reverse("employee-single", kwargs={"pk": self.arnaldo.pk})
        )
        employee = EmployeeSerializer(Employee.objects.get(pk=self.arnaldo.pk))
        self.assertEqual(response.data, employee.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_employee(self):
        response = self.client.get(
            reverse("employee-single", kwargs={"pk": 10})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewEmployeeTest(BaseEmployeeTest):

    def test_create_valid_employee(self):
        response = self.client.post(
            reverse("employee-all"),
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_employee(self):
        response = self.client.post(
            reverse("employee-all"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteEmployeeTest(BaseEmployeeTest):

    def test_delete_valid_employee(self):
        response = self.client.delete(
            reverse("employee-single", kwargs={"pk": self.arnaldo.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_employee(self):
        response = self.client.delete(
            reverse("employee-single", kwargs={"pk": 10})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdatePutEmployeeTest(BaseEmployeeTest):

    def test_update_put_valid_employee(self):
        response = self.client.put(
            reverse("employee-single", kwargs={"pk": self.arnaldo.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_put_invalid_payload_employee(self):
        response = self.client.put(
            reverse("employee-single", kwargs={"pk": self.arnaldo.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_put_invalid_employee(self):
        response = self.client.put(
            reverse("employee-single", kwargs={"pk": 10}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdatePatchEmployeeTest(BaseEmployeeTest):

    def test_update_patch_valid_employee(self):
        response = self.client.patch(
            reverse("employee-single", kwargs={"pk": self.arnaldo.pk}),
            data=json.dumps(self.valid_partial_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_patch_invalid_payload_employee(self):
        response = self.client.patch(
            reverse("employee-single", kwargs={"pk": self.arnaldo.pk}),
            data=json.dumps(self.invalid_partial_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_patch_invalid_employee(self):
        response = self.client.patch(
            reverse("employee-single", kwargs={"pk": 10}),
            data=json.dumps(self.valid_partial_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
