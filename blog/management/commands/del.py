from django.core.management.base import BaseCommand
from blog import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Post.objects.all().delete()
        models.Tag.objects.all().delete()
        models.Category.objects.all().delete()
        print('牛逼666，数据已清空')
    