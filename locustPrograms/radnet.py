#!venv/bin/python3

from locust import HttpUser, constant, task, tag, events

class WebsiteUser(HttpUser):
    wait_time = constant(2)

    @tag("mainPage")
    @task(10)
    def mainPage(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman")
    
    @tag("produkLayanan")
    @task(8)
    def radnextInternet(self):
        with self.client.get("/radnext-internet", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(8)
    def privatePeering(self):
        with self.client.get("/private-peering", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(8)
    def internetSecurity(self):
        with self.client.get("/internet-security", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(3)
    def indocenter(self):
        with self.client.get("/hosting", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(8)
    def ezyHome(self):
        with self.client.get("/ezyhome", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(5)
    def ezySky(self):
        with self.client.get("/ezysky", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(5)
    def exyEMS(self):
        with self.client.get("/ezyems", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(5)
    def ezyMG(self):
        with self.client.get("/ezymg", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(5)
    def ezyDNS(self):
        with self.client.get("/ezydns", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(3)
    def siadi(self):
        with self.client.get("/siadi", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("produkLayanan")
    @task(3)
    def akademiDigitalIndonesia(self):
        with self.client.get("/akademi-digital-indonesia", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman produk layanan")

    @tag("dukungan")
    @task(8)
    def FAQ(self):
        with self.client.get("/faq", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman dukungan")
    
    @tag("dukungan")
    @task(8)
    def video(self):
        with self.client.get("/radnext-video", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman dukungan")

    @tag("tentangKami")
    @task(9)
    def tentangKami(self):
        with self.client.get("/tentang-kami", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Gagal membuka halaman tentang-kami")