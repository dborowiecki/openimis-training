import graphene
from django.core.exceptions import PermissionDenied

from core.schema import OrderedDjangoFilterConnectionField, signal_mutation_module_validate
from insuree.apps import InsureeConfig
from insuree_deceased.gql.gql_mutations.deceased_mutations import CreateInsureeDeceasedMutation, \
    UpdateInsureeDeceasedMutation, DeleteInsureeDeceasedMutation
from insuree_deceased.gql.gql_types import InsureeDeceasedGQLType
from insuree_deceased.models import InsureeDeceased, InsureeDeceasedMutation
from django.utils.translation import gettext as _


class Query(graphene.ObjectType):
    insuree_deceased = OrderedDjangoFilterConnectionField(
        InsureeDeceasedGQLType
    )

    def resolve_insuree_deceased(self, info, **kwargs):
        if not info.context.user.has_perms(InsureeConfig.gql_query_insurees_perms):
            raise PermissionDenied(_("unauthorized"))
        if not kwargs.get('insuree__uuid'):
            raise ValueError("Insuree UUID has to be provide to get deceased data")
        return InsureeDeceased.objects.filter(**kwargs)


class Mutation(graphene.ObjectType):
    create_deceased = CreateInsureeDeceasedMutation.Field()
    update_deceased = UpdateInsureeDeceasedMutation.Field()
    delete_deceased = DeleteInsureeDeceasedMutation.Field()


def on_insuree_deceased_mutation(sender, **kwargs):
    uuid = kwargs['data'].get('uuid', None)
    if not uuid:
        return []
    if "InsureeDeceasedMutation" in str(sender._mutation_class):
        impacted_policy_holder = InsureeDeceased.objects.get(id=uuid)
        InsureeDeceasedMutation.objects.create(
            policy_holder=impacted_policy_holder,
            mutation_id=kwargs['mutation_log_id']
        )
    return []


def bind_signals():
    signal_mutation_module_validate["insuree_deceased"].connect(on_insuree_deceased_mutation)
