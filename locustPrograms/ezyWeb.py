#! venv/bin/python3

from locust import HttpUser, task, between, tag, events, LoadTestShape, constant

# class loadTest(LoadTestShape):
#     stages = [{"duration" : 180, "users" : 1000, "spawn_rate" : 20},
#     {"duration":360, "users": 1300, "spawn_rate":20},
#     {"duration":540, "users": 1600, "spawn_rate":20},
#     {"duration":720, "users": 2000, "spawn_rate": 20}]

#     def tick(self):
#         run_time = self.get_run_time()

#         for stage in self.stages:
#             if run_time < stage["duration"]:
#                 return (stage["users"], stage["spawn_rate"])

@events.test_start.add_listener
def callStart(environment, **kwargs):
    print("Test Mulai")

@events.test_stop.add_listener
def callStop(environment, **kwargs):
    print("Test Selesai")

class websiteUser(HttpUser):
    wait_time = constant(1)

    @tag("index")
    @task(10)
    def beranda(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Halaman gagal dibuka : {response.status_code}")

    @tag("akun")
    @task(3)
    def register(self):
        with self.client.get("/register", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Halaman gagal dibuka : {response.status_code}")
    
    @tag("about")
    @task(7)
    def about(self):
        with self.client.get("/tentang-kami", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Halaman gagal dibuka: {response.status_code}")
    
    @tag("layanan")
    @task(8)
    def layanan(self):
        with self.client.get("/layanan", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Halaman gagal dibuka: {response.status_code}")
    
    @tag("demo")
    @task(4)
    def demo(self):
        with self.client.get("/demo", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Halaman gagal dibuka: {response.status_code}")

    @tag("kontak")
    @task(5)
    def kontak(self):
        with self.client.get("/kontak", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Halaman gagal dibuka: {response.status_code}")