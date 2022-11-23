
from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,cr_slug=None):
    cr_page=None
    prod=None

    if cr_slug!=None:
        cr_page=get_object_or_404(catg,slug=cr_slug)
        prod=product.objects.filter(catagory=cr_page,avilable=True)
    else:
        prod=product.objects.all().filter(avilable=True)
    cat=catg.objects.all()
    paginator=Paginator(prod,2)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_page)

        
       
    return render(request,'index.html',{'pr':prod,'ct':cat,'pg':pro})


def prodectdetails(requst,cr_slug,product_slug):
    prodot=product.objects.get(catagory__slug=cr_slug,slug=product_slug)
    return render(requst,'iteam.html',{'pr':prodot})
def search(requst):
    qury=None
    prod=None
    if 'q' in requst.GET:

     qury=requst.GET.get('q')
     prod=product.objects.all().filter(Q(name__contains=qury)|Q(disc__contains=qury))
    return render(requst,'search.html',{'qury':qury,'pr':prod})

# Create your views here.
# def home1(request):
#     return render(request,'base.html')

