from django import forms
from .models import Davomat

class DavomatForm(forms.ModelForm):
    talaba_ism_familiya = forms.CharField(  # Yangi maydon qo‘shildi
        label='O‘quvchi (Ism Familiya)',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sana = forms.DateField(
        label='Sana',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    kelgan = forms.BooleanField(
        label='Kelganmi?',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Davomat
        fields = ['sana', 'kelgan']

    def save(self, commit=True):
        instance = super().save(commit=False)
        talaba_ism_familiya = self.cleaned_data['talaba_ism_familiya']
        ism_familiya = talaba_ism_familiya.split(' ', 1)
        if len(ism_familiya) == 2:
            ism, familiya = ism_familiya
        else:
            ism = talaba_ism_familiya
            familiya = ""

        from .models import Talaba  # Models import qilish
        talaba, created = Talaba.objects.get_or_create(
            ism=ism,
            defaults={'familiya': familiya}
        )
        instance.talaba = talaba
        if commit:
            instance.save()
        return instance

from django import forms
from .models import Homework, Talaba

class HomeworkForm(forms.ModelForm):
    talaba_ism_familiya = forms.CharField(  # O‘quvchining ism-familiyasini qo‘lda kiritish
        label='Student (First Last Name)',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sana = forms.DateField(
        label='Date',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    topshiriq = forms.CharField(
        label='Homework',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    bajarildi = forms.BooleanField(
        label='Completed?',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Homework
        fields = ['sana', 'topshiriq', 'bajarildi']  # `talaba` o‘rniga qo‘lda kiritilgan maydon ishlatiladi

    def save(self, commit=True):
        instance = super().save(commit=False)
        talaba_ism_familiya = self.cleaned_data['talaba_ism_familiya']
        ism_familiya = talaba_ism_familiya.split(' ', 1)
        if len(ism_familiya) == 2:
            ism, familiya = ism_familiya
        else:
            ism = talaba_ism_familiya
            familiya = ""

        from .models import Talaba
        talaba, created = Talaba.objects.get_or_create(
            ism=ism,
            defaults={'familiya': familiya}
        )
        instance.talaba = talaba
        if commit:
            instance.save()
        return instance