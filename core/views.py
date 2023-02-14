from django.shortcuts import render


from store.models import Product


def frontpage(request):
    products = Product.objects.all()[0:6]

    return render(request, 'core/frontpage.html', {
        'products': products
    })

def viziune(request):
    return render(request, 'core/viziune.html')

def contact(request):
    return render(request, 'core/contact.html')

def actiune(request):
    return render(request, 'core/actiune.html')

def adventura(request):
    return render(request, 'core/adventura.html')

def fantezie(request):
    return render(request, 'core/fantezie.html')

def educatie(request):
    return render(request, 'core/educatie.html')

def religie(request):
    return render(request, 'core/religie.html')
