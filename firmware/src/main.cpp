#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

#define TRIG 5
#define ECHO 18

#define GREEN_LED 26
#define RED_LED 27
#define BUZZER 25

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

float binHeight = 30.0;

void setup_wifi()
{
    Serial.print("Connecting WiFi ");

    WiFi.begin(ssid,password);

    while(WiFi.status()!=WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nWiFi Connected");
}

void reconnect()
{
    while(!client.connected())
    {
        Serial.println("Connecting MQTT...");

        if(client.connect("SmartBinNode1"))
        {
            Serial.println("MQTT Connected");
        }
        else
        {
            delay(2000);
        }
    }
}

float getDistance()
{
    digitalWrite(TRIG,LOW);
    delayMicroseconds(2);

    digitalWrite(TRIG,HIGH);
    delayMicroseconds(10);

    digitalWrite(TRIG,LOW);

    long duration=pulseIn(ECHO,HIGH);

    float distance=duration*0.034/2;

    return distance;
}

void publishData(float fill)
{
    String status;

    if(fill>=95)
        status="OVERFLOW";
    else if(fill>=80)
        status="FULL";
    else
        status="NORMAL";


    String payload="{";
    payload += "\"bin_id\":\"BIN01\",";
    payload += "\"fill\":" + String(fill,2) + ",";
    payload += "\"status\":\"" + status + "\"";
    payload += "}";

    client.publish(
        "smartbin/data",
        payload.c_str()
    );

    Serial.println(payload);
}

void setup()
{
    Serial.begin(115200);

    pinMode(TRIG,OUTPUT);
    pinMode(ECHO,INPUT);

    pinMode(GREEN_LED,OUTPUT);
    pinMode(RED_LED,OUTPUT);
    pinMode(BUZZER,OUTPUT);

    setup_wifi();

    client.setServer(
        mqtt_server,
        1883
    );
}

void loop()
{
    if(!client.connected())
        reconnect();

    client.loop();

    float distance=getDistance();

    float fill=
    ((binHeight-distance)/binHeight)*100;

    if(fill<0)
        fill=0;

    if(fill>100)
        fill=100;


    if(fill<80)
    {
        digitalWrite(GREEN_LED,HIGH);
        digitalWrite(RED_LED,LOW);
        noTone(BUZZER);
    }
    else
    {
        digitalWrite(GREEN_LED,LOW);
        digitalWrite(RED_LED,HIGH);
        tone(BUZZER,1000);
    }

    publishData(fill);

    delay(5000);
}