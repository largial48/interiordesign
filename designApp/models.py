from django.db import models
from django.utils.timezone import now

class item(models.Model):
    id = models.AutoField
    item_name = models.CharField(max_length=50)
    item_category = models.CharField(max_length=150,blank=True)
    item_desc = models.CharField(max_length=500,default="")
    item_price = models.CharField(max_length=50)
    item_image = models.ImageField(upload_to='items/',default="")
    item_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.item_name

class system(models.Model):
    id = models.AutoField
    system_name = models.CharField(max_length=70)
    system_category = models.CharField(max_length = 150, blank = True)
    system_desc = models.CharField(max_length = 500)
    system_feature = models.CharField(max_length = 350)
    system_image1 = models.ImageField(upload_to = 'systems/')
    system_image2 = models.ImageField(upload_to = 'systems/')
    system_price = models.CharField(max_length = 50)
    system_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.system_name

class contact(models.Model):
    id=models.AutoField
    contact_name = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=50)
    contact_message = models.CharField(max_length = 500)
    contact_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.contact_name + "(" + self.contact_email + ")"

#Django Admin SuperUser details = Name: shivam , Password: shivam
# check contacts table in it