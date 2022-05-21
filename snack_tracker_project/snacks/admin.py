from django.contrib import admin
from .models import Snack

# register the model

# class AdminSnack(admin.ModelAdmin)
#     pass

admin.site.register(Snack)