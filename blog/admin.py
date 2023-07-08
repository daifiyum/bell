from django.contrib import admin
from django import forms

from .models import Post
from .models import Category
from .models import Tag
from .models import Menu

# 注册
admin.site.register(Category)
admin.site.register(Tag)


# 文章定制
class PostAdminForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Tags', False),
        required=False
    )
    
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Categories', False),
        required=False
    )
    
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)



# 菜单定制
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'url', 'target', 'parent', 'order')
    list_editable = ('order',)
    list_filter = ('parent',)
    search_fields = ('title',)

admin.site.register(Menu, MenuAdmin)