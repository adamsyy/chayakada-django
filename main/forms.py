
from django.forms import ModelForm
from .models import Main,Todoform
class Todoform(ModelForm):
    class  Meta:
        model=Todoform
        fields=['id','price','title']