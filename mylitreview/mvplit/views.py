from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from itertools import chain
from django.urls import reverse
from django.db.models import CharField, Value, Q
from django.views.generic import UpdateView, TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import AbstractUser, Ticket, Review, CustomUser, AutoReview, Friend
from .forms import AutoReviewForm, CriticAutoReviewForm


# Create your views here.

from .forms import CustomUserCreationForm, CreateForm, ReviewForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy
    template_name = 'registration/signup.html'

def create(request):
    form = CreateForm(request.POST, request.FILES or None)
    if form.is_valid():
        ticket = Ticket()
        ticket.user = request.user
        ticket.titre = form.cleaned_data["titre"]
        ticket.description = form.cleaned_data["description"]
        ticket.image = request.FILES["image"]
        ticket.save()
        sauvegarde = True
    else:
        form = CreateForm()
    form = CreateForm()
    return render(request, 'create.html', {
        'form':form
    })

def review(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = Review()
        review.user = request.user
        review.rating = form.cleaned_data["rating"]
        review.headline = form.cleaned_data["headline"]
        review.body = form.cleaned_data["body"]
    else:
        form = ReviewForm()
    form = ReviewForm()
    return render(request, 'review.html', {
        'form':form
    })

def flux(request):
    tickets = Ticket.objects.filter()
    return render(request, 'flux.html', {
        'tickets': tickets
    })

def detail(request, pk):
    template_name = "ticket_detail.html"
    ticket = get_object_or_404(Ticket, pk=pk)
    reviews = ticket.reviews.filter().order_by("-time_created")
    new_review = None
    # Nouvelle review
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            # Creation review mais on ne la sauve pas tout de suite
            new_review = review_form.save(commit=False)
            # On assigne la review au ticket concerné
            new_review.ticket = ticket
            # On definit l'user comme auteur
            new_review.user = request.user
            # On sauvegarde la review
            new_review.save()
    else:
        review_form = ReviewForm()
    
    review_form = ReviewForm()

    return render(
        request,
        template_name,
        {
            "ticket" : ticket,
            "reviews" : reviews,
            "new_review" : new_review,
            "review_form" : review_form,
        },
        )

def critic_detail(request, pk):
    template_name = "auto_review_detail.html"
    auto_review = get_object_or_404(AutoReview, pk=pk)
    critic_auto_reviews = auto_review.critic_auto_reviews.filter().order_by("-time_created")
    new_critic = None
    # Nouvelle critique
    if request.method == "POST":
        critic_auto_review_form = CriticAutoReviewForm(data=request.POST)
        if critic_auto_review_form.is_valid():
            new_critic = critic_auto_review_form.save(commit=False)
            new_critic.auto_review = auto_review
            new_critic.user = request.user
            new_critic.save()
    else:
        critic_auto_review_form = CriticAutoReviewForm()
    
    critic_auto_review_form = CriticAutoReviewForm()

    return render(
        request,
        template_name,
        {
            "auto_review" : auto_review,
            "critic_auto_reviews" : critic_auto_reviews,
            "new_critic" : new_critic,
            "critic_auto_review_form" : critic_auto_review_form
        },
    )

class TicketUpdate(UpdateView):
    model = Ticket
    context_object_name = "ticket"
    fields = ['titre', 'description']
    template_name = 'ticket_update_form.html'
    
    def get_success_url(self):
        return reverse(feed)

class TicketDelete(DeleteView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "ticket_confirm_delete.html"

    def get_success_url(self):
        return reverse(feed)
    
class AutoReviewUpdate(UpdateView):
    model = AutoReview
    context_object_name = "auto_review"
    fields = ['headline', 'description', 'rating', 'titre', 'body']
    template_name = 'auto_review_update_form.html'

    def get_success_url(self):
        return reverse(feed)

class AutoReviewDelete(DeleteView):
    model = AutoReview
    context_object_name = "auto_review"
    template_name = "auto_review_confirm_delete.html"

    def get_success_url(self):
        return reverse(feed)

def critic(request):
    form = AutoReviewForm(request.POST, request.FILES or None)
    if form.is_valid():
        auto_review = AutoReview()
        auto_review.user = request.user
        auto_review.headline = form.cleaned_data["headline"]
        auto_review.description = form.cleaned_data["description"]
        auto_review.rating = form.cleaned_data["rating"]
        auto_review.titre = form.cleaned_data["titre"]
        auto_review.body = form.cleaned_data["body"]
        auto_review.image = request.FILES["image"]
        auto_review.save()
        sauvegarde = True
    else:
        form = AutoReviewForm()
    form = AutoReviewForm()
    return render(request, 'critic.html', {
        'form':form
    })

class SearchView(ListView):
    model = CustomUser
    template_name = 'followuser.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        object_list = CustomUser.objects.filter(
            Q(username__icontains=query)
        )        
        return object_list

def follow_users(request):
    return redirect('followuser.html')

def feed(request):
    tickets = Ticket.objects.filter()
    auto_reviews = AutoReview.objects.filter()
    return render(request, 'feed.html', {'tickets':tickets, 'auto_reviews':auto_reviews })

def change_friends(request):    
    username = request.user.username
    friend = CustomUser.objects.get(username=username)
    if request.method == "POST":
        Friend.make_friend(request.user, friend)
    return render(request, 'followuser.html', {
        'friend':friend, 
    })

def lose_friends(request):
    username = request.user.username
    friend = CustomUser.objects.get(username=username)
    if request.method == 'POST':
        Friend.lose_friend(request.user, friend)
    return render(request, 'followuser.html', {
        'friend':friend,
    })
