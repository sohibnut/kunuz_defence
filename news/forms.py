from django.forms import ModelForm
from .models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        # fields = ['name', 'tel_number', 'theme', 'text']
        fields = '__all__'