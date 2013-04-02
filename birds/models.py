from django.db import models

class Recording(models.Model):
    url = models.URLField()
    common_name = models.CharField(max_length=200)
    catalog_id = models.IntegerField()
    sp = models.CharField(max_length=200)
    genus = models.CharField(max_length=200)



    def __unicode__(self):
        return self.genus + " " + self.sp 


    



    
