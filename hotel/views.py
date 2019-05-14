from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import Hotel

def home(request):
    search = request.GET.get('search_hotel', '')
    q = Hotel.objects.all()
    kota = request.GET.get('kota', '')
    provinsi = request.GET.get('provinsi', '')    
    if search != '':
        q = q.filter(nama__contains=search)
    if kota != '':
        q = q.filter(kota=kota)
    if provinsi != '':
        q = q.filter(provinsi=provinsi)

    return render(request, 'hotel/index.html', { 'songs': q, 'location' : getlocation() } )

def getharga(request):
    getharga = request.GET.get()

def getlocation():
    getloc = Hotel.objects.all()
    return getloc.values('kota','provinsi')




