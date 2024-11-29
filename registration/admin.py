from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Custom_User_Form
from .models import Custom_User_Model

class Custom_User_Admin(UserAdmin):
    add_form = Custom_User_Form
    model = Custom_User_Model
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'address', 'is_staff']

admin.site.register(Custom_User_Model, Custom_User_Admin)
