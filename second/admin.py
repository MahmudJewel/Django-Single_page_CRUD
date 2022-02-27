from django.contrib import admin
from second.models import Tag, Descriptions #, MembershipInline
# Register your models here.

lst = [Tag, Descriptions]
admin.site.register(lst)