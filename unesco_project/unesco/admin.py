from django.contrib import admin
from unesco.models import site, category, states, regions, iso

# Register your models here.

admin.site.register(category)
admin.site.register(states)
admin.site.register(regions)
admin.site.register(iso)
admin.site.register(site)
