from django.db import models
class Event(models.Model):
    event_title=models.CharField(max_length=120)
    event_location=models.CharField(max_length=70)
    event_date=models.CharField(max_length=120)
    event_description=models.TextField()
    def _str_(self):
        return self.event_title
    

class read(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=70)
    phone=models.CharField(max_length=20)
    event=models.ForeignKey('Event',on_delete=models.CASCADE)

