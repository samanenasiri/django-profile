from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated')
    search_fields = ('title',)
    list_filter = ('updated',)
    raw_id_fields = ('user',)
# Register your models here.
