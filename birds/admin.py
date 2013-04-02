from django.contrib import admin
from birds.models import Recording


class RecordingAdmin(admin.ModelAdmin):
    fields = ('url', 'common_name', 'catalog_id', 'sp', 'genus')



admin.site.register(Recording, RecordingAdmin)
