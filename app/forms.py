from django import forms

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=123)
    Sid= forms.IntegerField()
    Semail = forms.EmailField()