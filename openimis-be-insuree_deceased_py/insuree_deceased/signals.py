from django.db.models import Q

from core.service_signals import ServiceSignalBindType
from core.signals import bind_service_signal
from insuree.signals import signal_before_insuree_search_query
from insuree_deceased.models import InsureeDeceased
from insuree_deceased.service_validation import DeceasedInsureeServiceValidation
from insuree_deceased.services import DeceasedInsureeService


def append_isDeceased_filter_if_available(sender, **kwargs):
    additional_filter = kwargs.get('additional_filter', None)
    if "insureeDeceased" in additional_filter:
        # then check perms
        return Q(
            deceased__isnull=not additional_filter['insureeDeceased']
        )
    InsureeDeceased.objects.filter(is_null=True)


signal_before_insuree_search_query.connect(append_isDeceased_filter_if_available)


def bind_service_signals():
    def update_insuree_deceased_information(**kwargs):
        model = kwargs.get('result', None)
        deceased = model.json_ext.pop('insureeDeceased') if model.json_ext else None
        insuree_deceased = InsureeDeceased.objects.filter(insuree=model).first()
        if not insuree_deceased:
            DeceasedInsureeService(kwargs['sender'].user, DeceasedInsureeServiceValidation()).create({
                'decease_date': deceased['deceaseDate'],
                'insuree': model
            })
        else:
            DeceasedInsureeService(kwargs['sender'].user, DeceasedInsureeServiceValidation()).update({
                'decease_date': deceased['deceaseDate'],
                'insuree': model,
                'id': insuree_deceased.id
            })
        model.save()


    bind_service_signal(
        'insuree_service.create_or_update',
        update_insuree_deceased_information,
        bind_type=ServiceSignalBindType.AFTER
    )
