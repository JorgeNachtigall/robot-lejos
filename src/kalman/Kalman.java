package kalman;

import lejos.nxt.*;
import lejos.nxt.ColorSensor.Color;

//1 pretinho = 1.05cm

public class Kalman {
	public static void main(String[] args) {
		UltrasonicSensor usensor = new UltrasonicSensor(SensorPort.S1);
		ColorSensor colorSensor = new ColorSensor(SensorPort.S4);
		int blackCounter = 0;
		double filtroKalman = 0;
		int distancia = 0;
		int aux_kalman = 0;

		while ( filtroKalman <= 100 ) {
			
			Motor.A.setSpeed(300);
			Motor.C.setSpeed(300);
			Motor.A.backward();
			Motor.C.backward();
			
			distancia = usensor.getDistance();
			
			if (colorSensor.getColorID() == Color.BLACK) {
				while(colorSensor.getColorID() == Color.BLACK);
				blackCounter++;
			}
			
			filtroKalman = (0.9995 * distancia) + ((1 - 0.995) * (blackCounter * 1.05));
			
			aux_kalman = (int) filtroKalman;
			
			LCD.drawInt(blackCounter, 0, 1);
			LCD.drawInt(distancia, 0, 2);
			LCD.drawInt(aux_kalman, 0, 3);
		}
	}

}
