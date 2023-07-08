from django.shortcuts import render
# from django.http import HttpResponse
from blog import models
from django.core.paginator import Paginator
from blog.zincsearch import searchIndex
from django.db.models import Count

# 禁用缓存
from django.views.decorators.cache import never_cache

# 工具封装
# 分页
def paginate_queryset(request, queryset, limit):
    paginator = Paginator(queryset, limit)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


# 视图函数
@never_cache
def index(request):
    queryset = models.Post.objects.filter(type = 0).all().order_by('-is_top', '-created_at')
    queryset = paginate_queryset(request, queryset, 3)
    return render(request, 'index.html', {'posts': queryset})

def search(request):
    keys = request.GET.get('q')
    id_list = searchIndex(keys)
    queryset = models.Post.objects.filter(id__in = id_list, type=0).order_by('-is_top', '-created_at')
    return render(request, 'search.html', {'posts': queryset})

def page(request, pname):
    page = models.Post.objects.filter(slug = pname).first()
    return render(request, 'page.html', {'page': page})

def archives(request, pid=None):
    if pid is None:
        date_list = models.Post.objects.dates('created_at', 'month', order='DESC')
        posts = models.Post.objects.distinct().order_by('-created_at')

        # 创建一个字典来存储归档信息
        archives_dict = {}
        for post in posts:
            year = post.created_at.year
            month = post.created_at.month
            day = post.created_at.day
            if year not in archives_dict:
                archives_dict[year] = []
            archives_dict[year].append({'month': month, 'day': day, 'post': post})

        return render(request, 'archives.html', {'date_list': date_list, 'archives_dict': archives_dict})

    post = models.Post.objects.filter(id=pid).first()
    return render(request, 'post.html', {'post': post})

def categories(request, cid=None):
    if cid is None:
        categories = models.Category.objects.annotate(post_count=Count('post')).values('id', 'name', 'post_count')
        return render(request, 'categories.html', {'categories': categories})
    queryset = models.Post.objects.filter(categories__id=cid).order_by('created_at')
    queryset = paginate_queryset(request, queryset, 3)
    return render(request, 'category.html', {'posts': queryset})

def tags(request, tid=None):
    if tid is None:
        tags = models.Tag.objects.annotate(post_count=Count('post'))
        return render(request, 'tags.html', {'tags': tags})
    queryset = models.Post.objects.filter(tags__id=tid).order_by('created_at')
    queryset = paginate_queryset(request, queryset, 3)
    return render(request, 'tag.html', {'posts': queryset})
