from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Crée et enregistre un utilisateur avec un email et un mot de passe.

        Args:
            email (str): L'email de l'utilisateur.
            password (str): Le mot de passe de l'utilisateur.

        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Crée et enregistre un super utilisateur avec un email et un mot de passe.

        Args:
            email (str): L'email de l'utilisateur.
            password (str): Le mot de passe de l'utilisateur.

        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MarketStreamUser(AbstractBaseUser):
    """
    Classe dont la fonction est de créer un utilisateur avec un email et un mot de passe.

    Attributs:
        email (str): L'email de l'utilisateur.
        is_active (bool): Indique si l'utilisateur est actif.
        is_admin (bool): Indique si l'utilisateur est administrateur.
        is_staff (bool): Indique si l'utilisateur est staff.
    """

    email = models.EmailField(verbose_name="email", max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # permet de créer un utilisateur
    objects = UserManager()

    USERNAME_FIELD = "email"

    # permet de retourner l'email de l'utilisateur
    def __str__(self):
        return self.email

    # Methode qui permet de vérifier si l'utilisateur a les permissions spécifiques
    def has_perm(self, perm, obj=None):
        return True

    # Methode qui permet de vérifier si l'utilisateur a les permissions d'accès à l'application
    def has_module_perms(self, app_label):
        return True
