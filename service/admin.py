from django.contrib import admin
from service.models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display=('name','email','dateTime','peoples','specialrequest')
    
    
admin.site.register(Booking,BookingAdmin)    

