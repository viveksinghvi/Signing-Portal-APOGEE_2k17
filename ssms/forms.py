from django import forms
from ssms.models import Grub,Grub_Coord,Grub_Student,Veg,NonVeg,Both,Wear,Event,Wear_Student,Event_Student
from django.contrib.auth.models import User
from django.contrib.admin import widgets 
class Grub_CoordUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	
	def clean_username(self):
		users = self.cleaned_data["username"]
		if User.objects.filter(username=users).count() > 0:
        		raise forms.ValidationError("This username already exists.")
		return users
	def clean(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
    		if password and password != confirm_password:
        		raise forms.ValidationError("Passwords don't match.")
	
    		return self.cleaned_data
	class Meta:
	        model = User
	        fields = ('username','password','confirm_password')
class Grub_CoordUserProfileForm(forms.ModelForm):
	def clean(self):
		cgbid = self.cleaned_data.get('cg_bitsid')
		if cgbid and len(str(cgbid))!=12:
			raise forms.ValidationError("Enter a valid BITS ID")
		return self.cleaned_data
	class Meta:
		model = Grub_Coord
		fields = ('cg_name', 'cg_bitsid','assoc_name')


class GrubForm(forms.ModelForm):
	#date=forms.DateField(help_text="Format: YYYY-MM-DD")
	class Meta:
	        model = Grub
	        fields = ('name',)
		
class NonVegForm(forms.ModelForm):
	class Meta:
	        model = NonVeg
	        fields = ('n_images','n_price','n_venue')
class VegForm(forms.ModelForm):
	class Meta:
	        model = Veg
	        fields = ('v_images','v_price','v_venue')
class BothForm(forms.ModelForm):
	class Meta:
	        model = Both
	        fields = ('veg_images','non_veg_images','veg_price','non_veg_price','veg_venue','non_veg_venue')


class CoordStudentRegForm(forms.ModelForm):
	class Meta:
	        model = Grub_Student
		fields = ('student_id',)

class ExcelUpload(forms.ModelForm):
	"""def clean(self):	
		files = self.cleaned_data['excel']
		if files:
            		filename = files.name
            		print filename
            		if filename.endswith('.xls') or filename.endswith('.xlsx') or filename.endswith('.csv'):
                		return files
           		else:
                		raise forms.ValidationError("Unsupported File type.")

        	return files"""
	class Meta:
	        model = Grub
	        fields = ('excel',)
class ExcelUpload2(forms.ModelForm):
	"""def clean(self):	
		files = self.cleaned_data['excel']
		if files:
            		filename = files.name
            		print filename
            		if filename.endswith('.xls') or filename.endswith('.xlsx') or filename.endswith('.csv'):
                		return files
           		else:
                		raise forms.ValidationError("Unsupported File type.")

        	return files"""
	class Meta:
	        model = Wear
	        fields = ('excel',)
class ExcelUpload3(forms.ModelForm):
	"""def clean(self):	
		files = self.cleaned_data['excel']
		if files:
            		filename = files.name
            		print filename
            		if filename.endswith('.xls') or filename.endswith('.xlsx') or filename.endswith('.csv'):
                		return files
           		else:
                		raise forms.ValidationError("Unsupported File type.")

        	return files"""
	class Meta:
	        model = Event
	        fields = ('excel',)


class GrubFormEdit(forms.ModelForm):
	class Meta:
	        model = Grub
	        fields = ('name',)

class WearFormEdit(forms.ModelForm):
	class Meta:
	        model = Wear
	        fields = ('name',)

class EventFormEdit(forms.ModelForm):
	class Meta:
	        model = Event
	        fields = ('name',)    
class UploadFileForm(forms.Form):
	file = forms.FileField()
	def clean(self):
		files = self.cleaned_data.get("file")
		if files:
            		filename = files.name
            		if filename.endswith('.xls') or filename.endswith('.xlsx') or filename.endswith('.csv'):
                		return files
           		else:
                		raise forms.ValidationError("Unsupported File type.")

        	return files
		
	class meta:
		('file',)
		
class WearForm(forms.ModelForm):
	#date=forms.DateField(help_text="Format: YYYY-MM-DD")
	class Meta:
	        model = Wear
	        fields = ('name','meal','price','image')

class EventForm(forms.ModelForm):
	#date=forms.DateField(help_text="Format: YYYY-MM-DD")
	class Meta:
	        model = Event
	        fields = ('name','meal','venue','price','image')


