from django.test import TestCase
from user.models import *


class UserTestCase(TestCase):
    def setUp(self):
        self.faith = User.objects.create(first_name = "Faith", last_name = "Shum", gender = "Female", dob= )