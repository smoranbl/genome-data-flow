
import networkx as nx
import settings as stt

from process import helpers as ph


# Graph handler
G = nx.nx.DiGraph()


# Process loaded data from spreadsheet and map it in network Graph
def process_data(schema, data):
    """
    :param schema:
    :param data:
    :return:
    """
    stt.logger.info('process_data is being calling')

    for row in data:
        row_data = ph.get_dictionary_data(schema, row)
        process_graph(schema, row_data)

    stt.logger.info(G.nodes)
    stt.logger.info(G.edges)


# Process data of a row and create an :Object -> :JOB -> :Source data flow
def process_graph(schema, data):
    """
    :param schema:
    :param data:
    :return:
    """
    stt.logger.info('process_graph is being calling for the data: {}'.format(data))

    object_attr = ph.filter_by_group(schema.get_schema_headers_by_group('object'), data)
    job_attr = ph.filter_by_group(schema.get_schema_headers_by_group('job'), data)
    source_attr = ph.filter_by_group(schema.get_schema_headers_by_group('source'), data)

    master_labels = [':Entity', ':Object', ':Master']
    # raw_labels = [':Entity', ':Object', ':RAW']
    source_labels = [':Entity', ':Object', ':Source']

    # TODO: Need to add logic to identify when an object is from raw or master
    G.add_node(object_attr['physical_name'], labels=master_labels, values=object_attr)
    G.add_node(source_attr['source_physical_name'], labels=source_labels, values=source_attr)
    G.add_edge(object_attr['physical_name'], source_attr['source_physical_name'], values=job_attr)
