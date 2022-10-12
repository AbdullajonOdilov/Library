from django import forms
from django.core.exceptions import ValidationError
from .models import *


class StudentForm(forms.Form):
    i = forms.CharField(label="Ism")
    bitiruvchi = forms.BooleanField()
    kitoblari_soni = forms.IntegerField()

    def clean_i(self):
        qiymat = self.cleaned_data.get('i')
        if not qiymat.endswith('jon') and not qiymat.endswith('bek'):
            raise ValidationError("Ism o'zbekcha emas!")
        return qiymat

    def clean_kitoblari_soni(self):
        res = self.cleaned_data.get('kitoblari_soni')
        if res< 0 or res >= 5:
            raise ValidationError("Talaba 5 tagacha kitob o'qigan ")
        return res
class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ('nom','sahifa','janr','muallif')
class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = ('ism','tirik','kitob_soni','t_y')
    # ism = forms.CharField(label="Ism")
    # tirik = forms.BooleanField()


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('student','kitob','qaytardi','qaytargan_sana')



