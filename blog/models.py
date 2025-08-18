from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog_previews/", verbose_name="Превью", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ["-created_at"]
        permissions = [
            ("can_publish_post", "Может публиковать запись"),
            ("can_edit_any_post", "Может редактировать любую запись"),
            ("can_delete_any_post", "Может удалять любую запись"),
        ]

    def __str__(self):
        return self.title
