from django.contrib import admin
from Chef.models import Chef

class ChefAdmin(admin.ModelAdmin):
    list_display=('name','designation','image')
    
    
admin.site.register(Chef,ChefAdmin)    

