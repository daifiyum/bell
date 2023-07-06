from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Category
from .models import Tag
from .models import Menu

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
admin.site.unregister(User)

# 定义关联对象的样式，StackedInline为纵向排列每一行，TabularInline为并排排列
class UserProfileInline(admin.StackedInline):
    model = UserProfile   # 关联的模型

# 关联字段在User之内编辑，关联进来
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]

# 重新注册User
admin.site.register(User, UserProfileAdmin)



class PostAdminForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Tags', False),
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(Post, PostAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'url', 'target', 'parent', 'order')
    list_editable = ('order',)
    list_filter = ('parent',)
    search_fields = ('title',)

admin.site.register(Menu, MenuAdmin)