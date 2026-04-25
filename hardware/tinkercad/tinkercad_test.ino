int trig = 9;
int echo = 10;

int green = 6;
int red = 7;
int buzzer = 8;

float binHeight = 30.0;

/*
Hysteresis state:
prevents LED/buzzer flickering
around threshold.
*/
bool binFull = false;

void setup()
{
Serial.begin(9600);

pinMode(trig,OUTPUT);
pinMode(echo,INPUT);

pinMode(green,OUTPUT);
pinMode(red,OUTPUT);
pinMode(buzzer,OUTPUT);
}

void loop()
{

// Trigger ultrasonic pulse
digitalWrite(trig,LOW);
delayMicroseconds(2);

digitalWrite(trig,HIGH);
delayMicroseconds(10);

digitalWrite(trig,LOW);


// Read echo
long duration =
pulseIn(echo,HIGH);


// Distance in cm
float distance =
duration * 0.034 / 2;


// Fill percentage
float fill =
((binHeight-distance)/binHeight)*100;


// Safety bounds
if(fill<0)
fill=0;

if(fill>100)
fill=100;


// Print readings
Serial.print("Distance: ");
Serial.print(distance);

Serial.print(" cm   Fill: ");
Serial.print(fill);

Serial.println("%");



/*
HYSTERESIS LOGIC

Trigger full at 80%
Return normal only below 75%
*/

if(fill>=80)
{
binFull=true;
}

if(fill<=75)
{
binFull=false;
}



// Device actions
if(!binFull)
{
digitalWrite(green,HIGH);
digitalWrite(red,LOW);

noTone(buzzer);
}

else
{
digitalWrite(green,LOW);
digitalWrite(red,HIGH);

tone(buzzer,1000);
}


delay(1000);

}