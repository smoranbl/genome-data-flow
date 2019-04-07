
import logging


# Create a custom logger
logger = logging.getLogger('GENOME')

"""
File handler configuration for logger

f_handler = logging.FileHandler('../resources/genome.log')
f_handler.setLevel(logging.ERROR)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
"""

# Create handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)

# Create formatter and add it to handlers
c_format = logging.Formatter('%(name)s - [%(levelname)s]: %(message)s')
c_handler.setFormatter(c_format)

# Add handlers to the logger
logger.addHandler(c_handler)

###############################################################################################

# Default API scope for read spreadsheets in readonly mode
g_scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'
# Default path for storage temporal credentials once the first
g_credentials = '../resources/google_api/credentials.json'
# Default path for the client secret json that contains the google_api values
g_secret = '../resources/google_api/client_id.json'
# Default sample sheet id for testing
g_sheet_id = '1p01TJG6K19E7_Abb0kDigZFOPCTIh9VZ7ZKLQCajgUc'
# Default sample sheet range of raw data for testing
g_raw_range = 'DC-DD-Object-RAW!A5:AI'
# Default sample sheet range of master data for testing
g_master_range = 'DC-DD-Object-MASTER!A5:AI'
