from django import forms
from catalog.models import Product, Version

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_current':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['owner']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово "{word}" в наименовании продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово "{word}" в описании продукта')
        return cleaned_data


class ProductModeratorForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'description', 'is_published']

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово "{word}" в описании продукта')
        return cleaned_data


class VersionForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

