from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Posts

from django.core.mail import send_mail
from django.conf import settings


class PostListView(ListView):
    """
    Альтернативное представление списка постов
    """
    queryset = Posts.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Posts,
                             status=Posts.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


def post_share(request, post_id):
    # Извлечь пост по его идентификатору id
    post = get_object_or_404(Posts,
                             id=post_id,
                             status=Posts.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        # Форма была передана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы успешно прошли валидацию
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s ({cd['email']}) comments: {cd['comments']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
