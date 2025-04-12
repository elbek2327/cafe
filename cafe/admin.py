from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from cafe.models import Category, Food

admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Food)