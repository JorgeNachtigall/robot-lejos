// somente transcrevi o que fizemos para ter guardado e iniciarmos o git, mas esse arquivo nem será usado,
// portanto não se preocupem com detalhes, como o nome do package por exemplo.

package roboTOP;

import lejos.nxt.*;

public class caminhar {

    public static void main(String[] args) {
        UltrasonicSensor usensor = new UltrasonicSensor(SensorPort.S1);

        while (usensor.getDistance() < 254) {
            LCD.drawInt(usensor.getDistance(), 0, 3);
            Motor.A.setSpeed(720);
            Motor.C.setSpeed(720);
            Motor.A.forward();
            Motor.C.forward();
            LCD.drawString("HASTA LA VISTA", 0, 4);
        }

    }

}