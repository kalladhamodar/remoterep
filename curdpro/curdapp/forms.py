from django import forms
class insertingdata(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    Address = forms.CharField(
        label="Enter your address",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your address'
            }
        )
    )
    Constituecy = forms.CharField(
        label="Enter your constituency",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your constituency'
            }
        )
    )
    District = forms.CharField(
        label="Enter your District",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your District'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile no",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile no'
            }
        )
    )
    state = forms.CharField(
        label="Enter your state",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your state'
            }
        )
    )
class updatingdata(forms.Form):
    name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your mobile no",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile no'
            }
        )
    )



class deletingdata(forms.Form):
    name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }
        )
    )



