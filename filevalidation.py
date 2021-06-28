''' validation of file in the form '''

def clean_file(self):
    file = self.cleaned_data['file']
    if file.size > 25000000:
        raise ValidationError('The file is too big')
    return file