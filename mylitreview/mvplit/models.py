from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
CHOICES = [(i,i) for i in range(6)]

class CustomUser(AbstractUser):
    

    def __str__(self):
        return self.username
    


class Ticket(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tickets')

    class Meta:
        ordering = ['-time_created']
    
    def __str__(self):
        return self.titre

class Review(models.Model):
    ticket = models.ForeignKey(Ticket, default='', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    headline = models.CharField(max_length=128)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']
    
    def __str__(self):
        return self.headline

class AutoReview(models.Model):
    headline = models.CharField(max_length=128)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='images/', default='')
    rating = models.PositiveSmallIntegerField(choices=CHOICES)
    titre = models.CharField(max_length=128, default='')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='auto_reviews')
    body = models.TextField(default='')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']
    
    def __str__(self):
        return self.headline

class CriticAutoReview(models.Model):
    auto_review = models.ForeignKey(AutoReview, on_delete=models.CASCADE, related_name='critic_auto_reviews')
    rating = models.PositiveSmallIntegerField(choices=CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='critic_auto_reviews')
    headline = models.CharField(max_length=128)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.headline

FOLLOW_CHOICES = (
    ("Suivi", "Suivi"),
    ("Suivre", "Suivre"),
)

class Friend(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)


