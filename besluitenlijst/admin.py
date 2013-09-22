from django.contrib import admin
from besluitenlijst.models import Alv, Besluit, Contributors

class BesluitInline(admin.StackedInline):
  model = Besluit

class AlvAdmin(admin.ModelAdmin):
  inlines = [BesluitInline]

class BesluitAdmin(admin.ModelAdmin):
  search_fields = ['besluit']
  list_display = ('besluit', 'alv', 'volgnummer')

class ContributorAdmin(admin.ModelAdmin):
  model=Contributors

admin.site.register(Alv,AlvAdmin)
admin.site.register(Besluit,BesluitAdmin)
admin.site.register(Contributors,ContributorAdmin)
