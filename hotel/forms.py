from django import forms

#if  room is available book straight away,otherwise redirect to other section

class AvailabilityForm(forms.Form):
    #we need room category,check in and check out
    Room_Categories=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    
    room_category=forms.ChoiceField(choices=Room_Categories, required=True)
    check_in=forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M" ,])
    check_out=forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M" ,])