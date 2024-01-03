from django.db import models


class TestDB(models.Model):
    test_name = models.CharField(max_length=255)
    test_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.test_name
