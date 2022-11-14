from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CopyRight(models.Model):
    company_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = 'CopyRight'


class ContactInformation(models.Model):
    phone_number = PhoneNumberField(region='BD', null=True)
    resume = models.FileField(null=True)
    

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name_plural = 'ContactInformation'


class ContactUs(models.Model):
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone_number = PhoneNumberField(region='BD')
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Contact Us'


class Portfolio(models.Model):
    project_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to="portfolio")

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = 'Portfolio'

class Service(models.Model):
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name_plural = 'Services'

class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'About'


class BannerPortion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner_img = models.ImageField(upload_to="banner", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Banner Portion'