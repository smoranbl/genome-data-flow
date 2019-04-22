
from reader import reader
from writer import writer

# Default sample sheet id for testing
test_sheet_id = '1JXTenp08F6IqKQ_grlZfzt2Av9Yf1Hggcr5u15ydKBQ'
template_sheet_id = '1dC9XPEH3XmG8fVHvLc4FBhc9H4O1FKeWohWpxk5M6p4'


# TODO: Need to make the spreadsheet reader part more dynamic, must be prepared
#  to load data from different PI and sections (MASTER, RAW nd CUSTOM)
data_dictionary = reader.read_data_dictionary('2Q19', test_sheet_id)

# legend_template = reader.read_legend_template('2Q19', template_sheet_id)
# writer.write_legend_template(legend_template)
