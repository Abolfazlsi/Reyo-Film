from django.db import models
from account.models import User
from django.utils.text import slugify
from django.utils.html import format_html
from django.utils import timezone
from django.urls import reverse


class SerialType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None, ):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save()


class SerialGenre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Serial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="serial_image")
    type = models.ManyToManyField("serial.SerialType", related_name="serials")
    category = models.ManyToManyField("serial.Category", related_name="serials")
    genre = models.ManyToManyField("serial.SerialGenre", related_name="serials")
    studio = models.CharField(max_length=200)
    date_arid = models.DateField()
    status = models.BooleanField(default=False)
    score = models.FloatField()
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True, allow_unicode=True)

    def __str__(self):
        return f"{self.title} - {self.description[:30]}"

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Serial, self).save()

    def get_absolute_url(self):
        return reverse("serial:serial_detail", args=[self.slug])

    def show_image(self):
        if self.image:
            return format_html(f"<img src='{self.image.url}' width='70px' height='50px'>")
        return format_html("<h3 style:'color: red;'>No Image</h3>")

    show_image.short_description = 'Image'

    class Meta:
        ordering = ("-created_at",)


class SerialEpisode(models.Model):
    file = models.FileField(upload_to="serial_episodes")
    episode_number = models.IntegerField()
    serial = models.ForeignKey("serial.Serial", on_delete=models.CASCADE, related_name="serial_episodes")

    def __str__(self):
        return f"{self.serial} - {self.episode_number}"


class SerialRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    serial = models.ForeignKey("serial.Serial", on_delete=models.CASCADE, related_name="ratings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.serial}"

    class Meta:
        ordering = ("-created_at",)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    serial = models.ForeignKey("serial.Serial", on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.text}"

    def time_since_creation(self):
        time_delta = timezone.now() - self.created_at
        days = time_delta.days
        hours, remainder = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if days >= 365:
            years = days // 365
            return f"{years} years ago"
        elif days >= 30:
            months = days // 30
            return f"{months} months ago"
        elif days > 0:
            return f"{days} days ago"
        elif hours > 0:
            return f"{hours} hours ago"
        elif minutes > 0:
            return f"{minutes} minutes ago"
        else:
            return f"{seconds} seconds ago"

    class Meta:
        ordering = ("-created_at",)
