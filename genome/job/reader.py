
import networkx as nx

from entities import Schema, Attribute
from handlers import google as gh
from handlers import json as jh
from helpers import context as ctx


# Instance object schema with json version of data dictionary layout
def load_schema(version, level):
    # TODO: I'm not sure that copy() is necessary, need to check if schema
    #       change with a equal reference
    # Order the attr list based on the Attribute.position if it's informed
    def order_schema(to_order_attrs):
        if to_order_attrs is not None:
            return sorted(to_order_attrs, key=lambda key: key.position).copy()

    template = jh.get_schema_template(version, level)
    attrs = map(lambda c: Attribute(c['name'], c['description'], c['position'], c['group']), template)
    attrs = order_schema(list(attrs))

    return Schema(version, level, attrs)


# Auth google sheets service and get data from defined sheet and spreadsheet range
def load_sheet(sheet_id, sheet_range):
    credentials = gh.get_credentials(ctx.g_secret, ctx.g_scope, ctx.g_credentials)
    ctx.service = load_service(credentials)

    return gh.get_spreadsheet(ctx.service, sheet_id, sheet_range)


def load_service(credentials):
    return gh.get_sheet_service(credentials) if ctx.service is None else ctx.service


def load_network():
    return nx.Graph() if ctx.G is None else ctx.G
