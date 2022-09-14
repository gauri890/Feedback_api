from django.db import models

# Create your models here.

class feedback(models.Model):
    level = (
        ("Very Satisfield","Very Satisfield"),
        ("Satisfield","Satisfield"),
        ("Okayish","Okayish"),
        ("Unsatisfield","Unsatisfield")
    )

    Name = models.CharField(max_length = 15)
    Owned_Date = models.DateField()
    Satisfaction_level = models.CharField(max_length = 15,choices = level,default = "Very Satisfield")
    Feedback = models.TextField(max_length = 500,blank = True)

    def __str__(self):
        return self.Name
        