from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def home(request):

    categories = Category.objects.all()

    featured_products = Product.objects.filter(
        is_available=True,
        stock__gt=0
    ).order_by('-created_at')[:8]

    context = {
        'categories': categories,
        'featured_products': featured_products,
    }

    return render(
        request,
        'home.html',
        context
    )


def category_products(request, category_id):

    category = get_object_or_404(
        Category,
        id=category_id
    )

    products = Product.objects.filter(
        category=category,
        is_available=True,
        stock__gt=0
    )

    context = {
        'category': category,
        'products': products,
    }

    return render(
        request,
        'category_products.html',
        context
    )


def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True
    )

    return render(
        request,
        'product_detail.html',
        {
            'product': product
        }
    )