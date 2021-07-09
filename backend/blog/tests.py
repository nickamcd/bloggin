from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):
  def setUp(self):
    test_user = User.objects.create_user(username='test-user', 
                                         password='password')
    test_post = Post.objects.create(title='Test Title', 
                                    content='Test Content', author_id=1)

  def test_post_attributes(self):
    post = Post.objects.get(id=1)
    
    title = f'{post.title}'
    content = f'{post.content}'
    author = f'{post.author}'
    
    self.assertEqual(title, 'Test Title')
    self.assertEqual(content, 'Test Content')
    self.assertEqual(author, 'test-user')

    self.assertEqual(str(post), 'Test Title')

