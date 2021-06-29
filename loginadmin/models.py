from django.db import models

# Create your models here.
STATUS=(
    (0,"Admin"),
    (1,"Library"),
    (2,"Exam"),
    (3,"Placement")
)
class loginadmin(models.Model):
    admin_id=models.AutoField(primary_key=True)
    admin_name=models.CharField(max_length=100,null=False)
    admin_mail=models.EmailField(max_length=254,null=False)
    admin_pword=models.CharField(max_length=100,null=False)
    admin_panel=models.IntegerField(choices=STATUS,default=0)
    def __str__(self):
        return self.admin_name

