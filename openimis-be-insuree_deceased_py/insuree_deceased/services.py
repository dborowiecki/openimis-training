import logging

from core.services import BaseService
from insuree_deceased.models import InsureeDeceased

logger = logging.getLogger(__name__)


class DeceasedInsureeService(BaseService):
    OBJECT_TYPE = InsureeDeceased

