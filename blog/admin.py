from django.contrib import admin
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if not request.user.has_perm("blog.can_edit_any_post"):
            return False
        return super().has_change_permission(request, obj)
