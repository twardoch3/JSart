from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.http import HttpResponse

from main.models import User, Project
from main.forms import MainUserCreationForm

class Home(View):

    def get(self, request):
        return render(request, 'main/home.html')

class Portfolio(View):

    def get(self, request):
        return render(request, 'main/portfolio.html' ,{'projects':Project.objects.all()})


class ProjectView(View):

    def get(self, request):
        id = request.GET['id']

        return render(request, 'main/project_view.html',{'projects':Project.objects.get(id=id)})




class Contact(View):

    def get(self, request):
        return render(request, 'main/contact.html')



class About(View):

    def get(self, request):
        return render(request, 'main/contact.html')




class SignUPView(View):
    # Creating a new user
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = MainUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.email = form.cleaned_data.get('email')
            new_user.cv = form.cleaned_data.get('cv')
            new_user.image = form.cleaned_data.get('image')
            new_user.save()
            # authenticate and login new user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('main:home'))
        return render(request, 'registration/signup.html', {'form': form})
