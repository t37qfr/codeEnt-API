'''
Automatic testing API
'''
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from postings.models import BlogPost

from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

#new / blank db
User = get_user_model()


class BlogPostAPITestCase(APITestCase):
    def setUp(self):

        user = User.objects.create(username='test',email='test@test.com')
        user.set_password('random')
        user.save()

        blog_posts=BlogPost.objects.create(
            user=user,
            title='New title',
            content = 'Test content'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count,1)

    def test_get_list(self):
        '''Test the get list item'''
        data = {}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.get(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_post_item(self):
        '''Test the get list item'''
        data = {'title':'random title','content':'random conent'}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        print(response.data)