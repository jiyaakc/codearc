from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(CustomerProfile)
admin.site.register(AgentProfile)