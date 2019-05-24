from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import Hotel,reviewer
from .import forms

def home(request):
    search = request.GET.get('search_hotel', '')
    q = Hotel.objects.all().order_by('-timestamp')
    kota = request.GET.get('kota', '')
    provinsi = request.GET.get('provinsi', '')
    minprice = request.GET.get('harga_minimum','')
    if minprice !='':
        minprice = strToint(minprice) 
    maxprice = request.GET.get('harga_maksimum','')
    if maxprice !='':
        maxprice = strToint(maxprice)

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

def strToint(s):
    try:
        convert = int(s,10)
    except:
        return ''
    return convert

def review(request, pk):
    hotels = get_object_or_404(Hotel, pk=pk,)
    if request.method == 'POST':
        form = forms.Reviews(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ratinghotel = hotels
            review.save()
            return redirect('home')
    else:
        form = forms.Reviews()
    return render(request, 'hotel/review.html', {'form':form, 'hotel':hotels, })

def view(request, pk):
    hotels = get_object_or_404(Hotel, pk=pk)
    b = Hotel.objects.get(pk=pk)
    b = b.reviewer_set.all()
    #b = Hotel.objects.all()
    #b = b_set.all()
    return render(request, 'hotel/view.html', { 'hotel':hotels, 'b':b , })
    




