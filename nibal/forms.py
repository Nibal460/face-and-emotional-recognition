from socket import fromshare
from django import forms
from nibal.models import face

class faceform(forms.ModelForm):
    class Meta:
        model = face
        fields = ['image']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control'})