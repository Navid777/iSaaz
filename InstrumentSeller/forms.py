from django import forms

class ad_form(forms.Form):
    title = forms.CharField()
    details = forms.CharField()
    model = forms.CharField()
    manufacturer = forms.CharField()
    transport= forms.CharField()
    returning = forms.CharField()
    purchase = forms.CharField()
    price = forms.IntegerField()
    year = forms.ChoiceField(choices=[(x, x) for x in range(1370, 1393)], required=False)
    USED = (
        ('used', 'دست دو'),
        ('new', 'جدید')
    )
    used = forms.ChoiceField(choices=USED, required=True, label='Example')
    sound = forms.FileField(required=False)
    img1 = forms.FileField()
    img2 = forms.FileField(required=False)
    img3 = forms.FileField(required=False)
    img4 = forms.FileField(required=False)
    img5 = forms.FileField(required=False)
    img6 = forms.FileField(required=False)

