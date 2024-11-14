from django.contrib import admin
from blog.models import Blog, BlogGenre, BlogContent, Comment


class BlogContentAdmin(admin.StackedInline):
    model = BlogContent


@admin.register(BlogGenre)
class BlogGenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = (BlogContentAdmin,)
    search_fields = ("title",)
    exclude = ("slug",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog", "user", "created_at")
    search_fields = ("user",)
