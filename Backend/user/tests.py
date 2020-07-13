from django.test import TestCase

# Create your tests here.

from user.models import *
import datetime


class UserTestCase(TestCase):
    def setUp(self):
        self.faith = User.objects.create(first_name="Faith", last_name="Shum", gender="Female",
                                         dob="1997-10-19",  location="UK", email="FaithChung@Gmail.com", phone_no=38247298473892)
        self.faith_auth = Authentication.objects.create(
            username="BigFlower", password="abc123", user=self.faith)

    def test_faith_saved_pk(self):
        self.assertEqual(self.faith.pk, 1)

    def test_faith_saved_firstname(self):
        self.assertEqual(self.faith.first_name, "Faith")

    def test_faith_saved_lastname(self):
        self.assertEqual(self.faith.last_name, "Shum")

    def test_faith_saved_gender(self):
        self.assertEqual(self.faith.gender, "Female")

    def test_faith_saved_dob(self):
        self.assertEqual(self.faith.dob, "1997-10-19")

    def test_faith_location(self):
        self.assertEqual(self.faith.location, "UK")

    def test_faith_email(self):
        self.assertEqual(self.faith.email, "FaithChung@Gmail.com")

    def test_faith_phone_no(self):
        self.assertEqual(self.faith.phone_no, 38247298473892)

    def test_faith_auth_created(self):
        self.assertEqual(self.faith_auth.username, "BigFlower")
        self.assertEqual(self.faith_auth.password, "abc123")
        self.assertEqual(self.faith_auth.user.pk, self.faith.pk)
