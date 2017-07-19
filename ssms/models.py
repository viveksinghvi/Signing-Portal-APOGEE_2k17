from __future__ import unicode_literals
from django.db import models
import os
from datetime import datetime,date
from django import forms
from django.contrib.auth.models import User
from ssms import venue
import uuid

from django.db import models
from django import forms
#from django.contrib.admin.widgets import AdminDateWidget



def content_album_name(instance, filename):
	return os.path.join(instance.name,filename)
def content_album_name2(instance, filename):
	return os.path.join(instance.gm_id.name,filename)
#######Use verbose name


class Grub_Coord(models.Model):
	stype=(('Active','Active'),('Inactive','Inactive'))
	user = models.OneToOneField(User)
	cg_id= models.UUIDField("Coordinator UUID",primary_key=True, default=uuid.uuid4, editable=False)
	cg_name = models.CharField("Coordinator Name",max_length=32,blank=False)
	cg_bitsid = models.CharField("Coordinator Bits ID",max_length=32, unique=True)
	assoc_name = models.CharField("Association",max_length=64, blank=False)
	status=models.CharField(choices=stype,max_length=32,default='Active')
	date = models.DateTimeField(auto_now=True)
	reg_by = models.CharField(max_length=32)
	def __str__(self):
		return self.cg_name


