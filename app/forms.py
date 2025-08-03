from django import forms


class StudentRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=10, min_length=10)

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        try:
            int(phone)  # 98asdf => not possible to convert to int
        except ValueError:
            raise forms.ValidationError("Phone number must be numeric")

        # check first two digits of phone number
        if phone[:2] not in ("98", "97"):
            raise forms.ValidationError("Phone number must start with 98 or 97")

        return phone
