import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _
from .models import Blogs, Labels, Categorys, Contact


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "ly后台管理系统"
    site_footer = "个人网站"
    # menu_style = "accordion"


class BlogsAdmin(object):
    list_display = ['title', 'click_num', 'add_time']
    search_fields = ['title', 'click_num', 'add_time']
    list_filter = ['title', 'click_num', 'add_time']
    # model_icon = 'fas user-circle-o'
    style_fields = {"content": "ueditor"}


class LablesAdmin(object):
    list_display = ['lable', 'blog_lables']
    search_fields = ['lable', 'blog_lables']
    list_filter = ['lable', 'blog_lables']
    # <i class="fas fa-tags"></i>


class CategorysAdmin(object):
    list_display = ['mondel']
    search_fields = ['mondel']
    list_filter = ['mondel']
    # <i class="fas fa-glass-cheers"></i>

class ContactAdmin(object):
    list_display = ['pen_name', 'email']
    search_fields = ['pen_name', 'email']
    list_filter = ['pen_name', 'email']
    # fas fa-file-contract"></i>


xadmin.site.register(Blogs, BlogsAdmin)
xadmin.site.register(Labels, LablesAdmin)
xadmin.site.register(Categorys, CategorysAdmin)
xadmin.site.register(Contact, ContactAdmin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)