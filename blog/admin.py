from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ("title", "post_content")
    prepopulated_fields = {"slug": ("title", "author")}

admin.site.register(Post, PostAdmin)