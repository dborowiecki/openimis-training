import graphene

from core.schema import OpenIMISMutation


class InsureeDeceasedInputType(OpenIMISMutation.Input):
    decease_date = graphene.Date(required=False)
    json_ext = graphene.types.json.JSONString(required=False)
    insuree_id = graphene.Int(required=False, name="insureeId")


class InsureeDeceasedUpdateInputType(InsureeDeceasedInputType):
    id = graphene.UUID(required=True)