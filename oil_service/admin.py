from django.contrib import admin
from .models import (ClientsDataModel,
                     ClubAdminsModel,
                     ChronosModel
                     )


# Register your models here.
admin.site.register(ClientsDataModel)
admin.site.register(ClubAdminsModel)
admin.site.register(ChronosModel)
