from django.contrib import admin

from .models import Blogger, Blog, Comment

admin.site.register(Blogger)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'author')


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_filter = ('datetime',)
    list_display = ('title', 'author')
    inlines = [CommentInline]
