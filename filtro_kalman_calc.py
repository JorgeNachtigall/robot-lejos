from math import sqrt

def calcula_media(medidas):

    media = 0
	
    for medida in medidas:
	    media = media + medida
		
    media = media/30.0
	
    return media

def calcula_variancia(media, medidas):
    soma_geral = 0.0
	
    for medida in medidas:
	    soma_geral = soma_geral + (media - medida)**2

		
    return soma_geral/30
	
def calcula_desvio_padrao(variancia):
	
    return sqrt(variancia)

def ganho_kalman(variancia_cor, variancia_ultra):

    ganho = variancia_cor**2 / (variancia_ultra**2 + variancia_cor**2)

    return ganho

def main():
    
    media_ultra = 0.0
    variancia_ultra = 0.0
    desvio_padrao_ultra = 0.0
    medidas_ultra = [99.0, 99.0, 98.1, 97.6, 98.9, 99.2, 100.3, 98.2, 98.7, 99.3, 100, 99.1, 99.4, 100.2, 100.3, 99.8, 98.7, 98.5, 100.0, 99.4, 98.6, 99.7, 99.5, 99.2, 99.0, 99.6, 99.4, 100.5, 98.9, 99.3]

    media_cor = 0.0
    variancia_cor = 0.0
    desvio_padrao_cor = 0.0
    medidas_cor = [104.0, 101.0, 103.4, 106.0, 105.5, 101.5, 108.4, 114.5, 104.4, 109.0, 117.8, 111.6, 105.5, 114.2, 102.0, 112.0, 101.9, 100.9, 103.5, 109.1, 103.8, 108.3, 105.3, 100.9, 100.3, 105.5, 98.7, 101.5, 103.6, 104.4]

    media_ultra = calcula_media(medidas_ultra)
    variancia_ultra = calcula_variancia(media_ultra, medidas_ultra)
    desvio_padrao_ultra = calcula_desvio_padrao(variancia_ultra)

    media_cor = calcula_media(medidas_cor)
    variancia_cor = calcula_variancia(media_cor, medidas_cor)
    desvio_padrao_cor = calcula_desvio_padrao(variancia_cor)

    ganho = ganho_kalman(variancia_cor, variancia_ultra)
	
    print("\n\n")
    print("Media Ultra Sensor: {} \n".format(media_ultra))
    print("Variancia Ultra Sensor: {} \n".format(variancia_ultra))
    print("Desvio Padrao Ultra Sensor: {} \n".format(desvio_padrao_ultra))

    print("\n\n")
    print("Media Color Sensor: {} \n".format(media_cor))
    print("Variancia Color Sensor: {} \n".format(variancia_cor))
    print("Desvio Padrao Color Sensor: {} \n".format(desvio_padrao_cor))

    print("\n\n")
    print("Ganho de Kalman: {}".format(ganho))
	
main()