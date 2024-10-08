from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.validators import UnicodeUsernameValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur")

        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUserModel(AbstractBaseUser):
    TYPE_CHOICES = [
        ('LOCATAIRE', 'LOCATAIRE'),
        ('PROPRIETAIRE', 'PROPRIETAIRE'),
    ]

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator],
                                help_text="Obligatoire ! 150 caractères ou moins. Seuls les lettres, chiffres et @/./+/-/_.",
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                }, verbose_name="Nom d'utilisateur "
                                )
    first_name = models.CharField(max_length=30, verbose_name="Nom ")
    last_name = models.CharField(max_length=60, verbose_name="Prénoms ")
    email = models.EmailField(unique=True, verbose_name="Email ")
    phone_number = models.CharField(max_length=15, verbose_name="Téléphone ")
    num_cni = models.CharField(max_length=250, unique=True, verbose_name="Numéro de la CNI ")
    image_recto = models.ImageField(upload_to='CNI/', verbose_name="Image du recto ")
    image_verso = models.ImageField(upload_to='CNI/', verbose_name="Image du verso ")
    user_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='LOCATAIRE', verbose_name="Type d'utilisateur ")
    slug = models.SlugField(unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(uuid.uuid4())

        super(CustomUserModel, self).save(*args, **kwargs)
