from django.db import models
from django.contrib import admin

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    
class Descriptions(models.Model):
    tag = models.ManyToManyField(Tag, related_name='tagRelatedName')
    title = models.CharField(max_length=250, blank=True, null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.title

class Category(models.Model):
    MainCategory = models.CharField(max_length=200, null=True, blank=True)
    SubCategory1 = models.CharField(max_length=200, null=True, blank=True)
    SubCategory2 = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.SubCategory2

# class MembershipInline(admin.TabularInline):
#     model = Descriptions.tag.through

# class TagAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]

# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members',)