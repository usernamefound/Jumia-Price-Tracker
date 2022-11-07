from django.contrib.auth.forms import UserCreationForm
from links.models import CustomUser


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')
        labels = {
            'username': 'Username',
            'email': 'Email Address'
        }