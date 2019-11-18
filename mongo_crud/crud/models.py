from djongo import models


class Student(models.Model):
    name = models.CharField(max_length=100, default="")
    standard = models.CharField(max_length=50, default="")
    roll = models.BigIntegerField()
    essay_topic = models.CharField(max_length=100, default="")
    essay = models.TextField(default="")

    class Meta:
        """Meta."""

        managed = True
        db_table = "name"

    def __str__(self):
        """__str__."""
        return self.name