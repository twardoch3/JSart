from django.urls import path
from django.contrib.auth import views as auth_views

from main.views import Home, SignUPView , Contact , About , Portfolio

app_name = 'main'
urlpatterns = [
    path('main/', Home.as_view(), name="home"),
    path('portfolio/', Portfolio.as_view(), name="portfolio"),
    path('about/', About.as_view(), name="about"),
    path('contact/', Contact.as_view(), name="contact"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': ''}, name="logout"),
    path('signup/', SignUPView.as_view(), name="signup"),

]
