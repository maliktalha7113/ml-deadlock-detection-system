import random
import pandas as pd

def generate_dataset(samples=500):
    data = []

    for _ in range(samples):
        num_processes = random.randint(2, 10)
        num_resources = random.randint(1, 5)

        waiting_processes = random.randint(0, num_processes)
        allocated_resources = random.randint(0, num_resources)

        resource_utilization = allocated_resources / num_resources
        avg_wait_time = random.uniform(0, 10)

        # Simple rule to simulate deadlock
        deadlock = 1 if (waiting_processes > num_processes / 2 and resource_utilization > 0.7) else 0

        data.append([
            num_processes,
            waiting_processes,
            resource_utilization,
            avg_wait_time,
            deadlock
        ])

    columns = [
        "num_processes",
        "waiting_processes",
        "resource_utilization",
        "avg_wait_time",
        "deadlock"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("../data/deadlock_dataset.csv", index=False)
    print("✅ Dataset generated and saved")
generate_dataset()
