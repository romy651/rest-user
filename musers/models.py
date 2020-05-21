from django.db import models


def upload_to_image(instance, filename):
    return '{user}/{filename}'.format(user=instance.name, filename=filename)


class Muser(models.Model):
    name = models.TextField()
    surname = models.TextField()
    accountId = models.TextField()
    birthdate = models.DateField()
    citezenship = models.TextField()
    fname = models.TextField()
    count = models.IntegerField()
    mname = models.TextField()
    email = models.EmailField()
    balance = models.IntegerField()
    profile_photo = models.FileField(
        upload_to=upload_to_image, blank=True, null=True)
    passport_number = models.TextField()
    password = models.TextField()

    def __str__(self):
        return str(self.name)


class Beneficiary(models.Model):
    owner = models.ForeignKey(Muser, on_delete=models.CASCADE)
    name = models.TextField()
    surname = models.TextField()
    birthdate = models.DateField()
    citezenship = models.TextField()
    passport_number = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return str(self.name)
