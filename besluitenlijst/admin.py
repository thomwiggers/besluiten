from django.contrib import admin
from besluitenlijst.models import Alv, Besluit

class BesluitInline(admin.StackedInline):
  model = Besluit

class AlvAdmin(admin.ModelAdmin):
  inlines = [BesluitInline]

class BesluitAdmin(admin.ModelAdmin):
  search_fields = ['besluit']
  list_display = ('besluit', 'alv', 'volgnummer')

admin.site.register(Alv,AlvAdmin)
admin.site.register(Besluit,BesluitAdmin)

