from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
User = settings.AUTH_USER_MODEL


class Contact(models.Model):
    author = models.ForeignKey(User, default=1, null=True,
                               on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.CharField(max_length=120, null=True, blank=True)
    job_title = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/',
                              height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('phone:phone_detail', kwargs={'pk': self.pk})


# Phone
class Phone(models.Model):
    phone = models.CharField(max_length=120)
    contact = models.ForeignKey(
        Contact, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone


# Email
class Email(models.Model):
    email = models.EmailField()
    contact = models.ForeignKey(
        Contact, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
