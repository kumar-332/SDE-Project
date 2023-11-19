from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def landing_page(self):
        self.client.get("/")

    @task
    def browse(self):
        self.client.get("/store")