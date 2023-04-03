from core.models import UUIDModel, MutationLog
from django.db import models
from datetime import datetime as py_datetime

# Create your models here.
from insuree.models import Insuree

from core.fields import DateTimeField
from core.models import HistoryModel, ExtendableModel


class InsureeDeceased(HistoryModel):
    decease_date = DateTimeField(db_column="DateDeceased", default=py_datetime.now)
    insuree = models.ForeignKey(Insuree, models.DO_NOTHING, db_column='InsureeID', blank=True, null=True, related_name="deceased")


class InsureeDeceasedMutation(UUIDModel):
    policy_holder_insuree = \
        models.ForeignKey(InsureeDeceased, models.DO_NOTHING, related_name='mutations')
    mutation = models.ForeignKey(MutationLog, models.DO_NOTHING, related_name='insuree_deceased')

    class Meta:
        managed = True
        db_table = "insuree_deceased_InsureeDeceasedMutation"