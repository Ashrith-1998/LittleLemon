from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Menu


class MenuModelTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            title="Pizza",
            price=250,
            inventory=10
        )

    def test_menu_item(self):
        item = Menu.objects.get(title="Pizza")
        self.assertEqual(item.title, "Pizza")
        self.assertEqual(item.price, 250)
        self.assertEqual(item.inventory, 10)


class MenuAPITest(APITestCase):

    def setUp(self):
        Menu.objects.create(
            title="Pizza",
            price=250,
            inventory=10
        )

    def test_get_menu(self):
        response = self.client.get('/restaurant/menu/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)