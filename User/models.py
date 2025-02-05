from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    """custom manager for User creates user via email for 
    username and checks if the user inputs all the required fields"""
   
    def create_user(self, email, password, name, **extra_fields):

        if not email:
            raise ValueError("وارد نمودن ایمیل الزامی ست")
        if not password:
            raise ValueError("رمز عبور خود را وارد نمایید")
        if not name:
            raise ValueError("نام خود را وارد نمایید")

        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)

        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self.create_user(email, password=password, name=name, **extra_fields)


def user_avatar_path(instance, filename):
    """ Dynamic path to store user avatar to avoid conflict for similar file name"""
    return f'media/User/{instance.email}/avatar/{filename}'



class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # to avoid conflict with django user model
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.name
    