from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Hotel Melati Admin"
admin.site.site_title = "Hotel Admin Portal"
admin.site.index_title = "Welcome Hotel Admin"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('hotel.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)