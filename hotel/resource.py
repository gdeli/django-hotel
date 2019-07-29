from import_export import resources
from .models import Hotel

class HotelResource(resources.ModelResource):
    class Meta:
        model = Hotel