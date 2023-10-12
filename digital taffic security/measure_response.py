import requests
import time
import numpy as np
from tqdm import tqdm
import pandas as pd

if __name__ == "__main__":
    # Example loan application
    df = pd.read_csv('datasets/network_traffic_data.csv')

    # Location of my server
    url = "http://0.0.0.0:8989/predict"

    # Measure the response time
    all_times = []
    # For 1000 times
    for i in tqdm(range(1000)):
        t0 = time.time_ns() // 1_000_000
        # Send a request
        application = df.sample(1).to_dict('records')[0]
        resp = requests.post(url, json=application)
        t1 = time.time_ns() // 1_000_000
        # Measure how much time it took to get a response in ms
        time_taken = t1 - t0
        all_times.append(time_taken)

    # Print out the results
    print("Response time in ms:")
    print("Median:", np.quantile(all_times, 0.5))
    print("95th precentile:", np.quantile(all_times, 0.95))
    print("Max:", np.max(all_times))
