from django.contrib import admin
from blog.models import Tag, Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "published_at"]
    # exclude = ["published_at"]

admin.site.register(Tag)
# admin.site.register(Post, PostAdmin)

# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ["creator"]
