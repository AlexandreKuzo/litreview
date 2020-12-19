from django import forms
from django.db import models
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import RadioSelect
from django.forms.models import ModelChoiceField
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import CustomUser, Ticket, Review, AutoReview, CriticAutoReview

CHOICES = [(i,i) for i in range(6)]

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        labels = {
            "username": "Pseudo",
            "email": "E-mail"
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CreateForm(forms.Form):
    titre = forms.CharField(label="Titre", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    image = forms.FileField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'headline', 'body')
        widgets = {
            'rating': RadioSelect(choices=CHOICES),
        }
        labels = {
            "rating": "Note",
            "headline": "Titre",
            "body": "Commentaire"
        }


class AutoReviewForm(forms.ModelForm):
    class Meta:
        model = AutoReview
        fields = ('headline', 'description', 'image', 'titre', 'rating', 'body')
        widgets = {
            'rating': RadioSelect(choices=CHOICES),
        }
        labels = {
            "headline": "Titre",
            "description": "Description",
            "image": "Image",
            "titre": "Avis",
            "rating": "Note",
            "body": "Commentaire"
        }


class CriticAutoReviewForm(forms.ModelForm):
    class Meta:
        model = CriticAutoReview
        fields = ('rating', 'headline', 'body')
        labels = {
            "rating": "Note",
            "headline": "Avis",
            "body": "Commentaire"
        }
        widgets = {
            'rating': RadioSelect(choices=CHOICES),
        }





