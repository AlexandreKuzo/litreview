from django.contrib import admin

from .models import Ticket, Review, AutoReview


class TicketAdmin(admin.ModelAdmin):
    list_filter = ('id', 'time_created', 'user')
    list_display = ('user', 'image')


class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('id', 'time_created')
    list_display = ('user', 'body', 'ticket')


class AutoReviewAdmin(admin.ModelAdmin):
    list_filter = ('id', 'time_created')
    list_display = ('user', 'description', 'rating')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(AutoReview, AutoReviewAdmin)
