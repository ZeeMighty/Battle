from django.db import models



class heroe(models.Model):
    name = models.CharField(max_length = 100)
    biography = models.TextField()
    rewards = models.TextField()
    lived = models.CharField(max_length = 100)
    army = models.ForeignKey('army', on_delete=models.CASCADE, null=True)
    took_part = models.ForeignKey('event', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class event(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    result = models.TextField()
    participants = models.ManyToManyField(heroe, blank=True)
    event_id = models.ForeignKey('date', on_delete=models.CASCADE, related_name = "event_date", null=True)
    # event_date = models.ForeignKey('date', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class army(models.Model):
    name = models.CharField(max_length = 100)
    took_part_events = models.ManyToManyField(event, blank=True)
#    heroes = models.ForeignKey(heroe, on_delete=models.CASCADE, null=True)
    comander = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class date(models.Model):
    date = models.DateField()
#    date_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.date)


class place(models.Model):
    place = models.CharField(max_length = 200)
    place_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.place
