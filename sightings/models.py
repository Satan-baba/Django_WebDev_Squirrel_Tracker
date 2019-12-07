from django.db import models
  
class Sight(models.Model):
    x = models.FloatField('Latitude', default = 0.0)
    y = models.FloatField('Longitude', default = 0.0)
    unique_squi_id = models.CharField('Unique Squirrel ID', max_length = 200, default = '')
    Shift = models.CharField(max_length = 5, default = '')
    Date = models.IntegerField(default = 0)
    Age = models.CharField(max_length = 100, default = '')
    primary_fur_color = models.CharField(max_length = 200, default = '')
    Location = models.CharField(max_length = 100, default = '')
    specific_location = models.CharField(max_length = 100, default = '')
    running = models.BooleanField( default = False)
    Chasing = models.BooleanField(default = False)
    Climbing = models.BooleanField(default = False)
    Eating = models.BooleanField(default = False)
    Foraging = models.BooleanField(default = False)
    other_activities = models.CharField(max_length = 200, default = '')
    Kuks = models.BooleanField(default = False)
    Quaas = models.BooleanField(default = False)
    Moans = models.BooleanField(default = False)
    tail_flags = models.BooleanField(default = False)
    tail_twitches = models.BooleanField(default = False)
    approaches = models.BooleanField(default = False)
    indifferent = models.BooleanField(default = False)
    runs_from = models.BooleanField(default = False)
    def __str__(self):
        #return self.x, self.y, self.unique_squi_id, self.Shift, self.Date, self.Age, self.primary_fur_color, self.Location, self.specific_location, self.running, self.Chasing, self.Climbing, self.Eating, self.Foraging, self.other_activities, self.Kuks, self.Quaas, self.Moans, self.tail_flags, self.tail_twitches, self.approaches, self.indifferent, self.runs_from
         return self.unique_squi_id
# Create your models here.
