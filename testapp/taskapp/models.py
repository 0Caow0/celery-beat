from django.db import models


class DBTestDataBase(models.Model):
    user_id = models.DecimalField(max_digits=10,
                                  decimal_places=0,
                                  null=False,
                                  default=1)
    type = models.CharField(max_length=256,
                            null=False,
                            blank=False)


class DBTestTest(models.Model):
    data_info = models.ForeignKey(DBTestDataBase,
                                  related_name='data_info',
                                  on_delete=models.CASCADE)
    date = models.CharField(max_length=256,
                            null=False,
                            blank=True)
    value = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                null=False,
                                default=1)
