from django.contrib import admin
from .models import Admins,Course,Notes,Assignment,Video#,usercourse

admin.site.register(Admins)
admin.site.register(Course)
admin.site.register(Notes)
admin.site.register(Assignment)
admin.site.register(Video)
# admin.site.register(usercourse)