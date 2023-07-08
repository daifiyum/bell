from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    TYPE_CHOICES = (
        (0, '文章'),
        (1, '页面'),
    )

    title = models.CharField(max_length=100, verbose_name="标题", null=True)
    slug = models.CharField(max_length=255, null=True, blank=True, verbose_name="别名")
    content = models.TextField(verbose_name="文章", null=True)
    categories = models.ManyToManyField(Category, verbose_name="分类")
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    is_top = models.BooleanField(default=False, verbose_name="置顶")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    type = models.IntegerField(choices=TYPE_CHOICES, default=0, verbose_name="类型")

    def __str__(self):
        return self.title

class Menu(models.Model):
    TYPE_CHOICES = (
        ("_self", '默认'),
        ("_blank", '新窗口打开'),
    )
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=1023, null=True, blank=True)
    target = models.CharField(choices=TYPE_CHOICES, max_length=20, null=True, blank=True, default="_self")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_children(self):
        return Menu.objects.filter(parent=self)

    class Meta:
        ordering = ['order']

