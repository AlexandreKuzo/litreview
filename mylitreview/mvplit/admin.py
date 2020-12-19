from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Ticket, Review, AutoReview


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

class TicketAdmin(admin.ModelAdmin):
    list_filter = ('id', 'time_created', 'user')
    list_display = ('user', 'image')

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('id', 'time_created')
    list_display = ('user', 'body', 'ticket')

class AutoReviewAdmin(admin.ModelAdmin):
    list_filter = ('id', 'time_created')
    list_display = ('user', 'description', 'rating')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(AutoReview, AutoReviewAdmin)




