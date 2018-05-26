from django import forms
from datetime import date
import json

#our new entry form
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'this is how my colleagues calls me...'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'and this is how my professors call me...'}))
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'placeholder': 'no spam deals, please...'}))
    date_of_birth = forms.DateField(widget = forms.SelectDateWidget(years=range(1980, 2021)))
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Please no good mornings and no good nights... I\'m sick of them...'}))
    location = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={'placeholder': 'and you can find me here...'}))

    #i dunno what this is
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        date_of_birth = cleaned_data.get('date_of_birth')
        mobile = cleaned_data.get('mobile')
        location = cleaned_data.get('location')

        #if the form is completely empty
        if not first_name and not last_name and not email and not mobile and not location:
            raise forms.ValidationError('You have to write something!')
        else:
            #calculating age from the date of birth
            #i thought its useless or rathe a nor techy way to ask for age as we were gonna ask for the date of birth anyway
            age  = date.today()
            age = age.year - date_of_birth.year - ((age.month, age.day) < (date_of_birth.month, date_of_birth.day))


            #with open('q.txt','a') as data:
            #    data.write(',\n{')
            #    data.write('"first_name": "'+first_name +'",\n')
            #    data.write('"last_name":"'+last_name +'",\n')
            #    data.write('"email":"'+email +'",\n')
            #    date_of_birth = str(date_of_birth)
            #    data.write('"date_of_birth":"'+ date_of_birth+'",\n')
            #    mobile = str(mobile)
            #    data.write('"mobile":"'+mobile +'",\n')
            #    age = str(age)
            #    data.write('"age":"'+ age+'",\n')
            #    data.write('"location":"'+location +'",\n')
            #    data.write('}')



            #data to write in json file so that it can get reflected in Jquery Datatable
            mobile = str(mobile) #cnverting integer to be written in json
            date_of_birth = str(date_of_birth) # same here too but dataTimme field

            #form details casted into dictionary to be saved in json file
            data = {"first_name":first_name,"last_name":last_name,"email":email,"dob":date_of_birth,"mobile":mobile,"age":age,"location":location}

            # to save the forms data into the json file to be refleccted in the Jquery Datatable
            with open('data.json','r') as f:
               file = json.load(f)
               file["data"].append(data)
            with open ('data.json','w') as f:
               json.dump(file,f)

