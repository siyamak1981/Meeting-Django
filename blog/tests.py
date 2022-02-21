import urllib.parse
from django.urls import reverse,resolve
from django.test import TestCase, testcases
from .views import PostListView
from .models import Post
from tag.models import Tag
from category.models import SubCategory, Category
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth import get_user_model
User = get_user_model()


class BlogPostTests(TestCase):
    def setUp(self):
        category = Category.objects.create(title = "test category", content = 'this is test content category')
        subcategory = SubCategory.objects.create(title='Django subcat', content='Django subcat.', category = category)
        author = User.objects.create_user(first_name='siyamak',last_name = "abasnezhad" , email='jamal@doe.com', password='123')
        published_at = timezone.now()
        self.post = Post.objects.create(title='Django', summary = "Django summary test blog post", author = author, banner="https://static.vecteezy.com/system/resources/previews/002/375/042/non_2x/abstract-background-wave-radial-ellipse-free-vector.jpg",subcategory = subcategory, content='Django board.', published_at = published_at)
        self.post.tag.create(title = "test tag", status = 1)
        self.response = self.client.get(reverse('blog:create'))


#     def test_status_code_post_create(self):
#         self.assertEquals(self.response.status_code, 302)


#     def test_status_code_post_list(self):
#         view = resolve('/blog/list/')
#         self.assertEquals(view.func.view_class, PostListView)
    

#     def test_status_code_post_update(self):
#         url = reverse('blog:update', kwargs={'pk':self.post.pk})
#         self.assertEqual(self.client.get(url).status_code, 200)


#     def test_csrf(self):
#         url = reverse('blog:update', kwargs={'pk': self.post.pk})
#         response = self.client.get(url)
#         self.assertContains(response, 'csrfmiddlewaretoken')
 

#     def test_update_view_contains_link_to_post_list_page(self):
#         url = reverse('blog:update', kwargs={'pk':self.post.pk})
#         x = reverse('blog:list')
#         response = self.client.get(url)
#         self.assertContains(response, 'href="{}"'.format(x))

    # def test_redirection(self):
    #     response = self.client.get(reverse('blog:list'), follow=True)
    #     expected_url = reverse('login') + "?next=" + urllib.parse.quote(reverse('blog:list'), "")
    #     self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)
    

#     def test_new_post_valid_data(self):
#         url = reverse('blog:create')
#         data = {
#             'summary': 'Test title',
#             'content': 'Lorem ipsum dolor sit amet'
#         }
#         response = self.client.post(url, data)
#         self.assertTrue(Post.objects.exists())
    

#     def test_new_post_invalid_data(self):
#         '''
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         '''
#         url = reverse('blog:create')
#         response = self.client.post(url, {})
#         self.assertEquals(response.status_code, 302)

    
#     def test_new_post_invalid_post_data_empty_fields(self):
#         '''
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         '''
#         url = reverse('blog:create')
#         data = {
#             'title': '',
#             'summary': '',
#             'content': ''
#         }
#         response = self.client.post(url, data)
#         self.assertEquals(response.status_code, 302)
#         self.assertFalse(Post.objects.exists())


    
#     def test_contains_form(self):  # <- new test
#         url = reverse('blog:update', kwargs={'pk': self.post.pk})
#         response = self.client.post(url, {})
#         form = response.context.get('form')
#         self.assertIsInstance(form, PostForm)


#     def test_new_post_invalid_post_data(self):  # <- updated this one
#         '''
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         '''
#         url = reverse('blog:update', kwargs={'pk': self.post.pk})
#         response = self.client.post(url, {})
#         form = response.context.get('form')
#         self.assertEquals(response.status_code, 200)
#         self.assertTrue(form.errors)