#include <SoftwareSerial.h>
SoftwareSerial dfPlayer(13, 15); // D7=RX, D8=TX

void playTrack(uint8_t command, uint16_t param) {
  uint8_t packet[10] = {
    0x7E, 0xFF, 0x06, command, 0x00,
    (uint8_t)(param >> 8), (uint8_t)(param & 0xFF),
    0x00, 0x00, 0xEF
  };

  uint16_t checksum = 0 - (packet[1] + packet[2] + packet[3] + packet[4] + packet[5] + packet[6]);
  packet[7] = (uint8_t)(checksum >> 8);
  packet[8] = (uint8_t)(checksum & 0xFF);

  for (int i = 0; i < 10; i++) {
    dfPlayer.write(packet[i]);
  }
}


// ===================== Setup Awal ===========================
void setup() {
  Serial.begin(115200);
  dfPlayer.begin(9600);
  playTrack(0x06, 25);  // Volume
  delay(200);
  playTrack(0x03, 1);  // Mainkan lagu pertama
  delay(1000);
}

void loop() {

}
