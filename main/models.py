from django.db import models

class Sldier(models.Model):
    image = models.ImageField(upload_to="Slider/")
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title

class AboutProject(models.Model):
    image1 = models.ImageField(upload_to="AboutProject")
    image2= models.ImageField(upload_to="AboutProject")
    
class Direction(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Direction/")
    
class AboutProject2(models.Model):
    image1 = models.ImageField(upload_to="AboutProject2")
    image2= models.ImageField(upload_to="AboutProject2")

class Zadacha(models.Model):
    text = models.CharField(max_length=100)
    number = models.IntegerField()



class Result(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Result/", blank=True, null=True)

class AboutUs(models.Model):
    site = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=500)

class Link(models.Model):
    instagram = models.CharField(max_length=400)
    telegram = models.CharField(max_length=400)
    youtube = models.CharField(max_length=400)
    facebook = models.CharField(max_length=400)

class Question(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.answer


class Registration(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    born = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    answer = models.ManyToManyField(Answer, blank=True)
    def __str__(self):
        return self.name

class Pismo(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()

class Logo(models.Model):
    image = models.ImageField(upload_to="Logo/")
    