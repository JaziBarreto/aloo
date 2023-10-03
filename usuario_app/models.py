from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField

class CustomUser(AbstractUser):
    # Campos heredados de AbstractUser
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Campos personalizados
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        help_text=_('Specific permissions for this user.'),
    )
    birthday = models.DateField(null=True, blank=True)

      # Campo de género
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    GOAL_CHOICES = (
        ('Earn weight', _('Earn weight')),
        ('Lose weight', _('Lose weight')),
        ('Physical activity', _('Physical activity')),
    )
    goal = models.CharField(
        max_length=20,
        choices=GOAL_CHOICES,
        default='Earn weight',  # Opción predeterminada
    )
    

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    def __str__(self):
        return self.username

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

    
