
import httplib2
from googleapiclient import discovery
from oauth2client import file, client, tools

# API_SCOPE: Default API scope for read spreadsheets in readonly mode
API_SCOPE = 'https://www.googleapis.com/auth/spreadsheets.readonly'
# CREDENTIALS_PATH: Path for storage temporal credentials once the first
CREDENTIALS_PATH = '../resources/google_api/credentials.json'
# SECRETS_PATH: Path for the client secret json that contains the google_api values
SECRETS_PATH = '../resources/google_api/client_id.json'


def create_credentials(filename=SECRETS_PATH, scope=API_SCOPE, storage=None):
    """
    :param filename: string, Contains the path for client secrets json parameters
    :param scope: string, Attribute for delimit the scope of the  Google API requests
    :param storage: oauth2client.file.Storage, Contains the path for credentials.json temporal storage
    :return: oauth2client.client.Credentials, Credentials with the authorization token
    """
    flow = client.flow_from_clientsecrets(filename=filename, scope=scope)
    # Execute all steps needed for get new authorization credentials
    return tools.run_flow(flow, storage)


def get_credentials(filename=SECRETS_PATH, scope=API_SCOPE, temp_filename=CREDENTIALS_PATH):
    """
    :param filename: string, Contains the path for client secrets json parameters
    :param scope: string, Attribute for delimit the scope of the  Google API requests
    :param temp_filename: string, Contains the path for credentials.json temporal storage
    :return: oauth2client.client.Credentials, Credentials with the authorization token
    """
    storage = file.Storage(temp_filename)
    credentials = storage.get()
    # TODO: Pending to review the function "credentials.invalid" for exception management
    #       This function can throw a WARNING and the idea is to put it in a LOG.INFO
    # If temporal credentials is in force return it, other way create new credentials
    return create_credentials(filename, scope, storage) if not credentials or credentials.invalid else credentials


def get_sheet_service(credentials):
    """
    :param credentials: oauth2client.client.Credentials, Credentials with the authorization token
    :return: Service Object, A Resource object with methods for interacting with the service
    """
    # Build http request with the authorization credentials
    http = credentials.authorize(httplib2.Http())
    # Create a sheets service object
    return discovery.build(serviceName='sheets', version='v4', http=http)


def get_spreadsheet(service, spreadsheet_id, sheet_range):
    """
    :param service: Service Object, A Resource object with methods for interacting with the service sheets
    :param spreadsheet_id: string, Identifier of the spreadsheet that want to return
    :param sheet_range: string, Range of rows and columns of the spreadsheet
    :return: List, Metadata and matrix data of the spreadsheet
    """
    # API call for get spreadsheet data and metadata
    return service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet_range).execute()
