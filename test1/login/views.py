from django.shortcuts import render
from . import models
# Create your views here.
def Login(request):
    """
    #register
    product1=models.product(name='noshabe',price=100,quantity=100)
    product1.save()
    #update
    product.name='sanevich'
    product.price=250.25
    product.quantity=560
    product.save()
    """
    products=models.product.objects.all()

    product=models.product.objects.filter(id=3).first()
    product.delete()
    return render(request, 'index.html',context={'products':products})
def test(request):
    return render(request, 'test.html')