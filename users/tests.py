from django.test import TestCase
from django.urls import reverse, resolve
from users.views import log_out, register

class UrlTest(TestCase):
    def testLogoutPage(self):
       response = self.client.get('log_out/')
       print(response)
       self.assertEqual(response.status_code, 200)

    def testRegisterPage(self):
        response = self.client.get('register/')
        print(response)
        self.assertEqual(response.status_code, 200)

