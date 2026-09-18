from flask import Flask, request, jsonify, render_template
import subprocess
import os
import csv

app = Flask(__name__)

locust_process = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/laporan")
def laporan():
    return render_template("laporan.html")

@app.route("/start-ezyweb", methods=["POST"])
def mulaiEzy():

    global locust_process

    data = request.json
    users = data.get("users")
    spawn_rate = data.get("spawn_rate")
    time = data.get("time")

    if not os.path.exists("locustPrograms/ezyWeb.py"):
        return jsonify({"status": "error", "message": "Program tidak ditemukan"})
    
    if locust_process is not None:
        locust_process.terminate()

    command = [
        "locust", "-f", "locustPrograms/ezyWeb.py", "--headless", "-u", str(users),
        "-r", str(spawn_rate), "-t", str(time), "--host", "https://ezy.web.id",
        "--html", "templates/laporan.html", "--logfile", "logfile.log", "--csv","locust"
    ]

    locust_process = subprocess.Popen(command)

    return jsonify({"status": "program berjalan"})
    
@app.route("/start-riwara", methods=["POST"])
def mulaiRiwara():

    global locust_process

    data = request.json
    users = data.get("users")
    spawn_rate = data.get("spawn_rate")
    time = data.get("time")

    if not os.path.exists("locustPrograms/riwara.py"):
        return jsonify({"status": "error", "message": "Program tidak ditemukan"})
    
    if locust_process is not None:
        locust_process.terminate()

    command = [
        "locust", "-f", "locustPrograms/riwara.py", "--headless", "-u", str(users),
        "-r", str(spawn_rate), "-t", str(time), "--host", "https://riwara.id",
        "--html", "templates/laporan.html", "--logfile", "logfile.log", "--csv","locust"
    ]

    locust_process = subprocess.Popen(command)

    return jsonify({"status": "program berjalan"})
    
@app.route("/start-lokakarya", methods=["POST"])
def mulaiLoka():

    global locust_process

    data = request.json
    users = data.get("users")
    spawn_rate = data.get("spawn_rate")
    time = data.get("time")

    if not os.path.exists("locustPrograms/lokakarya.py"):
        return jsonify({"status": "error", "message": "Program tidak ditemukan"})
    
    if locust_process is not None:
        locust_process.terminate()

    command = [
        "locust", "-f", "locustPrograms/lokakarya.py", "--headless", "-u", str(users),
        "-r", str(spawn_rate), "-t", str(time), "--host", "https://lokakarya.radnext.id",
        "--html", "templates/laporan.html", "--logfile", "logfile.log", "--csv","locust"
    ]

    locust_process = subprocess.Popen(command)

    return jsonify({"status": "program berjalan"})
    
@app.route("/start-radnext", methods=["POST"])
def mulaiRadnet():

    global locust_process

    data = request.json
    users = data.get("users")
    spawn_rate = data.get("spawn_rate")
    time = data.get("time")

    if not os.path.exists("locustPrograms/radnet.py"):
        return jsonify({"status": "error", "message": "Program tidak ditemukan"})
    
    if locust_process is not None:
        locust_process.terminate()

    command = [
        "locust", "-f", "locustPrograms/radnet.py", "--headless", "-u", str(users),
        "-r", str(spawn_rate), "-t", str(time), "--host", "https://radnet-digital.id",
        "--html", "templates/laporan.html", "--logfile", "logfile.log", "--csv","locust"
    ]

    locust_process = subprocess.Popen(command)

    return jsonify({"status": "program berjalan"})
    
@app.route("/log", methods=["GET"])
def log():
    csv_file = "locust_stats.csv"

    if not os.path.exists(csv_file):
        return jsonify({"status": "menunggu", "data": []})

    dataStats = []

    with open (csv_file, mode="r", encoding="utf-8") as file:
        cvs_reader = csv.DictReader(file)
    
        for baris in cvs_reader:
            dataStats.append(baris)

    return jsonify({"status": "testing", "data": dataStats})

@app.route("/stop", methods=["POST"])
def stop():
    global locust_process

    if locust_process is not None:
        locust_process.terminate()

    return jsonify({"status": "program selesai"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)