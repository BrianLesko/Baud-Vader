int relay_1 = 4;

void setup() {
  Serial.begin(9600);
  pinMode(relay_1, OUTPUT);
  pinMode(13,OUTPUT);
  digitalWrite(13,HIGH); // for supplying test power to the relay
}

void loop() {
  if (Serial.available() > 0){
    //Receive data
    String incomingData = Serial.readStringUntil('\n');

    // Print received Data
    Serial.print("Received: ");
    Serial.println(incomingData);

    if (incomingData == "ON"){
      // write to relay, high
      digitalWrite(relay_1, HIGH);
    }
    if (incomingData == "OFF"){
      // write to relay, high
      digitalWrite(relay_1, LOW);
    }
  }
}
