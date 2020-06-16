from django.db import models

# Create your models here.
class login(models.Model):
    college_id = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
class Student2(models.Model): 
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField('Course')

class Course(models.Model):
    # Yoga, Spanish, French, etc.
    name = models.CharField(max_length=30)

class Score(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(max_length=4)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

class student(models.Model):
    lib= models.CharField(max_length=50 ,null=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    section=models.CharField(max_length=2)
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null= True)
    def __str__(self):
        return self.name

class mark(models.Model):
    maths = models.IntegerField()
    chemisty= models.IntegerField()
    c_programming=models.IntegerField()
    english=models.IntegerField()
    
    
    
class teacher(models.Model):
    lib=models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100)
    father_name= models.CharField(max_length=200)
    email=models.EmailField( max_length=254)
    branch = models.CharField(max_length=50)
    section=models.CharField(max_length=2)
    contact=models.IntegerField()
    Dob=models.DateField(auto_now=False)
    address=models.TextField(max_length=1000)
    status=models.CharField(default="active", max_length=50)
    def __str__(self):
        return self.name

class querytb(models.Model):
    lib=models.CharField(max_length=50,null=True)
    query= models.TextField(null=False ,max_length=500)
    status=models.CharField(max_length=50)
    datetime=models.DateTimeField(auto_now_add=True, null= True)
