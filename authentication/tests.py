from django.test import TestCase

from authentication.models import User


class UserModelTest(TestCase):
    # class User, fields
    # username = models.CharField(db_index=True, max_length=255, unique=True)
    # email = models.EmailField(db_index=True, unique=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='Big', email="usertest@test.test")

    def test_username_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('username').verbose_name
        print(field_label)
        self.assertEquals(field_label, 'username')

    def test_username_max_length(self):
        author = User.objects.get(id=1)
        max_length = author._meta.get_field('username').max_length
        self.assertEquals(max_length, 255)

    def test_email_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('username').verbose_name
        print(field_label)
        self.assertEquals(field_label, 'username')
