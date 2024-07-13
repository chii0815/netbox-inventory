from django import forms

from .models import AssetForm


__all__ = (
    'AssetBulkAddForm',
    'AssetBulkAddModelForm',
)


class AssetBulkAddForm(forms.Form):
    """ Form for creating multiple Assets by count """
    asset_tags = forms.CharField(
        widget=forms.Textarea
    )
    create_serial_from_asset = forms.BooleanField(
        required=False,
        label="Serial Number = Asset Tag?"
    )
    create_name_from_asset = forms.BooleanField(
        required=False,
        label="Name = Asset Tag?"
    )


class AssetBulkAddModelForm(AssetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset_tag'].disabled = True
        self.fields['serial'].disabled = True
        self.fields['name'].disabled = True
