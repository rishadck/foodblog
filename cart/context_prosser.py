from.models import*
from.views import*


def count(requset):
    iteam_count=0
    if 'admin' in requset.path:
        return{}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=c_id(requset))
            cti=items.objects.all().filter(cart=ct[:1])
            for i in cti:
                iteam_count+=i.quntity
        except cartlist.DoesNotExist:
            iteam_count=0
        return dict(itc=iteam_count)


