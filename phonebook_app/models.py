from django.db import models
from django.conf import settings


# Create your models here.
User = settings.AUTH_USER_MODEL


class Contact(models.Model):
    author = models.ForeignKey(User, default=1, null=True,
                               on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


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
