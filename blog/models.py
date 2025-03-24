from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.safestring import mark_safe


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=[
        (0, "Draft"), (1, "Published")
        ], default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    loves = models.ManyToManyField(User, related_name='blog_loves', blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name="posts", null=True, blank=True
    )
    featured_image = models.ImageField(
        upload_to='post_images', blank=True, null=True
        )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def total_likes(self):
        return self.likes.count()

    def total_loves(self):
        return self.loves.count()

    def get_content_as_html(self):
        """Return the content as safe HTML"""
        return mark_safe(self.content)

    def get_read_time(self):
        """Estimate read time based on
        word count (average 200 words per minute)"""
        word_count = len(self.content.split())
        minutes = word_count / 200
        if minutes < 1:
            return "Less than a minute"
        elif minutes < 2:
            return "1 minute"
        else:
            return f"{int(minutes)} minutes"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
        )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('comment', 'Comment'),
        ('like', 'Like'),
        ('love', 'Love'),
    )

    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notifications'
        )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_notifications'
        )
    notification_type = models.CharField(
        max_length=20, choices=NOTIFICATION_TYPES
        )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
