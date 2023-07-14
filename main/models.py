from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import uuid
import os


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")
        user = self.model(

            email=self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_staff = True
        user.is_superuser = True
        return user

def get_profile_image_filepath(self, filename):
    return f'/media/student/profile_images/{self.pk}/{profile_image.png}'

def get_default_profile_image():
    return "/profile_images/profile.svg"

class User(AbstractBaseUser):
    student_index = models.IntegerField(null=True, default=0)
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, default='Enter more about yourself...')
    collage = models.CharField(max_length=50, null=True, default=None)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username

    def get_profile_image_path(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True  

    class Meta:
        db_table = "user"




class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=250, null=True)
    address_2 = models.CharField(max_length=250, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    state_or_region = models.CharField(max_length=250, null=True)
    zip_code = models.IntegerField(null=True)

    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user_info"




class Payment(BaseModel):
    amount = models.IntegerField(null=True)



class Transaction(BaseModel):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    reciever = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    income_type = models.IntegerField(null=True)
    status = models.IntegerField(null=True)

    class Meta:
        db_table = "transaction"




class PaymentItem(BaseModel):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    reciever = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    income_type = models.IntegerField(null=True)
    municipality = models.IntegerField(null=True)
    budget_organization = models.IntegerField(null=True)
    phone_no = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)

    class Meta:
        db_table = "payment_item"



class Subject(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150, default='Enter more about this subject...')
    is_mandatory = models.BooleanField(default=False) 
    class Meta:
        db_table = "subject"