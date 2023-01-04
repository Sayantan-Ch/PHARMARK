from django.db import models
import string 
import random
import simplejson as json
from picklefield.fields import PickledObjectField

def generate_unique_code():
    length = 5

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Drug.objects.filter(suggestionCode=code).count() == 0:
            break

    return code

# Create your models here.
class Drug(models.Model):
    suggestionCode=models.CharField(max_length=5,default=generate_unique_code,unique=True)
    drugCode=models.CharField(max_length=5,default="",unique=True)
    Approved=models.BooleanField(null=False,default=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    names = models.TextField(null=True)
    