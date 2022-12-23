from django import template

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/snippets/recent_posts.html')
def render_recent_posts():
    posts = Post.objects.filter(status='published')
    recent_posts = posts.order_by('-created')[:6]
    return {
        'recent_posts': recent_posts
    }


@register.inclusion_tag('blog/snippets/popular_posts.html')
def render_popular_posts():
    posts = Post.objects.filter(status='published', is_popular=True)
    popular_posts = posts.order_by('-created')[:6]
    return {
        'popular_posts': popular_posts
    }


@register.inclusion_tag('blog/snippets/top_posts.html')
def render_top_posts():
    posts = Post.objects.filter(status='published', is_on_top=True)
    top_posts = posts.order_by('-created')[:6]
    return {
        'top_posts': top_posts
    }


