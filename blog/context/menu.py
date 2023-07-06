from blog import models

def menu_processor(request):
    menus = models.Menu.objects.filter(parent=None)
    return {'menus': menus}