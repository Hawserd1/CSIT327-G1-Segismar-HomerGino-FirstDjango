from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Select
from .models import CustomUser


def _add_bootstrap_classes(form):
    for field in form.fields.values():
        css_class = 'form-select' if isinstance(field.widget, Select) else 'form-control'
        field.widget.attrs['class'] = f"{field.widget.attrs.get('class', '')} {css_class}".strip()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'first_name', 'last_name', 'role', 'course')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _add_bootstrap_classes(self)


class UserProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'course')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _add_bootstrap_classes(self)