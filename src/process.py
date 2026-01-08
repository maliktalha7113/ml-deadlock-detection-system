class Process:
    def __init__(self, pid):
        self.pid = pid
        self.state = "Running"  # Running, Waiting, Terminated
        self.held_resources = set()
        self.requested_resource = None
        self.wait_time = 0
        self.priority = 1

    def __str__(self):
        return f"Process {self.pid} | State: {self.state}"
