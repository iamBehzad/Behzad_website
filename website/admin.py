from django.contrib import admin
from website.models import Contact,Proj_Cert,Type
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('name', 'email', 'created_date', )
    list_filter = ['email']
    search_fields=['name', 'message']
class Proj_CertAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('title', 'type', 'created_date', )
    list_filter = ['type']
    search_fields=['title', 'content']    
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Type)
admin.site.register(Proj_Cert, Proj_CertAdmin)