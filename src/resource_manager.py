class ResourceManager:
    def __init__(self, processes, resources):
        self.processes = processes
        self.resources = resources

    def request_resource(self, process, resource):
        if resource.allocated_to is None:
            resource.allocated_to = process.pid
            process.held_resources.add(resource.rid)
            print(f"Resource {resource.rid} allocated to Process {process.pid}")
        else:
            process.state = "Waiting"
            process.requested_resource = resource.rid
            resource.waiting_queue.append(process.pid)
            print(f"Process {process.pid} is waiting for Resource {resource.rid}")

    def release_resources(self, process):
        for res in self.resources:
            if res.allocated_to == process.pid:
                res.allocated_to = None
                print(f"Resource {res.rid} released from Process {process.pid}")

                if res.waiting_queue:
                    next_pid = res.waiting_queue.pop(0)
                    res.allocated_to = next_pid
                    print(f"Resource {res.rid} allocated to waiting Process {next_pid}")
