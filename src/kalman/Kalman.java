package kalman;

import lejos.nxt.*;

public class Kalman {
	public static void main(String[] args) {
		UltrasonicSensor usensor = new UltrasonicSensor(SensorPort.S1);
		usensor.continuous();
		int distance = 0;

		while (distance < 101) {
			distance = usensor.getDistance();
			LCD.drawInt(distance, 0, 1);
			Motor.A.setSpeed(100);
			Motor.C.setSpeed(100);
			Motor.A.backward();
			Motor.C.backward();
		}
	}

}
