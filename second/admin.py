from django.contrib import admin
from second.models import Tag, Descriptions,Category # MembershipInline
# Register your models here.

lst = [Tag, Descriptions, Category]
admin.site.register(lst)
