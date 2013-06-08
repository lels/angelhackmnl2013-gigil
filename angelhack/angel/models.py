from django.db import models

class YearLevel(models.Model):
  YEAR_IN_SCHOOL = ((1,'Nursery'),(2,'Kinder 1'),(3,'Kinder 2'),(4,'Grade 1'),\
        (5,'Grade 1'),(6,'Grade 2'),(7,'Grade 3'),(8,'Grade 4'),(9,'Grade 5'),\
        (10,'Grade 6'),(11,'Freshman HS'),(12,'Sophomore HS'),(13,'Junior HS'),\
        (14,'Senior HS'),(15,'Freshman College'),(16,'Sophomore College'),\
        (17,'Junior College'),(18,'Senior College'));
  
  year_in_school = models.CharField(max_length=2,
                                    choices=YEAR_IN_SCHOOL,
                                    default=0);
                                    
class Student(models.Model):
  first_name = models.CharField(max_length=50);
  middle_name = models.CharField(max_length=50);
  last_name = models.CharField(max_length=50);
  date_of_birth = models.DateTimeField('date published');
  amount_needed = models.IntegerField(default=0);
  amount_received = models.IntegerField(default=0);
  ind_success = models.CharField(max_length=1,default='N');
  c_year_level = models.ForeignKey(YearLevel);
  last_upd_dt = models.DateTimeField('date published');
  
class SuccessStory(models.Model):
  title = models.CharField(max_length=50);
  text = models.CharField(max_length=4000);
  create_dt = models.DateTimeField('date published');

# Create your models here.
