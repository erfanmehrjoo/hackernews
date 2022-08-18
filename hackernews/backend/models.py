from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class UserWithPhoto(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)
    def __str__(self):
        return self.user.username
class Links(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    userph = models.ForeignKey(UserWithPhoto , on_delete=models.CASCADE , blank=True , null=True )
    votes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Links.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
        
    def save(self, *args, **kwargs):
        self.slug = self._get_unique_slug()
        return super().save(*args, **kwargs)

class Message(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    links = models.ForeignKey(Links , on_delete=models.CASCADE)
    userph = models.ForeignKey(UserWithPhoto , on_delete=models.CASCADE , blank=True , null=True )
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated' , '-created']

    def __str__(self):
        return self.body[0:50]