from django.contrib import admin
from .models import Article

# настройка представления в админке - укажем какие колонки будут выводиться в списке Articles:
class ArticleAdmin(admin.ModelAdmin):
    #выведем id и title и дату создания
    list_display = ('id', 'title', 'created_at')


# Register your models here.
admin.site.register(Article, ArticleAdmin)

