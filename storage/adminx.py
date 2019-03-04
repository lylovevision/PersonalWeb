import xadmin
from .models import Storage, CommonTools


class StorageAdmin(object):
    list_display = ['degree', 'add_time', 'url_path']
    search_fields = ['degree', 'add_time', 'url_path']
    list_filter = ['degree', 'add_time', 'url_path']
    # <i class="fas fa-archive"></i>

class CommonToolsAdmin(object):
    list_display = ['name', 'url_path']
    search_fields = ['name', 'url_path']
    list_filter = ['name', 'url_path']
    # <i class="fas fa-tools"></i>


xadmin.site.register(Storage, StorageAdmin)
xadmin.site.register(CommonTools, CommonToolsAdmin)