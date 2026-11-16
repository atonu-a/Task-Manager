from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    
    STATUS = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    CATEGORY = [      
        ('Personal', 'Personal'),
        ('Study', 'Study'),
        ('Work', 'Work'),
        ('Other', 'Work'),
    ]
    
    
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    due_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default="Pending")
    category = models.CharField(max_length=10, choices=CATEGORY, default="Personal")
    
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.title
    
    
