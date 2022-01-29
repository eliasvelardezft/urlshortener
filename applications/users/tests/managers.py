from django.test import TestCase

from applications.users.models import User

class UserManagerTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(
            first_name='elias',
            last_name='velardez',
            username='elias',
            email='elias@gmail.com',
            password='elias123'
        )
        User.objects.create_superuser(
            first_name='bill',
            last_name='gates',
            username='billgates',
            email='billgates@gmail.com',
            password='bill123'
        )

    def test_create_user(self):
        user = User.objects.get(username='elias') 
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

    def test_create_superuser(self):
        user = User.objects.get(username='billgates') 
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
        