int trig = 9;
int echo = 10;

int green = 6;
int red = 7;
int buzzer = 8;

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

// Trigger sensor
digitalWrite(trig,LOW);
delayMicroseconds(2);

digitalWrite(trig,HIGH);
delayMicroseconds(10);

digitalWrite(trig,LOW);


// Read distance
long duration =
pulseIn(echo,HIGH);

float distance=
duration*0.034/2;


// Print reading
Serial.print("Distance: ");
Serial.print(distance);
Serial.println(" cm");



/*
STATE 1
Empty/Normal
*/
if(distance > 20)
{
digitalWrite(green,HIGH);
digitalWrite(red,LOW);

noTone(buzzer);

Serial.println("STATUS: NORMAL");
}


/*
STATE 2
Warning
*/
else if(distance > 10)
{
digitalWrite(green,LOW);
digitalWrite(red,HIGH);

noTone(buzzer);

Serial.println("STATUS: WARNING");
}


/*
STATE 3
Overflow
*/
else
{
digitalWrite(green,LOW);
digitalWrite(red,HIGH);

tone(buzzer,1000);

Serial.println("STATUS: OVERFLOW");
}

Serial.println("----------------");

delay(1000);

}