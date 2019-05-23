from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from main.views import Home, SignUPView , Contact , About , Portfolio ,Project,ProjectView,Profile

app_name = 'main'
urlpatterns = [
    path('main/', Home.as_view(), name="home"),
    path('project/', ProjectView.as_view(), name="project_view"),
    path('portfolio/', Portfolio.as_view(), name="portfolio"),
    path('about/', About.as_view(), name="about"),
    path('contact/', Contact.as_view(), name="contact"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': ''}, name="logout"),
    path('signup/', SignUPView.as_view(), name="signup"),
    path('profile/', Profile.as_view(), name="profile"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += path(
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )
