from django.db import models
from .validators import validate_symbols, validate_feeling, validate_score

# Create your models here.
class Page(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[validate_symbols]
    )
    content = models.TextField(
        validators=[validate_symbols]
    )
    feeling = models.CharField(
        max_length=80,
        validators=[validate_feeling]
    )
    score = models.IntegerField(
        validators=[validate_score]
    )
    dt_created = models.DateTimeField()

    def __str__(self):
        return self.title