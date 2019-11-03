from django.contrib import admin
from repository import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Blog)
admin.site.register(models.UserRelationship)
admin.site.register(models.Reporting)
admin.site.register(models.Article)
admin.site.register(models.ArticleDetial)
admin.site.register(models.Classification)
admin.site.register(models.Caption)
admin.site.register(models.Comment)
admin.site.register(models.ArticleToCaption)
admin.site.register(models.Perference)

