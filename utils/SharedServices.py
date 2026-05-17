def common_attrs(name, placeholder, className=None, maxLength=None):
    attrs = {
        'name': name,
        'placeholder': placeholder,
    }
    return {
        'class': 'form-control ' + (className if className else ''),
        'name': name,
        'placeholder': placeholder,
        'maxlength': maxLength if maxLength else '100'
    }