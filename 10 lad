int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

void setup() {
    for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
    }
}

void loop() {
    // Turn on LEDs one by one
    for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], HIGH);
        delay(100);  // Wait for half a second
    }
    // Turn off LEDs one by one
    for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], LOW);
        delay(100);  // Wait for half a second
    }
}
