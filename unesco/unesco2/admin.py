from django.contrib import admin
from unesco2.models import unesco_site, unesco_category, unesco_states, unesco_regions, unesco_iso

# Register your models here.

admin.site.register(unesco_category)
admin.site.register(unesco_states)
admin.site.register(unesco_regions)
admin.site.register(unesco_iso)
admin.site.register(unesco_site)
