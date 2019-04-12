
class Job:

    def __init__(self, **kwargs):
        self.job_id = kwargs.get('physical_name', None)
        self.frequency = kwargs.get('physical_name', None)
        self.loading_type = kwargs.get('physical_name', None)
        self.target_delimiter = kwargs.get('physical_name', None)
        self.source_delimiter = kwargs.get('physical_name', None)
