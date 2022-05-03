from .base import SetUp
from django.urls import reverse
from PIL import Image
from blog.models import Post, Comment, Category, IpPerson
class TestModels(SetUp):
    def test_post_manager_all(self):
        posts = Post.objects.all()
        self.assertIsInstance(posts[0], Post)
        post_count = posts.count()
        Post.objects.create(
            title="My Second Post",
            slug="second-post",
            category="health",
            metadesc="Curious about your health? Look no further!!",
            draft=False,
            # metaimg = ""
            # metaimg_mimetype = ""
            snippet="Long ago, the four nations lived together in harmony.",
            content="Long ago, the four nations lived together in harmony. Then everything changed when the fire nation attacked.",
            # date_posted = ""
            author=self.super_user
            # likes
            # views

        )
        new_post_count = Post.objects.count()
        self.assertEqual(new_post_count, post_count + 1)

    def test_post_manager_active(self):
        active_posts = Post.objects.active()
        self.assertIsInstance(active_posts[0], Post)
        active_posts_count = active_posts.count()
        post3 = Post.objects.create(
            title="My Second Post",
            slug="second-post",
            category="health",
            metadesc="Curious about your health? Look no further!!",
            draft=False,
            # metaimg = ""
            # metaimg_mimetype = ""
            snippet="Long ago, the four nations lived together in harmony.",
            content="Long ago, the four nations lived together in harmony. Then everything changed when the fire nation attacked.",
            # date_posted = ""
            author=self.super_user
            # likes
            # views

        )
        new_active_post_count = Post.objects.active().count()
        self.assertEqual(new_active_post_count, active_posts_count + 1)
        post_draft = post3
        # Needed a new variable, else it wasn't saving.
        post_draft.draft = True
        post_draft.save()
        active_posts_minus_draft = Post.objects.active().count()
        self.assertEqual(active_posts_minus_draft, new_active_post_count - 1)

    def test_category(self):
        Category.objects.create(name="TEST")
        self.assertEqual(self.category1.get_absolute_url(), "/category/TEST/")

    def test_ip_person(self):
        ip_person = IpPerson.objects.create(ip=self.localhost_ip)
        self.assertEqual(str(ip_person), self.localhost_ip)

    def test_post(self):
        self.assertEqual(str(self.post1), "My First Post | test_superuser")
        self.assertEqual(self.post1.get_absolute_url(), "/post/first-post/")

        post_no_slug = Post.objects.create(
            title="No slug given",
            # slug="first-post",
            category="health",
            metadesc="Curious about your health? Look no further!",
            draft=False,
            # metaimg = ""
            snippet="Long ago, the four nations lived together in harmony.",
            content="Long ago, the four nations lived together in harmony. Then everything changed when the fire nation attacked.",
            author=self.super_user
        )
        self.assertEqual(post_no_slug.slug, "no-slug-given")

    def test_comment(self):
        test_comment = Comment.objects.create(post=self.post1, content="I am a comment", author=self.super_user)
        self.assertEqual(str(test_comment), "I am a comment")
        self.assertEqual(test_comment.get_absolute_url(), self.post1_detail_url)

    # Users Models

    def test_profile(self):
        self.assertEqual(str(self.profile1), "test_superuser Profile")
        self.assertEqual(self.profile1.get_absolute_url(), reverse('profile'))
        width, height = 400, 400
        img = Image.new(mode="RGB", size=(width, height))
        img.save(
            "/Users/johnsolly/Documents/code/blogthedata/django_project/media/default.png")
        self.profile1.save()
        with Image.open(self.profile1.image.path) as img:
            self.assertEqual(img.height, 300)
            self.assertEqual(img.width, 300)