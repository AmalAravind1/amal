from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import product
from .models import Cart,CartItem
# Create your views here.
def _cart_id_(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def cart_add(request,product_id):
    products=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id_(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id_(request))
        cart.save()
    try:
        cart_item=CartItem.objects.get(product=products,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+= 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(product=products,cart=cart,quantity=1)
        cart_item.save()
    return redirect('cartappp:cartdetails')
def cart_details(request, total=0, counter=0,grand=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id_(request))
        cartitems=CartItem.objects.filter(cart=cart,active=True)
        for cartitem in cartitems:
            total += (cartitem.product.price * cartitem.quantity)
            counter += cartitem.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cartitems=cartitems,total=total,counter=counter,grand=grand))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id_(request))
    products=get_object_or_404(product,id=product_id)
    cartitem=CartItem.objects.get(product=products,cart=cart)
    if cartitem.quantity > 1:
        cartitem.quantity -=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cartappp:cartdetails')

def cart_delete(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id_(request))
    products=get_object_or_404(product,id=product_id)
    cartitem=CartItem.objects.get(product=products,cart=cart)

    cartitem.delete()
    return redirect('cartappp:cartdetails')

