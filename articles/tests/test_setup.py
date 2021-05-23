from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

class TestSetUp(APITestCase):
    def setUp(self):
        self.article_url = '/articles/'
        self.article_data = {
            'title': 'New title',
            'content': 'Content of article',
            'author': 'Author'
        }
        self.user = self.setup_user()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
        return super().setUp()
    
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create(
            username='user1',
            password='user1',
            email='user1@mail.com'
        )
