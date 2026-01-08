class Resource:
    def __init__(self, rid):
        self.rid = rid
        self.allocated_to = None
        self.waiting_queue = []

    def __str__(self):
        return f"Resource {self.rid} | Allocated to: {self.allocated_to}"
