from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email  = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-created_date']
    def __str__(self):
        return self.name

class Type(models.Model):
    name  = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Proj_Cert(models.Model):
    image = models.ImageField(upload_to='website/', default='website/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    type= models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    Proj_Cert_url=models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_date']
      
    def __str__(self):
        return "{} - {}".format(self.title ,self.id)
    
    def snippets(self):
        return self.content[:100] + '...'
    
    class Meta:
        ordering=['-created_date']
    def __str__(self):
        return self.title
        