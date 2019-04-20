
from reader import reader


# Default sample sheet id for testing
test_sheet_id = '1JXTenp08F6IqKQ_grlZfzt2Av9Yf1Hggcr5u15ydKBQ'


# TODO: Need to make the spreadsheet reader part more dynamic, must be prepared
#  to load data from different PI and sections (MASTER, RAW nd CUSTOM)

reader.load_data_dictionary('v1.0', test_sheet_id)
