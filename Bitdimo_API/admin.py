from django.contrib import admin
from .models import SubperUser ,Province ,Area ,Type_of_post ,Landscapes,Post,Comment ,Type_of_image,Image,Evaluate
# Register your models here.
admin.site.register(SubperUser) 
admin.site.register(Province)
admin.site.register(Area) 
admin.site.register(Type_of_post)
admin.site.register(Landscapes) 
admin.site.register(Post)
admin.site.register(Comment) 
admin.site.register(Type_of_image)
admin.site.register(Image) 
admin.site.register(Evaluate)