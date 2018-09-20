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
	
def main():
    
    media = 0.0
    variancia = 0.0
    desvio_padrao = 0.0
    medidas = [99.0, 99.0, 98.1, 97.6, 98.9, 99.2, 100.3, 98.2, 98.7, 99.3, 100, 99.1, 99.4, 100.2, 100.3, 99.8, 98.7, 98.5, 100.0, 99.4, 98.6, 99.7, 99.5, 99.2, 99.0, 99.6, 99.4, 100.5, 98.9, 99.3]
	
    media = calcula_media(medidas)
    variancia = calcula_variancia(media, medidas)
    desvio_padrao = calcula_desvio_padrao(variancia)
	
    print("\n\n")
    print("Media: {} \n".format(media))
    print("Variancia: {} \n".format(variancia))
    print("Desvio Padrao: {} \n".format(desvio_padrao))
	
main()