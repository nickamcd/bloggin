from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post
from django.contrib.auth.models import User

# Create your tests here.
class PostAPITestCase(APITestCase):
  def setUp(self):
    test_user = User.objects.create_user(username='test-user', 
                                         password='password')
    test_post = Post.objects.create(title='Test API Post Title', 
                                    content='Test API Post Content', author_id=1)

  def test_get_posts_list(self):
    # create api request and get responst
    url = reverse('api:list_create') # 'domain/api/'
    res = self.client.get(url, format='json')

    # test response
    self.assertEqual(res.status_code, status.HTTP_200_OK)

  def test_create_post(self):
    self.test_user = User.objects.create_user(username='test_user', password='password')

    data = {
      'title': 'Create Post Title',
      'content': 'Create Post Content',
      'author': 1
    }

    # create api request and get response 
    url = reverse('api:list_create') # 'domain/api/'
    res = self.client.post(url, data, format='json')

    # test response
    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Post.objects.count(), 2) # inlcude setUp object
    self.assertEqual(str(Post.objects.get(id=2)), 'Create Post Title')