class Grub(models.Model):
	mtype=(('Veg','Veg'),('Non Veg','Non Veg'),('Both','Both'))
	stype=(('Active','Active'),('Inactive','Inactive'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	gm_id=  models.UUIDField("Grub UUID",primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField("Grub Name",max_length=32)
	meal= models.CharField("Meal Type",choices=mtype,max_length=16,default='Veg')
	cg_id= models.ForeignKey(Grub_Coord,verbose_name="Coordinator Id")
	reg_date = models.DateTimeField("Registration Date",default=datetime.now, blank=False)	
	date = models.DateField(default=datetime.now,blank=False)
	deadline = models.DateField(default=datetime.now,blank=False)
	deadline2 = models.DateField(default=datetime.now,blank=False)
	status=models.CharField(choices=stype,max_length=128,default='Active')
	excel = models.FileField(upload_to=content_album_name,blank=False)	
	mails=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	def __str__(self):
		return self.name



class Grub_Student(models.Model):
	unique_id = models.UUIDField("Unique Student Id",primary_key=True, default=uuid.uuid4, editable=False)
	stype=(('Signed Up','Signed Up'),('Opted Out','Opted Out'))  
	mtype=(('Veg','Veg'),('Non Veg','Non Veg'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	name = models.CharField(max_length=32)
	student_id= models.CharField("Bits Id",max_length=32,blank=False)
	user_id=models.CharField("Bits Email Id",db_index=True,max_length=32,blank=False)
	gm_id = models.ForeignKey(Grub,default='1',verbose_name="Grub Id")
	mail=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	meal= models.CharField("Mealtype Selected",choices=mtype,max_length=16,default='Veg',blank=False)
	status=models.CharField(choices=stype,max_length=128,blank=False)
	room=models.CharField("Room No.",max_length=32,default='303')
	bhawan=models.CharField("Bhawan",max_length=32,default='VK')
	class Meta:
		unique_together = ('student_id', 'gm_id','status') ##add meal
	def __str__(self):
                return self.student_id


class Wear(models.Model):
	mtype=(('T Shirt','T Shirt'),('Sweat Shirt','Sweat Shirt'))
	stype=(('Active','Active'),('Inactive','Inactive'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	gm_id=  models.UUIDField("Wear UUID",primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField("Wear Name",max_length=32)
	meal= models.CharField("Wear Type",choices=mtype,max_length=16,default='T Shirt')
	cg_id= models.ForeignKey(Grub_Coord,verbose_name="Coordinator Id")
	reg_date = models.DateTimeField("Final Submission Date",default=datetime.now, blank=False)	
	date = models.DateField(default=datetime.now,blank=False)
	deadline = models.DateField(default=datetime.now,blank=False)
	deadline2 = models.DateField(default=datetime.now,blank=False)
	status=models.CharField(choices=stype,max_length=128,default='Active')
	excel = models.FileField(upload_to=content_album_name,blank=False)	
	mails=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	price = models.IntegerField("Wear Price",default=0,null=False)
	image =  models.ImageField("Wear image",upload_to=content_album_name, blank=False)
	def __str__(self):
		return self.name



class Wear_Student(models.Model):
	unique_id = models.UUIDField("Unique Student Id",primary_key=True, default=uuid.uuid4, editable=False)
	stype=(('Signed Up','Signed Up'),('Opted Out','Opted Out'))  
	mtype=(('S','S'),('M','M'),('L','L'),('XL','XL'),('XXL','XXL'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	name = models.CharField(max_length=32)
	student_id= models.CharField("Bits Id",max_length=32,blank=False)
	user_id=models.CharField("Bits Email Id",db_index=True,max_length=32,blank=False)
	gm_id = models.ForeignKey(Wear,default='1',verbose_name="Wear Id")
	mail=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	meal= models.CharField("Size Selected",choices=mtype,max_length=16,default='S',blank=False)
	status=models.CharField(choices=stype,max_length=128,blank=False)
	room=models.CharField("Room No.",max_length=32,default='303')
	bhawan=models.CharField("Bhawan",max_length=32,default='VK')
	class Meta:
		unique_together = ('student_id', 'gm_id','status') ##add meal
	def __str__(self):
                return self.student_id

class Event(models.Model):
	mtype=(('Workshop','Workshop'),('Prof Shows','Prof Shows'))
	stype=(('Active','Active'),('Inactive','Inactive'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	gm_id=  models.UUIDField("Event UUID",primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField("Event Name",max_length=32)
	meal= models.CharField("Event Type",choices=mtype,max_length=16,default='Workshop')
	cg_id= models.ForeignKey(Grub_Coord,verbose_name="Coordinator Id")
	reg_date = models.DateTimeField("Registration Date",default=datetime.now, blank=False)	
	date = models.DateField(default=datetime.now,blank=False)
	deadline = models.DateField(default=datetime.now,blank=False)
	deadline2 = models.DateField(default=datetime.now,blank=False)
	status=models.CharField(choices=stype,max_length=128,default='Active')
	excel = models.FileField(upload_to=content_album_name,blank=False)	
	mails=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	price = models.IntegerField("Event Price",default=0,null=False)
	image =  models.ImageField("Event image",upload_to=content_album_name, blank=False)
	venue =  models.CharField("Event Venue",max_length=16,blank=False)
	def __str__(self):
		return self.name



class Event_Student(models.Model):
	unique_id = models.UUIDField("Unique Student Id",primary_key=True, default=uuid.uuid4, editable=False)
	stype=(('Signed Up','Signed Up'),('Opted Out','Opted Out'))  
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	mtype=(('Workshop','Workshop'),('Prof Shows','Prof Shows'))
	name = models.CharField(max_length=32)
	student_id= models.CharField("Bits Id",max_length=32,blank=False)
	user_id=models.CharField("Bits Email Id",db_index=True,max_length=32,blank=False)
	gm_id = models.ForeignKey(Event,default='1',verbose_name="Event Id")
	mail=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	meal= models.CharField("Size Selected",choices=mtype,max_length=16,default='Workshop',blank=False)
	status=models.CharField(choices=stype,max_length=128,blank=False)
	room=models.CharField("Room No.",max_length=32,default='303')
	bhawan=models.CharField("Bhawan",max_length=32,default='VK')
	class Meta:
		unique_together = ('student_id', 'gm_id','status') ##add meal
	def __str__(self):
                return self.student_id
                
class Student(models.Model):
	unique_id = models.UUIDField("Unique Stud Id",primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=32)
	bits_id= models.CharField("BITS ID",max_length=32,unique=True)
	bhawan = models.CharField(max_length=32)
	room_no = models.CharField("Room No.",max_length=4)
	user_id=models.CharField("Bits Email Id",db_index=True,max_length=32,blank=False)
	def __str__(self):
                return self.user_id
	
	
class Veg(models.Model):
	gm_id = models.ForeignKey(Grub,verbose_name="Grub Id")
	v_id=  models.UUIDField("Veg Grub ID",primary_key=True, default=uuid.uuid4, editable=False)
	v_venue = models.CharField("Veg Location",choices=venue.place,max_length=16,blank=False)
	v_price = models.IntegerField("Veg Price",default=0,null=False)
	v_images = models.ImageField("Veg Meal image",upload_to=content_album_name2, blank=False)
	def __str__(self):
                return self.gm_id.name
class NonVeg(models.Model):
	gm_id = models.ForeignKey(Grub,verbose_name="Grub Id")
	n_id=  models.UUIDField("Non Veg Grub ID",primary_key=True, default=uuid.uuid4, editable=False)
	n_venue = models.CharField("Non Veg Location",choices=venue.place,max_length=16,blank=False)
	n_price = models.IntegerField("Non Veg Price",default=0,null=False)
	n_images = models.ImageField("Non Veg Meal image",upload_to=content_album_name2, blank=False)	
	def __str__(self):
                return self.gm_id.name

class Both(models.Model):
	gm_id = models.ForeignKey(Grub,verbose_name="Grub Id")
	b_id=  models.UUIDField("Veg+Non Veg Grub Id",primary_key=True, default=uuid.uuid4, editable=False)
	veg_venue = models.CharField("Veg Location",choices=venue.place,max_length=16,blank=False)
	non_veg_venue = models.CharField("Non Veg Location",choices=venue.place,max_length=16,blank=False)
	veg_price = models.IntegerField("Veg Price",default=0,null=False)
	non_veg_price = models.IntegerField("Non Veg price",default=0,null=False)
	veg_images = models.ImageField("Veg Meal Image",upload_to=content_album_name2, blank=False)
	non_veg_images = models.ImageField("Non Veg Image",upload_to=content_album_name2, blank=False)	
	def __str__(self):
                return self.gm_id.name

class DateMailStatus(models.Model):
	date = models.DateField(default=datetime.now,blank=False)
	mails = models.IntegerField("Mails Sent",default = 0)
	def __str__(self):
		return self.date.strftime('%m/%d/%Y')

