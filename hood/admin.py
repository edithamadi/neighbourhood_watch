from django.contrib import admin
from .models import Neighbourhood,Business,Post,Profile,Comment,Location,category
# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(category)