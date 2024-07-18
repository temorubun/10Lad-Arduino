

int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
int num_fingers = 0;

void setup() {
    Serial.begin(9600);
    for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
    }
    Serial.println("Arduino is ready");
}

void loop() {
    if (Serial.available() > 0) {
        num_fingers = Serial.parseInt();
        Serial.print("Received fingers: ");
        Serial.println(num_fingers);
        controlLEDs(num_fingers);
    }
}

void controlLEDs(int num) {
    for (int i = 0; i < 10; i++) {
        if (i < num) {
            digitalWrite(ledPins[i], HIGH);
        } else {
            digitalWrite(ledPins[i], LOW);
        }
    }
}
