from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _

from core.validation import BaseModelValidation
from insuree_deceased.apps import InsureeDeceasedConfig
from insuree_deceased.models import InsureeDeceased


class DeceasedInsureeServiceValidation(BaseModelValidation):
    OBJECT_TYPE = InsureeDeceased

    @classmethod
    def validate_create(cls, user, **data):
        if not user.has_perms(InsureeDeceasedConfig.can_create_deceased):
            raise PermissionDenied(_("unauthorized"))

    @classmethod
    def validate_update(cls, user, **data):
        if not user.has_perms(InsureeDeceasedConfig.can_update_deceased):
            raise PermissionDenied(_("unauthorized"))

    @classmethod
    def validate_delete(cls, user, **data):
        if not user.has_perms(InsureeDeceasedConfig.can_delete_deceased):
            raise PermissionDenied(_("unauthorized"))
