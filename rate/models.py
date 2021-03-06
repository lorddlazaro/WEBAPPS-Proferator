from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class Account(models.Model):
    email = models.CharField(max_length=200,unique=True)
    isVerified = models.BooleanField()
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

#for checking    
class Professor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    college = models.ForeignKey(College)
    department = models.ForeignKey(Department)
    # ratings = models.ForeignKey(Rating)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name


#for checking
class Class(models.Model):
    term = models.IntegerField()
    professor = models.ForeignKey(Professor)
    course = models.ForeignKey(Course)

#for checking
class Rating(models.Model):
    time = models.DateTimeField()
    account = models.ForeignKey(Account)
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(Professor)
    
class Factor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
#for checking
class FactorRating(models.Model):
    value = models.IntegerField()
    comment = models.CharField(max_length=500)
    factor = models.ForeignKey(Factor)
    rating = models.ForeignKey(Rating)
    class Meta:
        unique_together = ("rating", "factor") #unique together actually applies here
    
    def was_published_recently(self):
        return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'time'
    was_published_recently.boolean = True

#model for professor with number of rating
class ProfessorView(models.Model):
    name = models.ForeignKey(Professor)
    raters = models.IntegerField()

    def __str__(self):
        return self.name
