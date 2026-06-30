import math
#pegando informaçoes#
print ('Tem que ter a requisição de equipamentos, por favor digite abaixo os equipamentos:')
computadores = switchs = switchsgre = dvrs = impressoras = servidorarq = roteadores = 0

resposta = str(input('Voce deseja usar computadores?')).strip().upper(0)
if resposta == 'sim':
 computadores = int(input('Quantos computadores usará?'))
else:
 pass
resposta1 = str(input('Voce deseja usar switchs?')).strip().upper(0)
if resposta == 'sim':
 switchs = int(input('Quantos cswithcs usará?'))
else:
 pass
resposta2 = str(input('Voce deseja usar switchs gerenciaveis?')).strip().upper(0)
if resposta == 'sim':
 switchsgre = int(input('Quantos usará?'))
else:
 pass
resposta3 = str(input('Voce deseja usar DVR?')).strip().upper(0)
if resposta == 'sim':
 dvrs = int(input('Quantos DVR usará?'))
else:
 pass
resposta4 = str(input('Voce deseja usar impressoras?')).strip().upper(0)
if resposta == 'sim':
 impressoras = int(input('Quantas impressoras usará?'))
else:
 pass
resposta5 = str(input('Voce deseja usar servidores de arquivos?')).strip().upper(0)
if resposta == 'sim':
 servidorarq = int(input('Quantos usará?'))
else:
 pass
resposta6 = str(input('Voce deseja usar roteadores?')).strip().upper(0)
if resposta == 'sim':
 roteadores = int(input('Quantos roteadores usará?'))
else:
 pass
#Fazendo a soma dos componentes para quantidade de conectores RJ45#
cabo1 = computadores * 2
cabo2 = switchs * 2
cabo3 = switchsgre * 2
cabo4 = dvrs * 2 
cabo5 = impressoras * 2
cabo6 = servidorarq * 2
cabo7 = roteadores * 2
#Resposta:#
print ('A quantidade de computadores é {} e a quantidade de conectores para conexão é {}'.format(computadores,cabo1))

print ('A quantidade de switchs é {} e a quantidade de conectores para conexão é {}'.format(switchs,cabo2))

print ('A quantidade de switchs gerenciaveis é {} e a quantidade de conectores para conexão é {}'.format(switchsgre,cabo3))

print ('A quantidade de switchs gerenciaveis é {} e a quantidade de conectores para conexão é {}'.format(dvrs,cabo4))

print ('A quantidade de impressoras que serão utilizados é {} e a qauntidade de conectores necessários é {}'.format(impressoras, cabo5))

print ('A quantidade de servidores que serão utilizados é {} e a quantidade de conectores necessários é {} '.format(servidorarq, cabo6))

print ('A quantidade de roteadores utilizados é {} e a quantidade de conectores necessários {}'.format(roteadores, cabo7))
#Calculando o tamanho da area e distancia dos equipamentos#
area = int(input('Qual é a quantidade de metros quadrados do seu projeto?'))

distancia = int(input('Qual vai ser a distancia entre os equipamentos?'))
total = distancia * computadores * switchs * switchsgre * dvrs * impressoras * servidorarq * roteadores
total1 = total + area
#Dando resposta de acordo com o tamanho da distancie entre os computadores#
if distancia >= 5 and distancia <= 10:
    print ('A area total dos computadores é {}'.format(total1))
elif distancia >= 11 and distancia <= 20:
    print ('A area total dos computadores é {}'.format(total1))
elif distancia >= 21 and distancia <= 30:
    print ('A area total dos computadores é {}'.format(total1))
elif distancia >= 31 and distancia <= 40:
    print ('A area total dos computadores é {}'.format(total1))             
elif distancia >= 41 and distancia <= 50:
    print ('A area total dos computadores é {}'.format(total1))
elif distancia >= 51 and distancia <= 60:
    print ('A area total dos computadores é {}'.format(total1))
elif distancia >= 61 and distancia <= 70:
    print ('A area total dos computadores é {}'.format(total1))             
elif distancia >= 71 and distancia <= 80:
    print ('A area total dos computadores é {}'.format(total1))
elif distancia >= 81 and distancia <= 90:
    print ('A area total dos computadores é {}'.format(total1))
elif distancia >= 91 and distancia <= 100:
    print ('A area total dos computadores é {}'.format(total1))   
#Fazendo o calculo de quantas caixas de cabo de rede serão necessárias para o projeto#
metros = total1
caixas = metros / 305
#resposta#
print ('A área total do seu projeto é de {}m² e irá precisar de {} caixas de cabo de rede'.format(total1,math.ceil(caixas)))




 