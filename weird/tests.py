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
        data = {'text': r'This is some simple(?) text without weird backslashes.'}
        response = self.client.post(reverse('encode'), data)
        response_split = response.data.split('\n-weird-\n')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_split), 3, "Output doesn't have a proper format.")
        self.assertEqual(len(response_split[1].split()), 8, "Encoded text has got wrong words number.")
        self.assertEqual(response_split[2], "backslashes simple some text This weird without",
                         "Original words differ from the expected ones.")

    def test_encode_text_with_backslashes(self):
        data = {'text': r'This is a long (looong) test sentence,\n with some big (biiiig) words!'}
        response = self.client.post(reverse('encode'), data)
        response_split = response.data.split('\n-weird-\n')
        self.assertEqual(len(response_split), 3, "Output doesn't have a proper format.")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_split[2], 'long looong sentence some test This with words',
                         "Original words differ from the expected ones.")

    def test_missing_parameter(self):
        response = self.client.post(reverse('encode'), {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DecodeTests(TestCase):
    """
    Tests ``:class:`Decode```
    """
    def setUp(self):
        self.client = APIClient()

    def test_decode_simple_text(self):
        data = {'text': r'\n-weird-\nJsut ttinseg a txet, an esay one\n-weird-\neasy Just testing text'}
        response = self.client.post(reverse('decode'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'Just testing a text, an easy one')

    def test_decode_text_with_backslashes(self):
        data = {'text': r'\n-weird-\nTihs is a ,,lnog (lonoog) tset snecnete,\n wtih smoe big (biiiig) '
                        r'wodrs!\n-weird-\nlong looong sentence some test This with words'}
        response = self.client.post(reverse('decode'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'This is a ,,long (looong) test sentence,\n with some big (biiiig) words!')

    def test_missing_parameter(self):
        response = self.client.post(reverse('decode'), {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_encoder_format(self):
        data = {'text': 'This is a wrong format.\n-weird-\n'}
        response = self.client.post(reverse('decode'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
