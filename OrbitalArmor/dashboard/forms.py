from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    class Meta:
        widgets = {
            'file' : forms.FileInput(attrs={'accept':'.pcap, .csv'})
        }
