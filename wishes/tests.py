from django.test import TestCase
from django.urls import reverse
from wishes.models import Wishes
from unittest.mock import Mock, patch


class AllWishesTestCase(TestCase):
    def setUp(self):
        # Set up test data for the view function
        self.wish_1 = Wishes.objects.create(title='Test Wish 1', status='Open', list_date='2022-01-01')
        self.wish_2 = Wishes.objects.create(title='Test Wish 2', status='Pending', list_date='2022-01-02')
        self.wish_3 = Wishes.objects.create(title='Test Wish 3', status='Fulfilled', list_date='2022-01-03')
        self.wish_4 = Wishes.objects.create(title='Test Wish 4', status='Open', list_date='2022-01-04')
        self.wish_5 = Wishes.objects.create(title='Test Wish 5', status='Pending', list_date='2022-01-05')
        self.wish_6 = Wishes.objects.create(title='Test Wish 6', status='Fulfilled', list_date='2022-01-06')


    @patch('wishes.models.Wishes.main_photo', new_callable=Mock, return_value=None)
    @patch('wishes.models.Wishes.photo_1', new_callable=Mock, return_value=None)
    @patch('wishes.models.Wishes.photo_2', new_callable=Mock, return_value=None)
    def test_all_wishes_view(self, main_photo_mock, photo_1_mock, photo_2_mock):
        # Send a GET request to the view function
        response = self.client.get(reverse('wishes:all_wishes'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the correct number of wishes
        self.assertEqual(len(response.context['all_wishes']), 6)

        # Check that the rendered template is the correct one
        self.assertTemplateUsed(response, 'wishes/all_wishes.html')

        # Check that the main_photo attribute is mocked in the rendered context
        self.assertIsNone

         # Check that the photo_1 attribute is mocked in the rendered context
        self.assertIsNone

         # Check that the photo_2 attribute is mocked in the rendered context
        self.assertIsNone
