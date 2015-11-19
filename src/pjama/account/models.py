from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from django.utils.timezone import now

class TeamManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                           **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,username  ,email=None, password=None, **extra_fields):
        return self._create_user(username ,email, password, False, False,
                                 **extra_fields)

    def create_superuser(self,username, email, password, **extra_fields):
        return self._create_user(username , email, password, True, True,
                                 **extra_fields)

class Team(AbstractBaseUser, PermissionsMixin):
    team_name                       =  models.CharField(max_length=255, unique=True)
    organization                    =  models.CharField(max_length=255, blank=True, default='')
    email                            =  models.EmailField(max_length=255)
    problem_num                     =  models.IntegerField(blank=True, null=True, default=0)
    username                        =  models.CharField(max_length=255, unique=True)
    language                        =  models.CharField(max_length=255, default='ja')
    is_admin                        =  models.BooleanField(default=False)
    is_active                       =  models.BooleanField(default=True)
    is_staff                        =  models.BooleanField(default=False)
    created_at                      =  models.DateTimeField(null=True, auto_now_add=True)
    updated_at                      =  models.DateTimeField(blank=True, null=True, auto_now=True)
    objects = TeamManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    class Meta:
        verbose_name="チーム名"
        ordering=['created_at']
        swappable = 'AUTH_USER_MODEL'

    def get_short_name(self):
        "Returns the short name for the user."
        return self.username

