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
    
    #test post detail page and view
    def test_post_detail_view(self):
        response = self.client.get('/blog/post/1/')
        no_response = self.client.get('/blog/post/9999/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Just test Title')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
    
    #test get_absolute_url method
    def test_method_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/blog/post/1/')

    #test for create post in our site
    def test_blog_post_create_view(self):
        response = self.client.post(reverse('post_new'),{
            'title': 'Test Title',
            'body': 'Test Body Text',
            'author': self.user, 
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Body Text')
    

    def test_blog_post_update_view(self):
        # reverse build url like this http://localhost:8000/blog/post/1/edit/
        response = self.client.post(reverse('blog_post_edit', args='1'),{
            'title': 'Changed post',
            'body': 'Changed body',
        })
        self.assertEqual(response.status_code, 302)
    

    def test_blog_post_delete_view(self):
        # reverse method in delete build url like this 
        # http://localhost:8000/blog/post/1/delete/
        response = self.client.get(
            reverse('blog_post_delete', args='1')
        )
        self.assertEqual(response.status_code, 200)


    


        


