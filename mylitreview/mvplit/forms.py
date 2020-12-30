from django import forms
from django.db import models
from django.conf import settings
from django.forms import RadioSelect
from django.contrib.auth.models import User
from .models import Ticket, Review, AutoReview, CriticAutoReview, Profile

CHOICES = [(i,i) for i in range(6)]
FOLLOW_CHOICES=(
	("Suivi", "Suivi"),
	("Suivre", "Suivre"),
	)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'lieu', 'date_naissance', 'avatar')

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
