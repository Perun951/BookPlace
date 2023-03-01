from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail

from store.models import Product

def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:10]

    return render(request, 'core/frontpage.html', {
        'products': products
    })

def viziune(request):
    return render(request, 'core/viziune.html')

def contact(request):
    return render(request, 'core/contact.html')