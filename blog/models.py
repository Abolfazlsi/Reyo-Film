from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from account.models import User


class BlogGenre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogContent(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    blog_image = models.ImageField(upload_to="blogcontent_images")
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE, related_name="blog_contents", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog_image")
    description = models.TextField()
    genre = models.ManyToManyField("blog.BlogGenre", related_name="blogs")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Blog, self).save()

    def get_absolute_url(self):
        return reverse("blog:blog_details", args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_blog")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")

    def __str__(self):
        return f"{self.blog} - {self.user}"

    class Meta:
        ordering = ("-created_at",)
