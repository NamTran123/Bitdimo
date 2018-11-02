from django.db import models
from  django.contrib.auth.models  import  User 

class SubperUser(models.Model):
    '''
    #Table user   // vì chưa biết xử lí thế nào với nó
    #  
    '''
    GENDER=(
        ('F' ,"Fimale" ),
        ('M' , 'Male')
    )
    STATUS = (
        ('act','active'),
        ('uact', 'unactive')
    )
    Username  = models.CharField(max_length = 50 ,null =False)
    Password  = models.CharField(max_length = 20  , null  = False)
    Email  = models.EmailField()
    Gender = models.CharField(max_length = 1  ,choices=GENDER, default='F')
    Birthdate =  models.DateField() 
    Status  = models.CharField(max_length = 4 ,choices=STATUS, default='uact')
    def  __str__ (self):
        return  "{}-{}-{}-{}-{}".format(self.Username , self.Email, self.Gender, self.Birthdate, self.Status) 

class Province(models.Model):
    '''
    #Table  province (Tỉnh)
    '''
    Province_name =  models.CharField(max_length = 300)

class Area(models.Model):
    '''
    #Table  Area ( Khu vực )
    '''

    Province = models.OneToOneField(Province , on_delete=models.CASCADE)
    Name_area  =  models.CharField(max_length = 200)

class Type_of_post(models.Model):
    '''
    #Table type  of post   
    '''
    Name =  models.CharField(max_length=  50)
    def  __str__ (self):
        return  "{}".format(self.Name )

class Landscapes(models.Model):
    '''
    #Table  evaluate (Danh thắng )  : Name  of beautiful evaluate
    '''
    Name_landscapes =  models.CharField(max_length = 150)
    Path = models.CharField(max_length = 300)
    Longtitude  = models.CharField(max_length = 200)
    Latitude  = models.CharField(max_length =  200)
    Area =  models.OneToOneField(Area , on_delete=models.PROTECT)

    def  __str__ (self):
        return  "{}-{}-{}".format(self.Name_landscapes , self.Path, self.Area)


class Post(models.Model):
    '''
    #Table post  of user
    '''
    Landscapes   = models.OneToOneField(Landscapes , on_delete=models.CASCADE)
    Type_of_post =   models.ForeignKey(Type_of_post, on_delete=models.CASCADE)
    User = models.ForeignKey(User , on_delete=models.CASCADE) 
    Number_of_images =  models.IntegerField()
    Number_of_comment = models.IntegerField()
    Average_rating = models.FloatField()
    def  __str__ (self):
        return  "{}-{}-{}-{}".format(self.Landscapes , self.Type_of_post, self.User, self.Average_rating) 

class Comment(models.Model):
    '''
    #Table comment  of post  
    '''
    Post =models.OneToOneField(Post , on_delete=models.CASCADE)
    User =models.OneToOneField(User , on_delete=models.CASCADE)
    Content  =  models.TextField(max_length=1000)
    Time_comment =  models.DateTimeField()

    def  __str__ (self):
        return  "{}-{}-{}-{}".format(self.Post , self.User, self.Content, self.Time_comment)

class Type_of_image(models.Model):
    '''
    #Table type  of image   
    '''
    Name = models.CharField(max_length =200)
    def  __str__ (self):
        return  "{}".format(self.Name )

class Image(models.Model):
    '''
    #Table images of  post   
    '''
    URL  = models.CharField(max_length = 300 , null  = False)
    Post =models.OneToOneField(Post , on_delete=models.CASCADE) 
    User =models.OneToOneField(User , on_delete=models.CASCADE) 
    Type_of_image = models.ForeignKey(Type_of_image , on_delete=models.CASCADE) 
    def  __str__ (self):
        return  "{}-{}-{}".format(self.URL , self.Post, self.User)

class Evaluate(models.Model):
    '''
    #Table  evaluate ( Đánh giá )
    '''
    Post =models.OneToOneField(Post , on_delete=models.CASCADE)
    Value = models.IntegerField() 
    def  __str__ (self):
        return  "{}-{}".format(self.Post , self.Value)







