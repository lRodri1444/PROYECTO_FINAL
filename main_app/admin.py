from django.contrib import admin
from . import models as model

admin.site.register(model.user_object)
admin.site.register(model.new_post)