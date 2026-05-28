from django import forms

class ComentarioForm(forms.Form):
    curso = forms.CharField(label="curso:",max_length=500)
    comentario = forms.CharField(widget=forms.Textarea)