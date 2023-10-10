from django import forms
Genders=[('male','Male'),('female','Female'),('others','Others')]
class WorkerRegistration(forms.Form):
    First_Name=forms.CharField(widget=forms.TextInput(attrs={'class':'name','id':'Fname','placeholder':'Enter First Name'}),max_length=40)
    Middle_Name=forms.CharField(max_length=40,required=False,widget=forms.TextInput(attrs={'class':'name','id':'Mname','placeholder':'Enter Middle Name'}))
    Last_Name=forms.CharField(max_length=40,required=False,widget=forms.TextInput(attrs={'class':'name','id':'Fname','placeholder':'Enter Last Name'}))
    Mobile_Number=forms.CharField(max_length=14,widget=forms.TextInput(attrs={'id':'MNo','placeholder':'Enter Mobile Number'}))
    # Gender=forms.CharField(widget=forms.RadioSelect(choices=Genders,attrs={'id':'Gender'}))
    Gender=forms.CharField(widget=forms.Select(choices=Genders,attrs={'id':'Gender'}))
    Age=forms.IntegerField(widget=forms.NumberInput(attrs={'id':'age','placeholder':'Enter Age'}))
    Address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'id':'Add','placeholder':'Enter Address','rows':5,'cols':20}))
    Pin=forms.IntegerField(widget=forms.NumberInput(attrs={'id':'Pin','placeholder':'Enter Area Pin'}))
 
class SearchWorkers(forms.Form):
    Area_Pin=forms.IntegerField(widget=forms.NumberInput(attrs={'id':'Pin','placeholder':'Enter Area Pin'}))
    
