from django.shortcuts import render,redirect,get_object_or_404
from shop . models import *
from . models import *
from django .core.exceptions import ObjectDoesNotExist
# Create your views here.
#
def cart_deatails(requset,tot=0,count=0,cart_iteam=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(requset))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quntity)
            count+=i.quntity
    except ObjectDoesNotExist:
        pass

    return render(requset,'cart.html',{'ci':ct_items,'t':tot,'cn':count})
   


def c_id(requset):
    ct_id=requset.session.session_key
    if not ct_id:
        ct_id=requset.session.create()
    return ct_id    


def add_cart(requset,product_id):
    prod=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(requset))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(requset))
        ct.save()

    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quntity < c_items.prodt.stock:
            c_items.quntity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quntity=1,cart=ct)
        c_items.save()
    return redirect('cartDeatails')    



def min(requset,product_id):
    ct=cartlist.objects.get(cart_id=c_id(requset))
    prod=get_object_or_404(product,id=product_id)
    c_item=items.objects.get(prodt=prod,cart=ct)
    if c_item.quntity >1:
        c_item.quntity -=1
        c_item.save()
    else:
        c_item.delete()
    return redirect("cartDeatails")
def cart_delete(requset,product_id):
    mt=cartlist.objects.get(cart_id=c_id(requset))
    pr=get_object_or_404(product,id=product_id)
    citems=items.objects.get(prodt=pr,cart=mt)
    citems.delete()
    return redirect("cartDeatails")