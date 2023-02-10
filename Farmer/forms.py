from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", max_length = 11, required = True)
    pwd = forms.CharField(label="Password", max_length = 12, required = True)

class SignUpForm(forms.Form):
    fname = forms.CharField(label = "First Name", max_length = 20, required = True)
    lname = forms.CharField(label = "Last Name/Surname", max_length = 20, required = True)
    phoneno = forms.CharField(label = "Phone number", max_length = 10, required = True)
    password = forms.CharField(label = "Password", max_length = 20, required = True)
    repassword = forms.CharField(label = "Re-enter password", max_length = 20, required = True)
    address = forms.CharField(label = "Address", max_length = 100, required = True)
    place = forms.CharField(label = "City/Town/Village", max_length = 25, required = True)

class LabBookForm(forms.Form):
    labid = forms.CharField(label="Lab Id",max_length = 10)
    uid = forms.CharField(label="Your ID", max_length = 11)

class SellerRegForm(forms.Form):
    uname = forms.CharField(label="User Name",max_length=20)
    products = forms.CharField(label = "Products you sell",max_length=60)


    
    