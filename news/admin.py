from django.contrib import admin
from .models import MyModel
from mce_filebrowser.admin import MCEFilebrowserAdmin
from .models import NewsData, Activity, Reference, Team, Partners, Contacts

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)

admin.site.register(NewsData)
admin.site.register(Activity)
admin.site.register(Reference)
admin.site.register(Team)
admin.site.register(Partners)
admin.site.register(Contacts)
