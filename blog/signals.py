from django.db.models.signals import post_save, pre_delete, post_migrate
from django.dispatch import receiver
from .models import Post
from .zincsearch import addIndex, updateIndex, delIndex, initIndex

# 初始化 zincsearch 索引数据库
@receiver(post_migrate)
def initialize_zinc_search(sender, **kwargs):
    if sender.name == 'blog':
        initIndex()


# zincsearch 索引自动创建

# 增、改数据
@receiver(post_save, sender=Post)
def post_updated(sender, instance, created, **kwargs):
    if created:
        addIndex(instance.id)
    else:
        updateIndex(instance.id)

# 删除数据
@receiver(pre_delete, sender=Post)
def post_deleted(sender, instance, **kwargs):
    delIndex(instance.id)
