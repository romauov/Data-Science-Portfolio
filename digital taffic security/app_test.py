import pandas as pd
from locust import HttpUser, task, constant_throughput


df = pd.read_csv('datasets/network_traffic_data.csv')


class TrafficActivity(HttpUser):
    wait_time = constant_throughput(1)

    @task
    def predict(self):
        self.client.post(
            "/predict",
            json=df.sample(1).to_dict('records')[0],
            timeout=1,
        )
