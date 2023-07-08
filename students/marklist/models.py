from django.db import models

# Create your models here.
class marklist(models.Model):
    rollno = models.CharField(max_length=20)
    sname = models.CharField(max_length=100)
    smark = models.CharField(max_length=5)

    class Meta:
        db_table = "marklist"