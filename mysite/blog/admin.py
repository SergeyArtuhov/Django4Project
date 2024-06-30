from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """

    @admin.register(Post) аналогично admin.site.register(Post)

    PostAdmin - класс, который указывает как отображать модель в админке
    list_display - какие поля отображаются в админке в виде столбцов
    list_filter - добавление справа панели для фильтрации объектов
    search_fields - по каким полям будет осуществляться поиск
    prepopulated_fields - (предзаполненное поле) указывает что поле slug формируется в зависимости от title
    raw_id_fields - представление поля в "сыром" виде, по id
    date_hierarchy - иерархия, отображается ниже поля поиска
    ordering - сортировка

    """
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "post", "created", "active"]
    list_filter = ["active", "created", "body"]
    search_fields = ["name", "email", "body"]

