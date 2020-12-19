from django.urls import path
from django.conf.urls import include, url
from .views import SignUpView, TicketUpdate, TicketDelete, SearchView, AutoReviewUpdate, AutoReviewDelete

from . import views

urlpatterns =[   
   path('signup/', SignUpView.as_view(), name='signup'),
   url('create/', views.create, name='create'),
   url('review/', views.review, name='review'),
   url('flux/', views.flux, name='flux'),
   url('critic/', views.critic, name='critic'),
   url('feed/', views.feed, name='feed'),
   path('update/<int:pk>', TicketUpdate.as_view(), name='update'),
   path('delete/<int:pk>', TicketDelete.as_view(), name='delete'),
   path('ticket_detail/<int:pk>', views.detail, name='ticket_detail'),
   path('followusers', SearchView.as_view(), name='followusers'),
   path('followusers/', views.change_friends, name='change_friends'),
   path('followusers/', views.lose_friends, name='lose_friends'),
   path('follow', views.follow_users, name='follow'),
   path('auto_review_detail/<int:pk>', views.critic_detail, name='auto_review_detail'),
   path('auto_review_update/<int:pk>', AutoReviewUpdate.as_view(), name='update'),
   path('auto_review_delete/<int:pk>', AutoReviewDelete.as_view(), name='delete'),

]