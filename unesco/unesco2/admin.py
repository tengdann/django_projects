from django.contrib import admin
from unesco2.models import Site, Category, State, Region, Iso

# Register your models here.

admin.site.register(Category)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(Site)
