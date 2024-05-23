from django.db import models


# Create your models here.
class UserProfile(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    username=models.CharField(max_length=250, default='jack')
    email=models.CharField(max_length=250)
    image=models.ImageField(upload_to='profile/%Y/%m/%d')
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    def __str__(self):
        return f'{self.first_name}'


class Post(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='photos/%Y/%m/%d')
    content=models.TextField()
    like=models.BooleanField(default=False)
    tags=models.ManyToManyField('Tag')
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    time_create=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering=['-time_create']

class Tag(models.Model):
    tag=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tag}'
    