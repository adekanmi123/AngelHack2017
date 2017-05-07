#include <string.h>

/// Lights
int ll[3]={2,3,4};
int bl[3]={5,6,7};
int rl[3]={10,9,8};
int fl[3]={13,12,11};

char left='r';
char right='r';
char back='r';
char front='r';

int j=0;
String inputString;
String newstr;

void setup() {
  // put your setup code here, to run once:
for(int i=0; i<=2;i++)
{
  pinMode(ll[i],OUTPUT);
  pinMode(fl[i],OUTPUT);
  pinMode(rl[i],OUTPUT);
  pinMode(bl[i],OUTPUT); 
}
Serial.begin(9600);
}

void loop() {

  if(left == 'r')
  {
    digitalWrite(ll[0],HIGH);
    digitalWrite(ll[1],LOW);
    digitalWrite(ll[2],LOW);
  }
  else if(left == 'y')
  {
    digitalWrite(ll[0],LOW);
    digitalWrite(ll[1],HIGH);
    digitalWrite(ll[2],LOW);
  }
  else if(left == 'g')
  {
    digitalWrite(ll[0],LOW);
    digitalWrite(ll[1],LOW);
    digitalWrite(ll[2],HIGH);
  }
  else 
  {
    digitalWrite(ll[0],LOW);
    digitalWrite(ll[1],LOW);
    digitalWrite(ll[2],LOW);
  }



  if(right == 'r')
  {
    digitalWrite(rl[0],HIGH);
    digitalWrite(rl[1],LOW);
    digitalWrite(rl[2],LOW);
  }
  else if(right == 'y')
  {
    digitalWrite(rl[0],LOW);
    digitalWrite(rl[1],HIGH);
    digitalWrite(rl[2],LOW);
  }
  else if(right == 'g')
  {
    digitalWrite(rl[0],LOW);
    digitalWrite(rl[1],LOW);
    digitalWrite(rl[2],HIGH);
  }
  else 
  {
    digitalWrite(rl[0],LOW);
    digitalWrite(rl[1],LOW);
    digitalWrite(rl[2],LOW);
  }

  if(front == 'r')
  {
    digitalWrite(fl[0],HIGH);
    digitalWrite(fl[1],LOW);
    digitalWrite(fl[2],LOW);
  }
  else if(front == 'y')
  {
    digitalWrite(fl[0],LOW);
    digitalWrite(fl[1],HIGH);
    digitalWrite(fl[2],LOW);
  }
  else if(front == 'g')
  {
    digitalWrite(fl[0],LOW);
    digitalWrite(fl[1],LOW);
    digitalWrite(fl[2],HIGH);
  }
  else 
  {
    digitalWrite(fl[0],LOW);
    digitalWrite(fl[1],LOW);
    digitalWrite(fl[2],LOW);
  }


  if(back == 'r')
  {
    digitalWrite(bl[0],HIGH);
    digitalWrite(bl[1],LOW);
    digitalWrite(bl[2],LOW);
  }
  else if(back == 'y')
  {
    digitalWrite(bl[0],LOW);
    digitalWrite(bl[1],HIGH);
    digitalWrite(bl[2],LOW);
  }
  else if(back == 'g')
  {
    digitalWrite(bl[0],LOW);
    digitalWrite(bl[1],LOW);
    digitalWrite(bl[2],HIGH);
  }
  else 
  {
    digitalWrite(bl[0],LOW);
    digitalWrite(bl[1],LOW);
    digitalWrite(bl[2],LOW);
  }
  
}


void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    inputString=Serial.readStringUntil('}');
    Serial.print(inputString);
    front = inputString[0];
    back = inputString[1];
    left = inputString[2];
    right = inputString[3];
    }
    }

