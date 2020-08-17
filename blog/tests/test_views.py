from django.test import TestCase
from django.urls import reverse

from blog.models import Blog, Blogger


class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_blogs = 9

        test_blogger = Blogger.objects.create(user=None, bio='test bio')
        for blog_id in range(number_of_blogs):
            Blog.objects.create(
                author=test_blogger,
                title=f'test title {blog_id}',
                description=f'test description {blog_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_is_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['blog_list']), 5)
