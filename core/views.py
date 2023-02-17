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
