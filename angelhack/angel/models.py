from django.db import models
from datetime import datetime;

class Gender(models.Model):
  GENDER = (('M', 'Male'),('F','Female'));
  gender = models.CharField(max_length=1,choices=GENDER,default='M');
  
class YesNo(models.Model):
  YES_NO = (('Y', 'Yes'),('N','No'));
  yes_no = models.CharField(max_length=1,choices=YES_NO,default='Y');
  
class YearLevel(models.Model):
  YEAR_IN_SCHOOL = (('1','Nursery'),('2','Kinder 1'),('3','Kinder 2'),\
        ('4','Grade 1'),('5','Grade 1'),('6','Grade 2'),('7','Grade 3'),\
        ('8','Grade 4'),('9','Grade 5'),('10','Grade 6'),('11','Freshman HS'),\
        ('12','Sophomore HS'),('13','Junior HS'),('14','Senior HS'),\
        ('15','Freshman College'),('16','Sophomore College'),\
        ('17','Junior College'),('18','Senior College'));
  
  year_in_school = models.CharField(max_length=2,choices=YEAR_IN_SCHOOL,\
                                    default=0);

class Student(models.Model):
  first_name = models.CharField(max_length=50);
  middle_name = models.CharField(max_length=50);
  last_name = models.CharField(max_length=50);
  date_of_birth = models.DateField();
  gender = models.ForeignKey(Gender);
  amount_needed = models.IntegerField(default=0);
  amount_received = models.IntegerField(default=0);
  ind_success = models.CharField(max_length=1,default='N');
  c_year_level = models.ForeignKey(YearLevel);
  last_upd_dt = models.DateTimeField(auto_now=True);

class SuccessStory(models.Model):
  student = models.ForeignKey(Student);
  title = models.CharField(max_length=50);
  text = models.CharField(max_length=4000);
  create_dt = models.DateTimeField(auto_now_add=True);
  last_upd_dt = models.DateTimeField(auto_now=True);

class User(models.Model):
  username = models.CharField(max_length=32);
  password = models.CharField(max_length=32);
  first_name = models.CharField(max_length=50);
  middle_name = models.CharField(max_length=50);
  last_name = models.CharField(max_length=50);
  last_login_dt = models.DateTimeField();
  last_upd_dt = models.DateTimeField(auto_now=True);

# Create your models here.
