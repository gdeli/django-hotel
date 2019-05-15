from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import Hotel

def home(request):
    search = request.GET.get('search_hotel', '')
    q = Hotel.objects.all().order_by('-timestamp')
    kota = request.GET.get('kota', '')
    provinsi = request.GET.get('provinsi', '')
    minprice = request.GET.get('harga_minimum','')
    maxprice = request.GET.get('harga_maksimum','')    
    if search != '':
        q = q.filter(nama__contains=search)
    if kota != '':
        q = q.filter(kota=kota)
    if provinsi != '':
        q = q.filter(provinsi=provinsi)
    if maxprice !='' and minprice != '':
        q = q.filter(harga__gte=minprice,harga__lte=maxprice)
    elif maxprice !='':
        q = q.filter(harga__lte=maxprice)
    elif minprice !='':
        q = q.filter(harga__gte=minprice)

    return render(request, 'hotel/index.html', { 'hotels': q, 'location' : getlocation(), })

    


#def getpricerange(request):
#    minprice = request.GET.get('harga_minimum','')
#    maxprice = request.GET.get('harga_maksimum','')
#    if maxprice !='' and minprice != '':
#        #rangeprice = Hotel.objects.filter(harga__range=(minprice, maxprice))
#        rangeprice = Hotel.objects.filter(harga__gte=minprice,harga__lte=maxprice)
#    return 

   
def getlocation():
    getloc = Hotel.objects.all()
    return getloc.values('kota','provinsi')




