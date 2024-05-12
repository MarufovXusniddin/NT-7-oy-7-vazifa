from django.db.models import Count, Avg, Max, Min, Sum, Q
from django.shortcuts import render
from .models import Category, Product


def index(request):
    data = {
        'products': Product.objects.all()
    }
    return render(request,'app/index.html', data)

def product_by_category(request, id):
    data = {
        'products': Product.objects.filter(category_id=id)
    }
    return render(request,'app/index.html', data)

def order_by_alphabet(request):
    data = {
        'products': Product.objects.all().order_by('name')
    }
    return render(request,'app/index.html', data)

def order_by_alphabet_reverse(request):
    products = Product.objects.all().order_by('name')
    data = {
        'products': products.reverse()
    }
    return render(request,'app/index.html', data)

def order_by_price(request):
    data = {
        'products': Product.objects.all().order_by('price')
    }
    return render(request,'app/index.html', data)

def discount(request):
    data = {
        'products': Product.objects.none()
    }
    return render(request,'app/index.html', data)

def discount(request):
    data = {
        'products': Product.objects.filter(discount=True)
    }
    return render(request,'app/index.html', data)

def anotate(request):
    data = {
        'Anotates': Category.objects.anotate(Count('product'))
    }
    return render(request, 'app/index.html', data)

def And(request):
    data = {
        'products': Product.objects.filter(Q(category_id=1) & Q(discount=True))
    }
    return render(request, 'app/index.html', data)


# Qolgan metodlarni bu proyektga ishlatib bo'lmadi