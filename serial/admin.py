from django.contrib import admin
from serial.models import SerialType, Category, SerialGenre, Serial, SerialRating, SerialEpisode, Comment


class SerialEpisodeAdmin(admin.StackedInline):
    model = SerialEpisode


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ("title", "studio", "date_arid", "status", "score", "show_image")
    inlines = (SerialEpisodeAdmin,)
    search_fields = ("title",)
    list_filter = ("studio",)
    exclude = ("slug",)


@admin.register(SerialRating)
class SerialRatingAdmin(admin.ModelAdmin):
    list_display = ("user", "serial", "created_at")


@admin.register(Comment)
class ComeAdmin(admin.ModelAdmin):
    list_display = ("user", "serial")
    search_fields = ("user",)


admin.site.register(SerialType)
admin.site.register(Category)
admin.site.register(SerialGenre)
