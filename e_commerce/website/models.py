import django.db.models as model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class Products(model.Model):
    product_id = model.AutoField(primary_key=True)
    name = model.CharField(max_length=250)
    description = model.TextField()
    price = model.DecimalField(max_digits=10, decimal_places=2)
    stock = model.IntegerField()
    #created_at = model.DateTimeField(auto_now_add=True)
    #updated_at = model.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Signal to create auth token when a new user is created
@receiver(post_save, sender='website.AuthUser')
def create_auth_user_token(sender, instance=None, created=False, **kwargs):
    if created:
        from rest_framework.authtoken.models import Token
        Token.objects.create(user=instance)


class AuthUser(AbstractUser):
    email = model.EmailField(unique=True)
    user_permissions = None  # Disable user permissions field
    groups = None  # Disable groups field
    first_name = None  # Disable first_name field
    last_name = None  # Disable last_name field

    def __str__(self):
        return self.username

class Customers(model.Model):
    customer_id = model.AutoField(primary_key=True)
    first_name = model.CharField(max_length=100)
    last_name = model.CharField(max_length=100)
    email = model.EmailField(unique=True)
    phone = model.CharField(max_length=20, blank=True)
    address = model.TextField(blank=True)
    city = model.CharField(max_length=100, blank=True)
    country = model.CharField(max_length=100, blank=True)
    created_at = model.DateTimeField(auto_now_add=True)
    updated_at = model.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Categories(model.Model):
    category_id = model.AutoField(primary_key=True)
    name = model.CharField(max_length=250)
    description = model.TextField()   


    def __str__(self):
        return self.name
