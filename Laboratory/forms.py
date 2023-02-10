from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", max_length = 11, required = True)
    pwd = forms.CharField(label="Password", max_length = 12, required = True)

class SignUpForm(forms.Form):
    labname = forms.CharField(label='Lab Name',max_length = 20, required = True)
    password = forms.CharField(label='Password',max_length = 20, required = True)
    repassword = forms.CharField(label='Re-Enter Password',max_length = 20, required = True)
    place = forms.CharField(label='City/Town/Village',max_length = 20, required = True)
    phone = forms.CharField(label='PhoneNo',max_length = 20, required = True)
    email = forms.CharField(label='Email',max_length = 20, required = True)
    address = forms.CharField(label='Address',max_length = 100, required = True)
    
    
    