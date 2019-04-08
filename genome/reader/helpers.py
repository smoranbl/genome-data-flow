
import json as js

import httplib2
from googleapiclient import discovery
from oauth2client import file, client, tools

import settings as stt


# Create Google API credentials
def create_credentials(secret, scope, storage):
    """
    :param secret: string, Contains the path for client secrets json parameters
    :param scope: string, Attribute for delimit the scope of the  Google API requests
    :param storage: oauth2client.file.Storage, Contains the path for credentials.json temporal storage
    :return: oauth2client.client.Credentials, Credentials with the authorization token
    """
    stt.logger.info('create_credentials is being called with the params: secret={}, scope={}'.
                    format(secret, scope))

    flow = client.flow_from_clientsecrets(filename=secret, scope=scope)
    # Execute all steps needed for get new authorization credentials
    return tools.run_flow(flow, storage)


# Get Google API credentials
def get_credentials(secret, scope, temp_cred):
    """
    :param secret: string, Contains the path for client secrets json parameters
    :param scope: string, Attribute for delimit the scope of the  Google API requests
    :param temp_cred: string, Contains the path for credentials.json temporal storage
    :return: oauth2client.client.Credentials, Credentials with the authorization token
    """
    stt.logger.info('get_credentials is being called with the params: secret={}, scope={}, temp_cred={}'.
                    format(secret, scope, temp_cred))

    storage = file.Storage(temp_cred)
    credentials = storage.get()
    # TODO: Pending to review the function "credentials.invalid" for exception management
    #       This function can throw a WARNING and the idea is to put it in a LOG.INFO
    # If temporal credentials is in force return it, other way create new credentials
    if not credentials or credentials.invalid:
        credentials = create_credentials(secret, scope, storage)

    return credentials


# Get Google API sheet service
def get_sheet_service(credentials):
    """
    :param credentials: oauth2client.client.Credentials, Credentials with the authorization token
    :return: service, A Resource object with methods for interacting with the service
    """
    stt.logger.info('get_sheet_service is being called')

    # Build http request with the authorization credentials
    http = credentials.authorize(httplib2.Http())

    # Create a sheets service object
    return discovery.build(serviceName='sheets', version='v4', http=http)


# Read spreadsheet indicated by the id and range
def get_spreadsheet(service, spreadsheet_id, sheet_range):
    """
    :param service: Service Object, A Resource object with methods for interacting with the service sheets
    :param spreadsheet_id: string, Identifier of the spreadsheet that want to return
    :param sheet_range: string, Range of rows and columns of the spreadsheet
    :return: list, Metadata and matrix data of the spreadsheet
    """
    stt.logger.info('get_spreadsheet is being called with the params: service, spreadsheet_id={}, sheet_range={}'.
                    format(spreadsheet_id, sheet_range))

    # API call for get spreadsheet data and metadata
    values = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet_range).execute()['values']

    stt.logger.info('get_spreadsheet is returning a list with {} rows'.format(len(values)))
    return values


# Load the data dictionary template version in a Schema instance
def get_schema_template(version='v1.0', level='object'):
    """
    :param version: string, Version of the required schema
    :param level: string, Indicates schema type, object or field
    :return: dictionary, Schema info for passed version and level
    """
    stt.logger.info('get_schema_template is being calling with the params: version={}, level={}'
                    .format(version, level))

    path = '../resources/schemas/{version}/{level}_schema.json'.format(version=version, level=level)
    # Open the defined file and load json data
    with open(path) as json_file:
        schema_json = js.load(json_file)

    schema_template = schema_json['template']

    return schema_template


# TODO: I'm not sure that copy() is necessary, need to check if schema
#       change with a equal reference
# Order the attr list based on the Attribute.position if it's informed
def order_schema_template(to_order_attrs):
    """
    :param to_order_attrs: list, Attribute object list to order by Attribute.position
    :return: list, ordered list by Attribute.position
    """
    stt.logger.info('order_schema_template is being calling')

    if to_order_attrs is not None:
        return sorted(to_order_attrs, key=lambda key: key.position).copy()
