from django.contrib import admin
from .models import Article

# настройка представления в админке - укажем какие колонки будут выводиться в списке Articles:
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'created_at') #выведем id и title и дату создания
    list_display_links = ('id', 'title') # эти поля будут ссылками
    search_fields = ('title', 'content') #поле поиска, будет поиск в: title и content


# Register your models here.
admin.site.register(Article, ArticleAdmin)

