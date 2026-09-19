#! myvenv/bin/python3

from locust import HttpUser, task, between, tag, events, LoadTestShape
from locust.runners import MasterRunner

# class loadTest(LoadTestShape):
#     stages = [{"duration" : 180, "users" : 100, "spawn_rate" : 20},
#     {"duration":360, "users": 300, "spawn_rate":20},
#     {"duration":540, "users": 600, "spawn_rate":20},
#     {"duration":720, "users": 1000, "spawn_rate": 20}]

#     def tick(self):
#         run_time = self.get_run_time()

#         for stage in self.stages:
#             if run_time < stage["duration"]:
#                 return (stage["users"], stage["spawn_rate"])

@events.test_start.add_listener
def on_test_start (environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        print("Beginning test setup")
    else:
        print("Started test from Master node")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
        if not isinstance(environment.runner, MasterRunner):
            print("Cleaning up test data")
        else:
            print("Stopped test from Master node")

class WebUser(HttpUser):
    wait_time = between(1,5)

    @tag ('GetBeranda')
    @task(5)
    def LokakaryaRadnext(self):
        with self.client.get("/", catch_response = True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal")

    @tag('GetJadwalSeminar')
    @task(3)
    def JadwalSeminar(self):
        with self.client.get("/list-seminar", catch_response = True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal")

    @tag('GetTentangKami')
    @task(2)
    def AboutUs(self):
        with self.client.get("/about", catch_response = True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal")

    @tag('GetKontak')
    @task(1)
    def Kontak(self):
        with self.client.get("/kontak", catch_response = True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal")

    @tag('GetLogin')
    @task(5)
    def LoginPage(self):
        with self.client.get("/login", catch_response = True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal")

    @tag('PostLogin')
    @task(3)
    def Login(self):
        with self.client.post("/login", json={"Username": "ney", "Password": "password123"}, catch_response = True) as response:
            if response.status_code == 200:
                response.failure("Akun tidak ditemukan")
            else:
                response.success()