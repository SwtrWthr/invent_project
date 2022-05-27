from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None):
    if not email:
      return ValueError("Users must have an email address")
    if not first_name:
      return ValueError("Users must have a first name")

    user = self.model(
      email=self.normalize_email(email).lower(),
      first_name=first_name,
      last_name=last_name,
      password=password,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, first_name = 'Admin', last_name = 'Admin', password=None):
    user = self.create_user(
      email=self.normalize_email(email),
      password=password,
      first_name=first_name,
      last_name=last_name
    )
    user.is_admin = True
    user.save(using=self._db)
    return user


class Role(models.Model):
  title = models.CharField(max_length=100, unique=True)
  
  @classmethod
  def get_default_pk(cls):
    role, created = cls.objects.get_or_create(
      title='Manager'
    )
    return role.pk

  def __str__(self):
    return self.title

  class Meta:
    db_table = "roles"


class User(AbstractBaseUser):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64, null=True, blank=True)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=11, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(null=True, blank=True)
  role = models.ForeignKey(Role, on_delete=models.PROTECT, default=Role.get_default_pk)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELD = ['first_name']
  objects = UserManager()

  class Meta:
    db_table = "users"
  
  def get_full_name(self):
    return self.first_name + ' ' + self.last_name

  def get_short_name(self):
    return self.first_name

  @property
  def is_superuser(self):
    return self.is_admin

  @property
  def is_staff(self):
    return self.is_admin

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, app_label):
    return self.is_admin
  
  def __str__(self):
      return self.email


# Create your models here.
