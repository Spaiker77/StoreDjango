from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.shortcuts import redirect
from .models import BlogPost
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

class BlogListView(ListView):
    """Список опубликованных статей"""
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Показываем только опубликованные статьи
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    """Детальный просмотр статьи с увеличением просмотров"""
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()

        # Доп. задание: отправить письмо при 100 просмотрах
        if obj.views == 100:
            send_mail(
                subject='Поздравляем!',
                message=f'Статья "{obj.title}" достигла 100 просмотров!',
                from_email='admin@yourdomain.com',
                recipient_list=['your_email@example.com'],  # Заменить на свой
                fail_silently=True
            )
        return obj


class BlogCreateView(CreateView):
    """Создание новой статьи"""
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    """Редактирование статьи"""
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    """Удаление статьи"""
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

class BlogPostUpdateView(PermissionRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
    permission_required = 'blog.can_edit_any_post'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('blog.can_edit_any_post'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
