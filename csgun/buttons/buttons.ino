
void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  Serial.begin(9600);

}

int buttonState2 = 0;

int buttonState3 = 0;
int printCount = 0;

bool canClick = false;
bool canMove = false;
bool hasPrint = false;

void loop() {
  // read the state of the pushbutton value:
 
  if(buttonState2 != digitalRead(2))
  {
     buttonState2 = digitalRead(2);
//     Serial.println(buttonState2);
    }
     buttonState3 = digitalRead(3);
  // Show the state of pushbutton on serial monitor
  
  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState2 == LOW && canClick == false) 
 {
   canClick = true;
   
   
  } 
   if (canClick == true && buttonState2 == HIGH && printCount == 1) 
  {
   canClick = false;
   printCount = 0;
   
  } 
  
 if(canClick == true && printCount < 1)
  {
   
   printCount ++;
   hasPrint = true;
   Serial.println("leftclick");
   }
  
  if (buttonState3 == LOW && canMove == true) 
  {
   Serial.println("ADS");
   canMove = false;
  } 
  
   if (buttonState3 != LOW && canMove == false) 
  {
    Serial.println("STOPADS");
   canMove = true;
  } 

  
}
