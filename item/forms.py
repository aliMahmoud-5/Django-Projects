from django import forms
from .models import item, category


class add(forms.ModelForm):

     class Meta:
        
        model = item
        fields = ('categ','name','price','description','img')

        categ = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder':'category'}))
        name = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder':'name'}))
        description = forms.Textarea(attrs ={ 'placeholder':'name'})
        price = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder':'price'}))
        


class edit(forms.ModelForm):
    
    
    class Meta:

        model = item
        fields = ('name','price','description','img','sold')