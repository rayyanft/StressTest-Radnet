#! venv/bin/python3

from locust import HttpUser, constant, task, tag, events, LoadTestShape, between

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
    print("Test dimulai")

@events.test_stop.add_listener
def callStop(environment, **kwargs):
    print("Test selesai")

class websiteUser(HttpUser):
    wait_time = constant(1)

    def on_start(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("news")
    @task(10)
    def news(self):
        with self.client.get("/cat/1/news", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def karir(self):
        with self.client.get("/cat/2/karier", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def ekonomiBisnis(self):
        with self.client.get("/cat/3/ekonomi-bisnis", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def sejarahBudaya(self):
        with self.client.get("/cat/4/sejarah-budaya", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def kesehatan(self):
        with self.client.get("/cat/5/kesehatan", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def olahraga(self):
        with self.client.get("/cat/6/olahraga", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def lifestyle(self):
        with self.client.get("/cat/7/lifestyle", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def teknologi(self):
        with self.client.get("/cat/8/teknologi", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def otomotif(self):
        with self.client.get("/cat/9/otomotif", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def internasional(self):
        with self.client.get("/cat/10/internasional", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("kategori")
    @task(5)
    def defence(self):
        with self.client.get("/cat/11/defence", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")

    @tag("news")
    @task(3)
    def index(self):
        with self.client.get("/all-news", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("halaman gagal dibuka")