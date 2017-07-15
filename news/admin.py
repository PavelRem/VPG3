from django.contrib import admin
<<<<<<< HEAD

from .models import NewsData, Activity, Reference, Team, Partners, Contacts, Images
=======
from .models import MyModel
from mce_filebrowser.admin import MCEFilebrowserAdmin
from .models import NewsData, Activity, Reference, Team, Partners, Contacts
>>>>>>> 28d1b22af1e2483f2226cef062b2ae99b90c4977

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)

admin.site.register(NewsData)
admin.site.register(Activity)
admin.site.register(Reference)
admin.site.register(Team)
admin.site.register(Partners)
admin.site.register(Contacts)
admin.site.register(Images)
