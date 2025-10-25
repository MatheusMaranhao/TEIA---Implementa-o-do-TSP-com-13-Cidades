import random

# -----------------------------------------------------------------
# DADOS DO PROBLEMA (A instância USA13)
# -----------------------------------------------------------------

# Nomes das cidades (só pra gente saber quem é quem)
# 0: New York, 1: Los Angeles, 2: Chicago, 3: Minneapolis, 
# 4: Denver, 5: Dallas, 6: Seattle, 7: Boston, 8: San Francisco,
# 9: St. Louis, 10: Houston, 11: Phoenix, 12: Salt Lake City

# Essa matriz é o nosso "mapa". 
# Ex: USA13[0][1] é a distância de New York (0) até Los Angeles (1)
USA13 = [
    [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
    [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
    [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
    [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
    [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
    [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
    [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
    [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
    [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
    [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
    [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
    [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
    [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
]

N_CIDADES = 13 # O número total de cidades que temos que visitar

# -----------------------------------------------------------------
# TAREFA 1: FUNÇÃO DE VALIDAÇÃO
# -----------------------------------------------------------------

def is_valid_route(route):
    """
    Checa se uma rota (cromossomo) é válida.
    Precisa ter 13 cidades e visitar cada uma (0 a 12) só uma vez.
    """
    
    # 1. A rota tem o número certo de cidades?
    if len(route) != N_CIDADES:
        # print("Rota inválida: tamanho errado!")
        return False
        
    # 2. A rota tem cidades duplicadas?
    # Um truque fácil: 'set' é um tipo de lista que NÃO permite duplicados.
    # Se o tamanho do 'set' da rota for igual ao tamanho da lista da rota,
    # quer dizer que não tinha nenhuma cidade duplicada.
    if len(set(route)) != N_CIDADES:
        # print("Rota inválida: tem cidades repetidas!")
        return False
        
    # Se passou nos dois testes, a rota é boa.
    return True

# -----------------------------------------------------------------
# TAREFA 2: FUNÇÃO DE FITNESS (CÁLCULO DE DISTÂNCIA)
# -----------------------------------------------------------------

def calculate_total_distance(route):
    """
    Calcula a distância total de uma rota.
    Essa é a nossa função de fitness.
    """
    
    # Zera o odômetro
    total_distance = 0
    
    # Vamos somar cada "perna" da viagem
    # O loop vai de 0 até 11 (N_CIDADES - 1)
    for i in range(N_CIDADES - 1):
        # Pega a cidade atual e a próxima
        cidade_atual = route[i]
        proxima_cidade = route[i+1]
        
        # Olha no "mapa" (matriz) qual a distância
        distancia = USA13[cidade_atual][proxima_cidade]
        
        # Soma na distância total
        total_distance += distancia
        
    # Beleza, o loop terminou. 
    # Falta somar a última parte: a volta da última cidade para a primeira.
    
    cidade_final = route[-1]     # Pega o último item da lista
    cidade_inicial = route[0]    # Pega o primeiro item
    
    # Pega a distância da volta
    distancia_final = USA13[cidade_final][cidade_inicial]
    
    # Soma também
    total_distance += distancia_final
    
    return total_distance

# -----------------------------------------------------------------
# BLOCO DE TESTES (só pra ver se funciona)
# -----------------------------------------------------------------

# Isso aqui só roda se a gente executar esse arquivo direto
if __name__ == "__main__":
    
    print("--- Teste de Validação ---")
    
    # Rota simples, só pra testar
    rota_valida_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(f"Rota 1 é válida? {is_valid_route(rota_valida_1)}")
    
    # Rota embaralhada, mais realista
    rota_valida_2 = [0, 8, 5, 2, 11, 1, 12, 3, 6, 9, 10, 4, 7]
    print(f"Rota 2 é válida? {is_valid_route(rota_valida_2)}")

    # Inválida (repetiu a cidade 11)
    rota_invalida_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
    print(f"Rota 3 é válida? {is_valid_route(rota_invalida_1)}")

    # Inválida (curta demais)
    rota_invalida_2 = [0, 1, 2, 3, 4]
    print(f"Rota 4 é válida? {is_valid_route(rota_invalida_2)}")
    
    print("\n--- Teste de Fitness (Distância) ---")
    
    distancia_1 = calculate_total_distance(rota_valida_1)
    print(f"Distância da Rota 1 (em ordem): {distancia_1} milhas")
    
    distancia_2 = calculate_total_distance(rota_valida_2)
    print(f"Distância da Rota 2 (embaralhada): {distancia_2} milhas")

    # Nosso objetivo com o AG vai ser MINIMIZAR esse número.
    # A rota 2 (embaralhada) é muito pior que a rota 1 (em ordem).
    # (Isso é só coincidência, na maioria dos problemas a ordem 0,1,2... não é a melhor)