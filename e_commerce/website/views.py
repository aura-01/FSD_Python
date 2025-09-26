from django.shortcuts import render
import django.http as http
from website.models import Products
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
    #modify below code to interact with the database using Django ORM
    #products = Products.objects.get(pk=12)
    #products.name = "HP Laptop"
    #products.price = 60000.00
    #products.stock = 15
    #products.description = "This is the next generation HP Laptop with advanced features."
    #products.save()
    # delete a product
    #try:
    #    products = Products.objects.get(pk = 2)
    #    if products is not None:
    #        products.delete()
    #except Exception as e:
    #    print("Error deleting product:", e)
    # filter products with price greater than 500
    #products = Products.objects.filter(price__gt=500)
    #create new products
    #Products.objects.create(name="Smartphone", description="Latest model smartphone", price=699.99, stock=50)
    #Products.objects.create(name="Laptop", description="High performance laptop", price=1299.   99, stock=30)
    #Products.objects.create(name="Headphones", description="Noise-cancelling headphones", price=199.99, stock=100)
    #Products.objects.create(name="Smartwatch", description="Feature-rich smartwatch", price=249.99, stock=20)
    if request.user.is_authenticated:
        print("User is authenticated")  
    else:
        print("User is not authenticated")
    products = Products.objects.all()
    data = {'products': products,
            #'title': 'Home - E-Commerce Website',
            #'description': 'Welcome to our E-Commerce Website'
            }
    return render(request, 'website/index.html',data)

def about(request):
    return render(request, 'website/about.html', {'title': 'About - E-Commerce Website'})

def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact - E-Commerce Website'})

#def search(request):
 #   return http.HttpResponse("This is the search page.")

def search(request):
    data = {'title': 'Search - E-Commerce Website'}
    return render(request, 'website/index.html', data)

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #return redirect('home')
        return render(request, 'website/login.html', {'title': 'Login - E-Commerce Website'})
    else:
        return render(request, 'website/login.html', {'title': 'Login - E-Commerce Website', 'error': 'Invalid credentials'})

def logout_view(request):
    logout(request)
    return render(request, 'website/logout.html', {'title': 'Logout - E-Commerce Website'})

