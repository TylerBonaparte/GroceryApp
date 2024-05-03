# grocery/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, CartItem
from .models import CartItem
from .forms import AddToCartForm
from .forms import AddItemForm
from django.shortcuts import render
from .models import Item
from django.shortcuts import render, get_object_or_404
from .models import Category

def home(request):
    return render(request, 'home.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def about_us(request):
    company_name = "Tyler's Shopping Center"
    description = "Welcome to our online grocery store. We aim to provide the best shopping experience for our customers."
    return render(request, 'about_us.html', {'company_name': company_name, 'description': description})

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        # For example, you might process the form data and send an email
        # Here, we're just rendering a thank you page for demonstration purposes
        return render(request, 'contact_thank_you.html')
    else:
        # Render the contact form
        return render(request, 'contact.html')
    
def cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

@login_required
def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    user = request.user
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(item=item, user=user)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return redirect('item_list')
    else:
        form = AddToCartForm()
    return render(request, 'add_to_cart.html', {'form': form, 'item': item})

@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view
            return redirect('item_list')
    else:
        form = AddItemForm()
    return render(request, 'add_item.html', {'form': form})

def list_items(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})


