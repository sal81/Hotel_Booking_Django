from django import forms

class AvailabilityForms(forms.Form):
    CATEGORIES =(
       ('isAC', 'AC'),
       ('notAC', 'NON-AC'),
       ('delux', 'DELUX'),
       ('single', 'SINGLE'),
       ('double', 'DOUBLE'),
   ) 
    room_category = forms.ChoiceField(choices=CATEGORIES, required = "True")
    check_in = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],required = True,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    check_out = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],required = True,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
        )