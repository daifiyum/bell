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

    title = models.CharField(max_length=100, verbose_name="标题")
    slug = models.CharField(max_length=255, null=True, blank=True, verbose_name="别名")
    content = models.TextField(verbose_name="文章")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.PROTECT, verbose_name="分类")
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
    
# 用户模型
class UserProfile(models.Model):
    USER_GENDER_TYPE = (
        ('male', '男'),
        ('female', '女'),
    )
    
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = '用户')
    nike_name = models.CharField('昵称', max_length=50, blank=True, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=6, choices=USER_GENDER_TYPE, default='male')
    address = models.CharField('地址', max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100, verbose_name = '用户头像')
