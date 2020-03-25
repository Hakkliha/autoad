from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
) 
# Create your models here.

GENDERS = (('male', 'Male'), ('female', 'Female'))

class UserManager(BaseUserManager):
	def create_user(self, email, first_name=None, last_name=None, gender=None, birthday=None, password=None, is_active=True, is_staff=False, is_admin=False):
		if not email:
			raise ValueError('Users must have an email address.')
		if not password:
			raise ValueError('Users must have a password.')
		if not first_name:
			raise ValueError('Users must have a first name.')
		if not last_name:
			raise ValueError('Users must have a last name.')
		if not gender:
			raise ValueError('Users must have a gender.')
		if not birthday:
			raise ValueError('Users must have a birthday.')
		user_obj = self.model(
			email = self.normalize_email(email),
			first_name=first_name,
			last_name=last_name,
			gender=gender,
			birthday=birthday
		)
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, email, first_name=None, last_name=None, gender=None, birthday=None, password=None):
		user = self.create_user(
			email,
			first_name=first_name,
			last_name=last_name,
			gender=gender,
			birthday=birthday,
			password=password,
			is_staff=True
		)
		return user

	def create_superuser(self, email, first_name=None, last_name=None, gender=None, birthday=None, password=None):
		user = self.create_user(
			email,
			first_name=first_name,
			last_name=last_name,
			gender=gender,
			birthday=birthday,
			password=password,
			is_staff=True,
			is_admin=True
		)
		return user


class User(AbstractBaseUser):
	email 			= models.EmailField(unique=True, max_length=255)
	active			= models.BooleanField(default=True) # can login
	staff			= models.BooleanField(default=False) # staff user non superuser
	admin			= models.BooleanField(default=False) # superuser
	email_verified 	= models.BooleanField(default=False)
	id_verified		= models.BooleanField(default=False)
	first_name		= models.CharField(max_length=60, null=True)
	last_name		= models.CharField(max_length=60, null=True)
	gender			= models.CharField(choices=GENDERS, max_length=20, null=True)
	birthday		= models.DateField(auto_now_add=False, max_length=15, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.first_name + ' ' + self.last_name

	def get_short_name(self):
		return self.first_name

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active