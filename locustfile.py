import random
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.get("/")

    @task(6)
    def call_fast_endpoint(self):
        self.client.get("/fast")

    @task(3)
    def create_item(self):
        payload = {"name": f"item_{random.randint(1, 10000)}",
                   "price": random.randint(10, 500)}
        self.client.post("/items", json=payload)

    @task(1)
    def call_slow_endpoint(self):
        self.client.get("/slow")
