# RADNET Load Testing Interface

Interface internal untuk membantu tim RADNET menjalankan, mengatur, dan memantau load testing pada website atau layanan yang telah mendapatkan izin resmi.

Penggunaan alat ini hanya untuk pengujian yang sah dan terotorisasi. Dilarang menjalankan load test terhadap sistem, domain, atau API tanpa persetujuan dari pemilik layanan.

---

## Tujuan

Project ini menyediakan satu antarmuka terpusat untuk mempermudah eksekusi dan pemantauan load testing. Fitur utama yang disediakan meliputi:

* Pemilihan target pengujian (Ezy Web, Riwara, Lokakarya, dan Radnet).
* Konfigurasi parameter pengujian (Total Users, Spawn Rate, dan Run Time).
* Eksekusi pengujian secara kustom menggunakan skrip Locust.
* Pemantauan statistik performa (Response Time Percentiles) secara real-time.
* Penghentian proses pengujian secara instan dan aman.

---

## Teknologi

* Backend: Python (Flask)
* Frontend: HTML, CSS, JavaScript (Fetch API)
* Load-Testing Engine: Locust
* Inter-Process Communication: Python Subprocess

---

## Dokumentasi dan Demo

### Alur Antarmuka

docs/Index-Preview.png
docs/Dashboard-Preview.png

### Demonstrasi Pengujian

docs/Demo-StressTest.mp4

---

## Struktur Project

├── app.py                  # Server backend Flask dan routing API
├── requirements.txt        # Daftar dependensi Python
├── locustPrograms/         # Skenario pengujian Locust (.py)
│   ├── ezyWeb.py
│   ├── riwara.py
│   ├── lokakarya.py
│   └── radnet.py
├── templates/              # File antarmuka HTML
│   ├── index.html          # Halaman form konfigurasi pengujian
│   └── dashboard.html      # Halaman pemantauan statistik real-time
└── docs/                   # Dokumentasi visual dan aset laporan
    ├── Demo-StressTest.mp4
    ├── Index-Preview.png
    └── Dashboard-Preview.png

---

## Persiapan dan Penggunaan Lokal

### 1. Clone Repository
git clone <repository-url>
cd radnet-loadtest-interface

### 2. Salin dan Atur Environment Variable
cp .env.example .env

Isi file `.env` sesuai dengan konfigurasi lokal yang diberikan oleh tim.

### 3. Instal Dependensi
Pastikan Python 3.x telah terinstal, lalu jalankan:
pip install -r requirements.txt

### 4. Jalankan Aplikasi
python app.py

### 5. Akses Aplikasi
Buka browser dan akses alamat berikut:
http://localhost:5000

---

## Aturan Penggunaan Load Test

Sebelum menjalankan pengujian, pastikan:

1. Target pengujian telah memperoleh persetujuan tertulis dari pemilik sistem.
2. Waktu pelaksanaan pengujian telah dikomunikasikan kepada tim terkait.
3. Batas virtual user, durasi, dan spawn rate telah ditentukan secara aman.
4. Pengujian tidak menggunakan data produksi atau data pribadi tanpa izin.
5. Terdapat PIC yang siaga dan dapat dihubungi selama proses pengujian.
6. Pengujian segera dihentikan apabila terdeteksi gangguan pada sistem target.