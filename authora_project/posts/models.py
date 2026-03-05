from django.db import models

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='posts/')
    content=models.TextField(blank=True,null=True)
    category = models.ForeignKey(
    'categories.Category',
    on_delete=models.CASCADE,
    related_name="posts",
    )
    STATUS_CHOICE = [
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    ]
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='pending')
    
    def __str__(self):
        return self.title
    
