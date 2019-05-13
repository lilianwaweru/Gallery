from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class CategoryTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.name = Category(name = 'sports')

    #testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category)) 

    #testing save method
    def test_save_method(self):
        self.name.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)


class LocationTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.name = Location(name = 'Nairobi')

    #testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Location)) 

    #testing save method
    def test_save_method(self):
        self.name.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.location = Location(name = 'Nairobi')
        self.location.save_location()

        self.category = Category(name = 'sports')
        self.category.save_category()

        self.name = Image(name = 'football', description = 'an image showing football', category = self.category, location = self.location)

     #testing save method
    def test_save_method(self):
        self.name.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

