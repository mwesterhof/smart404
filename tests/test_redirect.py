from django.test import Client, TestCase

from smart404.models import NotFoundEntry


class TestRedirects(TestCase):
    def setUp(self):
        self.client = Client()

    def test_entry_creation(self):
        self.assertEqual(NotFoundEntry.objects.count(), 0)
        response = self.client.get('/foo/bar/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(NotFoundEntry.objects.count(), 1)

    def test_redirect_302(self):
        self.client.get('/foo/bar/')
        NotFoundEntry.objects.filter(url='/foo/bar/').update(
            redirect_to='/baz/')
        response = self.client.get('/foo/bar/')
        self.assertEqual(response['Location'], '/baz/')
        self.assertEqual(response.status_code, 302)

    def test_redirect_301(self):
        self.client.get('/foo/bar/')
        NotFoundEntry.objects.filter(url='/foo/bar/').update(
            permanent=True, redirect_to='/baz2/')
        response = self.client.get('/foo/bar/')
        self.assertEqual(response['Location'], '/baz2/')
        self.assertEqual(response.status_code, 301)
