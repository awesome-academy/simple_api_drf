from .test_setup import TestSetUp

class TestArticle(TestSetUp):
    def test_list_with_unauth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.article_url)
        self.assertEqual(response.status_code, 401)
    
    def test_list_success(self):
        response = self.client.get(self.article_url)
        self.assertEqual(response.status_code, 200)
    
    def test_create_successful(self):
        response = self.client.post(self.article_url, self.article_data, format='json')
        res_data = response.data
        self.assertEqual(res_data['title'], self.article_data['title'])
        self.assertEqual(res_data['content'], self.article_data['content'])
        self.assertEqual(res_data['author'], self.article_data['author'])
        self.assertEqual(response.status_code, 201)
    
    def test_create_invalid_data(self):
        invalid_data = self.article_data
        invalid_data['title'] = ''
        response = self.client.post(self.article_url, invalid_data, format='json')
        self.assertEqual(response.status_code, 400)
