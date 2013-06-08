from django.db import models;
from datetime import datetime;

class Gender(models.Model):
  GENDER = (('M', 'Male'),('F','Female'));
  gender = models.CharField(max_length=1,choices=GENDER,default='M');
  
  def get_desc(self):
    return dict(self.GENDER)[self.gender];
  
class YesNo(models.Model):
  YES_NO = (('Y', 'Yes'),('N','No'));
  yes_no = models.CharField(max_length=1,choices=YES_NO,default='Y');
  
  def get_desc(self):
    return dict(self.YES_NO)[self.yes_no];
  
class YearLevel(models.Model):
  YEAR_IN_SCHOOL = (('1','Nursery'),('2','Kinder 1'),('3','Kinder 2'),\
        ('4','Grade 1'),('5','Grade 2'),('6','Grade 3'),\
        ('7','Grade 4'),('8','Grade 5'),('9','Grade 6'),('10','Freshman HS'),\
        ('11','Sophomore HS'),('11','Junior HS'),('13','Senior HS'),\
        ('14','Freshman College'),('15','Sophomore College'),\
        ('16','Junior College'),('17','Senior College'));
  
  year_in_school = models.CharField(max_length=2,choices=YEAR_IN_SCHOOL,\
                                    default=0);
  
  def get_desc(self):
    return dict(self.YEAR_IN_SCHOOL)[self.year_in_school];

class Story(models.Model):
  title = models.CharField(max_length=50);
  text = models.CharField(max_length=4000);
  create_dt = models.DateTimeField(auto_now_add=True);
  last_upd_dt = models.DateTimeField(auto_now=True);

class Student(models.Model):
  first_name = models.CharField(max_length=50);
  middle_name = models.CharField(max_length=50);
  last_name = models.CharField(max_length=50);
  date_of_birth = models.DateField();
  gender = models.ForeignKey(Gender);
  image = models.ImageField(max_length=255, upload_to='media', null=True);
  amount_needed = models.DecimalField(default=0.0,max_digits=9, \
                                      decimal_places=2);
  story = models.ForeignKey(Story);
  c_year_level = models.ForeignKey(YearLevel);
  last_upd_dt = models.DateTimeField(auto_now=True);
  
  #This function returns the number of benefactors that has helped the given
  #scholar
  def num_benefactors(self):
    return Donation.objects.filter(student=self).count();
  
  #This function returns the amount recieved by a student
  def amount_received(self):
    return Donation.objects.filter(student=self) \
           .aggregate(models.Sum('amount'))['amount__sum'];
  
  def get_received_percent(self):
    print "a", self.amount_received();
    print "b", self.amount_needed;
    return "%.0f" % (self.amount_received() * 100 / self.amount_needed);

class Donator(models.Model):
  username = models.CharField(max_length=32);
  password = models.CharField(max_length=32);
  first_name = models.CharField(max_length=50);
  middle_name = models.CharField(max_length=50);
  last_name = models.CharField(max_length=50);
  last_login_dt = models.DateTimeField();
  last_upd_dt = models.DateTimeField(auto_now=True);
  
  #This function returns the number of scholars helped by the given benefactor
  def num_scholars(self):
    return Donation.objects.filter(donator=self).count();
    
  #This function returns the total amount given by the given benefactor
  def amount_given(self):
    return Donation.objects.filter(donator=self) \
           .aggregate(models.Sum('amount'))['amount__sum'];

class Donation(models.Model):
  student = models.ForeignKey(Student);
  donator = models.ForeignKey(Donator);
  amount = models.DecimalField(default=0.0,max_digits=9,decimal_places=2);
  
# Create your models here.
