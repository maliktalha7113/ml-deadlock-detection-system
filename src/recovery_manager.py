class RecoveryManager:
    def __init__(self, processes, resources, resource_manager):
        self.processes = processes
        self.resources = resources
        self.resource_manager = resource_manager

    def select_victim(self):
        # Select process holding the most resources
        active_processes = [p for p in self.processes if p.state != "Terminated"]
        victim = max(active_processes, key=lambda p: len(p.held_resources))
        return victim

    def recover_from_deadlock(self):
        victim = self.select_victim()
        print(f"\n❌ Terminating Process {victim.pid}")

        # Terminate process
        victim.state = "Terminated"

        # Release its resources
        self.resource_manager.release_resources(victim)
        victim.held_resources.clear()
        victim.requested_resource = None

        print(f"🔄 Recovering Process {victim.pid}")

        # Restart process (simulation)
        victim.state = "Running"
