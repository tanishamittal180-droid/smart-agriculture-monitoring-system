#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASS";

const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

int soilPin = 34;
int lightPin = 35;

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  client.setServer(mqtt_server, 1883);
}

void reconnect() {
  while (!client.connected()) {
    client.connect("ESP32_FARM");
  }
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }

  client.loop();

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  int soil = analogRead(soilPin);
  int light = analogRead(lightPin);

  String payload = String("{\"temp\":") + temp +
                   ",\"hum\":" + hum +
                   ",\"soil\":" + soil +
                   ",\"light\":" + light + "}";

  client.publish("agri/farm1/sensor", payload.c_str());

  delay(3000);
}