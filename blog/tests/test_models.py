from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Blogger, Blog, Comment


class BloggerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(username='testuser1', password='fai2Thie')
        Blogger.objects.create(user=test_user1, bio='bio')

    def test_bio_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_user_name(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(str(blogger), str(blogger.user))

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(blogger.get_absolute_url(), '/blog/blogger/1')


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(title='test title', description='test description', author=None)

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_blog_title(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(str(blog), blog.title)

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.get_absolute_url(), '/blog/1')


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_blog1 = Blog.objects.create(title='test title', description='test description', author=None)
        Comment.objects.create(author=None, blog=test_blog1, description='test comment description')

    def test_comment_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_comment_description(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(str(comment), comment.description)
