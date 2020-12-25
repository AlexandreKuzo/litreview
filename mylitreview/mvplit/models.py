from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
CHOICES = [(i,i) for i in range(6)]
FOLLOW_CHOICES = (
    ("Suivre", "Je suis"),
    ("Ne pas suivre", "Ne pas suivre"),
)
    


class Ticket(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')

    class Meta:
        ordering = ['-time_created']
    
    def __str__(self):
        return self.titre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='images/')
    bio = models.TextField(max_length=200, blank=True)
    lieu = models.CharField(max_length=50, blank=True)
    followed = models.ManyToManyField(User, default=None, blank=True, related_name='followed')
    date_naissance = models.DateField(null=True, blank=True)

    @property
    def nbr_followers(self):
        return self.followed.all().count()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

	def __str__(self):
		return self.user

class Review(models.Model):
    ticket = models.ForeignKey(Ticket, default='', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auto_reviews')
    body = models.TextField(default='')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']
    
    def __str__(self):
        return self.headline

class CriticAutoReview(models.Model):
    auto_review = models.ForeignKey(AutoReview, on_delete=models.CASCADE, related_name='critic_auto_reviews')
    rating = models.PositiveSmallIntegerField(choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='critic_auto_reviews')
    headline = models.CharField(max_length=128)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.headline

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    value = models.CharField(choices=FOLLOW_CHOICES, default='Follow', max_length=15)

    def __str__(self):
        return str(self.username)








