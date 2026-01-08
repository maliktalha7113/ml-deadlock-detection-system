from process import Process
from resource import Resource
from resource_manager import ResourceManager
from deadlock_detector import DeadlockDetector
from recovery_manager import RecoveryManager
from graph_visualizer import draw_wait_for_graph

import sys
sys.path.append("../ml")

from ml_model import predict_deadlock

# Create processes
processes = [Process(i) for i in range(1, 6)]

# Create resources
resources = [Resource(f"R{i}") for i in range(1, 4)]

rm = ResourceManager(processes, resources)
detector = DeadlockDetector(processes, resources)
recovery = RecoveryManager(processes, resources, rm)

# Simulate system activity
rm.request_resource(processes[0], resources[0])
rm.request_resource(processes[1], resources[1])
rm.request_resource(processes[2], resources[2])

rm.request_resource(processes[0], resources[1])
rm.request_resource(processes[1], resources[2])
rm.request_resource(processes[2], resources[0])

# ---- ML SYSTEM STATE SNAPSHOT ----
num_processes = len(processes)
waiting_processes = len([p for p in processes if p.state == "Waiting"])
resource_utilization = len([r for r in resources if r.allocated_to]) / len(resources)
avg_wait_time = sum(p.wait_time for p in processes) / len(processes)

system_state = [
    num_processes,
    waiting_processes,
    resource_utilization,
    avg_wait_time
]

probability = predict_deadlock(system_state)
print(f"\n🤖 ML Deadlock Probability: {probability:.2f}")

# ---- DECISION ----
if probability > 0.7:
    print("⚠️ High deadlock risk detected (ML)")

    graph = detector.build_wait_for_graph()
    draw_wait_for_graph(graph)

    recovery.recover_from_deadlock()

elif detector.detect_deadlock():
    print("🚨 Deadlock Detected (Classical)")

    graph = detector.build_wait_for_graph()
    draw_wait_for_graph(graph)

    recovery.recover_from_deadlock()
else:
    print("✅ System running safely")
