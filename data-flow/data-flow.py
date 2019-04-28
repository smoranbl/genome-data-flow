
from reader import reader

# Default sample sheet id for testing
test_sheet_id = '1xKIXrRT4c3o16a5nHjHhSzT14Zt2sANgv4zZEIQ99mk'
template_sheet_id = '1dC9XPEH3XmG8fVHvLc4FBhc9H4O1FKeWohWpxk5M6p4'


data_dictionary = reader.read_data_dictionary('2Q19', test_sheet_id)
# writer.write_data_dictionary(data_dictionary)

# template = reader.read_template_dictionary('2Q19', template_sheet_id)
# writer.write_template_dictionary('2Q19', template)
