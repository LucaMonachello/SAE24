import paho.mqtt.client as mqtt
from datetime import datetime
from MySQLdb import _mysql
from MySQLdb._exceptions import OperationalError
import csv

csv_filename = "donnees_MQTT.csv"

try:
    db = _mysql.connect("127.0.0.1", "root", "toto", "gr6")
except OperationalError:
    db = _mysql.connect("127.0.0.1", "root", "toto")
    db.query("CREATE DATABASE gr6")
    db.query("USE gr6")

db.ping(True)

db.query("""
CREATE TABLE IF NOT EXISTS gr6.capteur (
    id INT NOT NULL AUTO_INCREMENT,
    address VARCHAR(12) NOT NULL UNIQUE,
    piece VARCHAR(50) NOT NULL,
    emplacement VARCHAR(50),
    nom VARCHAR(50),
    PRIMARY KEY (id))
""")

db.query("""
CREATE TABLE IF NOT EXISTS gr6.capteur_data (
    id INT NOT NULL AUTO_INCREMENT,
    capteur_id INT NOT NULL,
    FOREIGN KEY (capteur_id) REFERENCES capteur(id),
    datetime DATETIME NOT NULL,
    temp DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (id))
""")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("IUT/Colmar2023/SAE2.04/Maison1")

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    data = message.split(",")

    # Extraction des données
    ID = data[0]
    PIECE = data[1]
    DATE = data[2]
    TIME = data[3]
    TEMP = data[4]

    # Enregistrement dans le fichier CSV
    with open(csv_filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ID, PIECE, DATE, TIME, TEMP])

    

    payload = str(msg.payload)[2:-1].split(",")
    mac_addr = payload[0].split("=")[1]
    piece = payload[1].split("=")[1]
    dt = datetime.strptime(payload[2].split("=")[1] + " " + payload[3].split("=")[1], '%d/%m/%Y %H:%M:%S')
    temp = payload[4].split("=")[1]

    try:
        db.query(f"INSERT INTO capteur (address, piece) VALUES ('{mac_addr}', '{piece}')")
    except Exception:
        pass

    db.query(f"SELECT id FROM capteur WHERE address='{mac_addr}'")
    id = int(db.store_result().fetch_row()[0][0])

    sql_data = f"INSERT INTO capteur_data (capteur_id, datetime, temp) VALUES ({id}, '{dt.strftime('%Y-%m-%d %H:%M:%S')}', {temp})"
    print(sql_data)

    reachable = True
    try:
        db.query(sql_data)
        reachable = True
    except Exception:
        reachable = False


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", port=1883, keepalive=60)

client.loop_forever()