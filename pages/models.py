from django.db import models

# Create your models here.


class Appeal(models.Model):
    telegram_id = models.IntegerField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    appeal = models.TextField()
    is_answered = models.BooleanField(default=False)
    answer = models.TextField(blank=True,default='')

    class Meta:
        db_table = 'appeal'
        verbose_name = 'appeal'

    def __str__(self):
        return self.name