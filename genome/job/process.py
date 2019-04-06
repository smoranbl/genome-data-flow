
import networkx as nx

from entities import Object


def process_data(schema, data):
    graph = nx.Graph()

    for spreadsheet in data:
        print('Im in process_data')
        print(spreadsheet)
        map(process_object, spreadsheet)


def process_object(row):
    attrs = dict(zip(schema.get_schema_headers(), row))
    node = Object(**attrs)
    graph.add_node(node, attr=':Object')
