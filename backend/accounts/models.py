from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class CoustomUser(AbstractUser):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    ip_hash=models.GenericIPAddressField(editable=False,null=True,blank=True)

    def __str__(self):
        return str(self.ip_hash)




class Link(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    link=models.SlugField(unique=True,max_length=100,blank=True)
    user=models.OneToOneField(CoustomUser,on_delete=models.CASCADE)

    


class Reaction(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    link=models.ForeignKey(Link,on_delete=models.CASCADE,related_name='reaction_link')
    ip_hash=models.GenericIPAddressField(editable=False,null=True,blank=True)

    class Meta :
        unique_together = ('link', 'ip_hash')


class Comment(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    context=models.ForeignKey(Link,on_delete=models.CASCADE)
    ip_hash=models.GenericIPAddressField(editable=False,null=True,blank=True)
    link=models.ForeignKey(Link,on_delete=models.CASCADE,related_name='comment_link')

    

    
    