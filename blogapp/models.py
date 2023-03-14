from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    video = models.CharField(max_length=20, null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField(null=True, blank=True)
    whatsapp = models.CharField(max_length=25, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} commented on {self.post}"


class Email(models.Model):
    name = models.CharField(max_length=20)
    email_address = models.EmailField()
    subject = models.CharField(max_length=20)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} sent an email'
    

