from django.contrib.auth.forms import UserCreationForm
from .models import Custom_User_Model

class Custom_User_Form(UserCreationForm):
    class Meta(UserCreationForm):
        model = Custom_User_Model
        fields = UserCreationForm.Meta.fields + ('age', 'address')