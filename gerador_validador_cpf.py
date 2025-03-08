import random

def gerar_cpf():
    nove_digitos = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    
    contador_regressivo = 10
    resultado_1 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(nove_digitos))
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo = 11
    resultado_2 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(dez_digitos))
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    
    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf_gerado

def validar_cpf(cpf_env_pelo_user):
    if len(cpf_env_pelo_user) != 11 or not cpf_env_pelo_user.isdigit():
        return False
    
    nove_digitos = cpf_env_pelo_user[:9]
    contador_regressivo = 10
    resultado_1 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(nove_digitos))
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    dez_digitos = cpf_env_pelo_user[:10]
    contador_regressivo = 11
    resultado_2 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(dez_digitos))
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    
    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf_env_pelo_user == cpf_gerado

# Gerar um CPF válido
cpf_gerado = gerar_cpf()
print(f'CPF gerado: {cpf_gerado}')

# Validar o CPF gerado
if validar_cpf(cpf_gerado):
    print(f'O CPF {cpf_gerado} é válido.')
else:
    print(f'O CPF {cpf_gerado} é inválido.')

# Validar um CPF específico
cpf_env_pelo_user = '03069897002'
if validar_cpf(cpf_env_pelo_user):
    print(f'O CPF {cpf_env_pelo_user} é válido.')
else:
    print(f'O CPF {cpf_env_pelo_user} é inválido.')import random

def gerar_cpf():
    nove_digitos = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    
    contador_regressivo = 10
    resultado_1 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(nove_digitos))
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo = 11
    resultado_2 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(dez_digitos))
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    
    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf_gerado

def validar_cpf(cpf_env_pelo_user):
    if len(cpf_env_pelo_user) != 11 or not cpf_env_pelo_user.isdigit():
        return False
    
    nove_digitos = cpf_env_pelo_user[:9]
    contador_regressivo = 10
    resultado_1 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(nove_digitos))
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    dez_digitos = cpf_env_pelo_user[:10]
    contador_regressivo = 11
    resultado_2 = sum(int(digito) * (contador_regressivo - i) for i, digito in enumerate(dez_digitos))
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    
    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf_env_pelo_user == cpf_gerado

# Gerar um CPF válido
cpf_gerado = gerar_cpf()
print(f'CPF gerado: {cpf_gerado}')

# Validar o CPF gerado
if validar_cpf(cpf_gerado):
    print(f'O CPF {cpf_gerado} é válido.')
else:
    print(f'O CPF {cpf_gerado} é inválido.')

# Validar um CPF específico
cpf_env_pelo_user = '03069897002'
if validar_cpf(cpf_env_pelo_user):
    print(f'O CPF {cpf_env_pelo_user} é válido.')
else:
    print(f'O CPF {cpf_env_pelo_user} é inválido.')
