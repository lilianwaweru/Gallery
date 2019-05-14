from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)
    

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
    
    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()


class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()
    
    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()


class Image(models.Model):
    name = models.CharField(max_length = 70)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/',blank=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    
    def save_image(self):
        self.save()


    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains = search_term)
        return images

