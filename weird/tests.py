from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class EncodeTests(TestCase):
    """
    Tests ``:class:`Encode```
    """
    def setUp(self):
        self.client = APIClient()

    def test_encode_simple_text(self):
        data = {'text': 'This is some simple(?) text without weird backslashes.'}
        response = self.client.post(reverse('encode'), data)
        response_split = response.data.split('\n-weird-\n')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_split), 3, "Output doesn't have a proper format.")
        self.assertEqual(len(response_split[1].split()), 8, "Encoded text has got wrong words number.")
        self.assertEqual(response_split[2], "backslashes simple some text This weird without",
                         "Original words differ from the expected ones.")

    def test_encode_with_backslashes(self):
        data = {'text': 'This is a long (looong) test sentence,\n with some big (biiiig) words!'}
        response = self.client.post(reverse('encode'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Some test comparing the output string to: "\n-weird-\nTihs is a lnog (lonoog) tset stcnneee,\n wtih smoe big
        # (biiiig) wrdos!\n-weird-\nlong looong sentence some test This with words"...


class DecodeTests(TestCase):
    """
    Tests ``:class:`Decode```
    """
    def setUp(self):
        self.client = APIClient()

    def test_decode_simple_text(self):
        data = {'text': ''}

