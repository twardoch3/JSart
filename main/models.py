from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cv = models.TextField(verbose_name="Coś o sobie...", blank=True)
    image = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username']

    def __str__(self):
        return self.username


class Project(models.Model):
    title = models.CharField(max_length=128, verbose_name="Tytuł projektu")
    description = models.TextField(verbose_name="Opis projektu", blank=True)
    last_modified = models.DateTimeField(auto_now=True, verbose_name="Data/godzina edycji")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")

    def __str__(self):
        return f'Projekt: {self.title}, Autor: {self.user}'


class Comment(models.Model):
    comment = models.TextField(verbose_name="Komentarz")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Projekt")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")
    adding_date = models.DateTimeField(auto_now_add=True, verbose_name="Data/godzina dodania")
    last_modified = models.DateTimeField(auto_now=True, verbose_name="Data/godzina edycji")


    def __str__(self):
        return f'{self.comment}, Użytkowni: {self.user}'
