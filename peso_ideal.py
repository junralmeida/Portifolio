#função 'calcular_peso_ideal' com parametro (altura, sexo, kg)

def calcular_peso_ideal(altura, sexo, kg): 

    #criando uma condição com informação dada pelo usiário sobre o sexo 
    # e de acordo com o informado, criada uma variável com calculo do peso ideal 
    
    if sexo.lower() == 'homem': 
        imc =  kg / (altura * 2)
        peso_ideal = 65.2 - (0.75 * altura) 
        print(f'Seu IMC é: {imc:.2f} kg o peso ideal para um homem com {altura}m é {peso_ideal:.2f}')
    elif sexo.lower() == 'mulher':
        imc = kg / (altura * 2)
        peso_ideal = 56.25 - (0.675 * altura) 
        print(f'Seu IMC é: {imc:.2f} kg o peso ideal para uma mulher com {altura}m é {peso_ideal:.2f}')
    else:
        print('Sexo não reconhecido. Por favor, insira "homem" ou "mulher".')

altura = float(input('Digite a altura em metros: '))
kg = float(input('Digite seu peso: '))
sexo = input('Digite o sexo (homem/mulher): ')

calcular_peso_ideal(altura, sexo, kg)