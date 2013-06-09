from django.db import models;
from datetime import datetime;

class Gender(models.Model):
  GENDER = (('M', 'Male'),('F','Female'),('N','Male/Female'));
  gender = models.CharField(max_length=1,choices=GENDER,default='M');
  
  def get_desc(self):
    return dict(self.GENDER)[self.gender];
    
  def __str__(self):
    return self.get_desc();
  
class YesNo(models.Model):
  YES_NO = (('Y', 'Yes'),('N','No'));
  yes_no = models.CharField(max_length=1,choices=YES_NO,default='Y');
  
  def get_desc(self):
    return dict(self.YES_NO)[self.yes_no];
    
  def __str__(self):
    return self.get_desc();

class NeedItem(models.Model):
  NEED = (('book', 'Books'),('food','Food Allowance'), \
            ('pencil','Pencils'),('notebook','Notebooks'));
  need = models.CharField(max_length=50,choices=NEED);
  
  def get_desc(self):
    return dict(self.NEED)[self.need];
    
  def __str__(self):
    return self.get_desc();

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
    
  def __str__(self):
    return self.get_desc();

class Story(models.Model):
  title = models.CharField(max_length=50);
  pitch = models.CharField(max_length=1000);
  text = models.CharField(max_length=4000);
  need_statement = models.CharField(max_length=1000);
  create_dt = models.DateTimeField(auto_now_add=True);
  last_upd_dt = models.DateTimeField(auto_now=True);

class Student(models.Model):
  first_name = models.CharField(max_length=50);
  middle_name = models.CharField(max_length=50);
  last_name = models.CharField(max_length=50);
  date_of_birth = models.DateField(null=True,blank=True);
  gender = models.ForeignKey(Gender);
  image = models.ImageField(max_length=255, upload_to='media', null=True);
  amount_needed = models.DecimalField(default=0.0,max_digits=9, \
                                      decimal_places=2);
  story = models.ForeignKey(Story);
  c_year_level = models.ForeignKey(YearLevel);
  need_items = models.ManyToManyField(NeedItem);
  code = models.CharField(max_length=10);
  last_upd_dt = models.DateTimeField(auto_now=True);
  
  #This function returns the number of benefactors that has helped the given
  #scholar
  def num_benefactors(self):
    return Donation.objects.filter(student=self).count();
  
  #This function returns the amount recieved by a student
  def amount_received(self):
    q = Donation.objects.filter(student=self)
    if q.count() > 0:
      return q.aggregate(models.Sum('amount'))['amount__sum'];
    return 0
  
  def get_received_percent(self):
    if self.amount_needed == 0:
      self.amount_needed = 1;
      
    percentage = (self.amount_received() * 100 / self.amount_needed);
    return "%.0f" % percentage;
    
  def __str__(self):
    return self.last_name + ", " + self.first_name + " " + self.middle_name;

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
           
  def __str__(self):
    return self.last_name + ", " + self.first_name + " " + self.middle_name;

class Donation(models.Model):
  student = models.ForeignKey(Student);
  donator = models.ForeignKey(Donator);
  amount = models.DecimalField(default=0.0,max_digits=9,decimal_places=2);
           
  def __str__(self):
    return str(self.donator) + " to " + str(self.student) + ": " + str(self.amount);
  
# Create your models here.
