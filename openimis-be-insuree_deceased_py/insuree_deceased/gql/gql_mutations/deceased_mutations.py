from core.gql.gql_mutations import DeleteInputType
from core.gql.gql_mutations.base_mutation import BaseMutation, BaseHistoryModelCreateMutationMixin, \
    BaseHistoryModelDeleteMutationMixin, BaseDeleteMutation, BaseHistoryModelUpdateMutationMixin
from insuree_deceased.gql.gql_mutations.input_types import InsureeDeceasedUpdateInputType, InsureeDeceasedInputType

from insuree_deceased.models import InsureeDeceased
from insuree_deceased.service_validation import DeceasedInsureeServiceValidation


class CreateInsureeDeceasedMutation(BaseHistoryModelCreateMutationMixin, BaseMutation):
    _mutation_class = "InsureeDeceasedMutation"
    _mutation_module = "insureeDeceased"
    _model = InsureeDeceased

    class Input(InsureeDeceasedInputType):
        pass

    @classmethod
    def _validate_mutation(cls, user, **data):
        super()._validate_mutation(user, **data)
        DeceasedInsureeServiceValidation.validate_create(user, **data)


class DeleteInsureeDeceasedMutation(BaseHistoryModelDeleteMutationMixin, BaseDeleteMutation):
    _mutation_class = "InsureeDeceasedMutation"
    _mutation_module = "insureeDeceased"
    _model = InsureeDeceased

    class Input(DeleteInputType):
        pass

    @classmethod
    def _validate_mutation(cls, user, **data):
        super()._validate_mutation(user, **data)
        DeceasedInsureeServiceValidation.validate_update(user, **data)


class UpdateInsureeDeceasedMutation(BaseHistoryModelUpdateMutationMixin, BaseMutation):
    _mutation_class = "InsureeDeceasedMutation"
    _mutation_module = "insureeDeceased"
    _model = InsureeDeceased

    class Input(InsureeDeceasedUpdateInputType):
        pass

    @classmethod
    def _validate_mutation(cls, user, **data):
        super()._validate_mutation(user, **data)
        DeceasedInsureeServiceValidation.validate_delete(user, **data)
