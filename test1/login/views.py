from django.shortcuts import render,redirect
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
    product=models.product.objects.filter(id=3).first()



    for product in products:
        product.delete()
   """
    products = models.product.objects.all()
    return render(request, 'index.html',context={'products':products})
def test(request):
    return render(request, 'test.html')
def create(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        price = request.GET.get('price')
        quantity = request.GET.get('quantity')
        product=models.product(name=name,price=price,quantity=quantity)
        product.save()
        return redirect('login')