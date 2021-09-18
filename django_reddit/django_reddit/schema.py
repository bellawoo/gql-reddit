import graphene
import graphql_jwt
import links.schema
import links.schema_relay
import users.schema


class Query(
    links.schema.Query,
    links.schema_relay.RelayQuery,
    users.schema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    links.schema.Mutation,
    links.schema_relay.RelayMutation,
    users.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)