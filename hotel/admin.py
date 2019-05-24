from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import reviewer

admin.site.register(Hotel)
admin.site.register(reviewer)
