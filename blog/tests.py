from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='john',
            email='example@gmail.com',
            password='password123'
        )

        self.post = Post.objects.create(
            title='Just test Title',
            body='Just Test body',
            author=self.user,
        )


    def test_string_object_title(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)
    

    def test_post_information(self):
        self.assertEqual(f'{self.post.title}', 'Just test Title' )
        self.assertEqual(f'{self.post.author}', 'john')
        self.assertEqual(f'{self.post.body}', 'Just Test body')
    
    def test_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) #200 == 200
        self.assertContains(response, 'Just Test body')
        self.assertTemplateUsed(response, 'blog/index.html')
        

