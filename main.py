
#CÓDIGO BASE!!!!!!!!!!!!!!!!!!!!!!!!!#


#def iniciar_jogo():
import pickle
import random
import sys
import time

print("Feito por:\nPedro Gonella Barão e \nLorenzo Vincentin")

def iniciar_jogo():
    print("-------------------------------")
    print("|          Bem-vindo          |")
    print("|        à aventura RPG       |")
    print("-------------------------------")
    print("\n")

    nome = input("Digite o nome do seu personagem: ").strip()
    regioes = ["Floresta 🌲", "Deserto 🏜️", "Mar 🌊", "Montes Nevados ❄️", "Entrada do Reino 🏰", "Dentro do Castelo 🏰"]
    jogo = {}  # Pode ser um dicionário ou outro objeto que gerencie o estado do jogo

    jogador = Jogador(nome, regioes)  # Cria uma instância do jogador
    jogador.escolher_classe(regioes, jogo)  # Chama o método para o jogador escolher a classe


class Jogador:
    def __init__(self, nome, regioes, ouro=10, xp=0, xp_up=50, sp=10, regiao_atual=0):
        self.nome = nome
        self.vida = 0
        self.vida_máxima = 0
        self.ouro = ouro
        self.xp = xp
        self.sp = sp
        self.regioes = regioes
        self.regiao_atual = regiao_atual
        self.sp_máximo = 0
        self.classe = None
        self.nivel = 1
        self.xp_up = xp_up
        self.ataque_base = 0
        self.defesa_base = 0
        self.habilidades = {}
        self.armadura_ativa = False
        self.vida_extra = 0
        self.inventario = []
        self.equipamentos = {"arma": None, "armadura": None}
        self.ataque_temporario = 0
        self.defesa_temporaria = 0
        self.amigo_da_floresta_ativo = False
        self.tipo = None

class Jogador:
    def __init__(self, nome, regioes, ouro=10, xp=0, xp_up=50, sp=10, regiao_atual=0):
        self.nome = nome
        self.vida = 0
        self.vida_máxima = 0
        self.ouro = ouro
        self.xp = xp
        self.sp = sp
        self.regioes = regioes
        self.regiao_atual = regiao_atual
        self.sp_máximo = 0
        self.classe = None
        self.nivel = 1
        self.xp_up = xp_up
        self.ataque_base = 0
        self.defesa_base = 0
        self.habilidades = {}
        self.armadura_ativa = False
        self.vida_extra = 0
        self.inventario = []
        self.equipamentos = {"arma": None, "armadura": None}
        self.ataque_temporario = 0
        self.defesa_temporaria = 0
        self.amigo_da_floresta_ativo = False
        self.tipo = None

    def escolher_classe(self, regioes, jogo):
        """
        Método para o jogador escolher sua classe e configurar atributos iniciais.
        """
        opcoes_classe = {
            "1": {"nome": "Guerreiro", "ataque": 10, "defesa": 15, "vida": 100, "sp": 10},
            "2": {"nome": "Assassino", "ataque": 20, "defesa": 5, "vida": 50, "sp": 10},
            "3": {"nome": "Arqueiro", "ataque": 15, "defesa": 10, "vida": 75, "sp": 10},
        }

        while True:
            print("Escolha sua classe:")
            for key, classe in opcoes_classe.items():
                print(f"{key}) {classe['nome']} - Ataque: {classe['ataque']}, Defesa: {classe['defesa']}, "
                      f"Vida: {classe['vida']}, SP: {classe['sp']}")

            escolha = input("Digite o número correspondente à sua classe: ").strip()

            if escolha in opcoes_classe:
                classe_escolhida = opcoes_classe[escolha]
                self.classe = classe_escolhida["nome"]
                self.vida = classe_escolhida["vida"]
                self.vida_máxima = classe_escolhida["vida"]
                self.sp = classe_escolhida["sp"]
                self.sp_máximo = classe_escolhida["sp"]
                self.ataque_base = classe_escolhida["ataque"]
                self.defesa_base = classe_escolhida["defesa"]
                print(f"🎖️ Você escolheu a classe {self.classe}!")
                self.exibir_status()
                menu(self, regioes, jogo)  # Direciona para o menu após escolher a classe
                break
            else:
                print("❌ Escolha inválida. Tente novamente.")

    def exibir_status(self):
        """
        Exibe os atributos atuais do jogador.
        """
        print(
            f"{self.nome} - ❤️ Vida: {self.vida}/{self.vida_máxima}, ⚡ Energia: {self.sp}/{self.sp_máximo}, "
            f"Classe: {self.classe}, 🗡️ Ataque: {self.ataque_base}, 🛡️ Defesa: {self.defesa_base}, "
            f"🪙 Ouro: {self.ouro}, 🎖️ Nível: {self.nivel}, XP: {self.xp}/{self.xp_up}"
        )



def usar_habilidade(self, inimigo):
    habilidades_disponiveis = [
        (nome, funcao, custo)
        for nivel, habilidades in self.habilidades.items()
        if self.nivel >= nivel
        for nome, funcao, custo in habilidades
    ]
    if not habilidades_disponiveis:
        print("Nenhuma habilidade disponível no momento.")
        return

    print("Escolha uma habilidade:")
    for i, (nome, _, custo) in enumerate(habilidades_disponiveis, 1):
        print(f"{i}) {nome} (Custo: {custo} SP)")

    try:
        escolha = int(input("Número: ")) - 1
        nome, funcao, sp_custo = habilidades_disponiveis[escolha]
        if self.sp >= sp_custo:
            self.sp -= sp_custo
            funcao(inimigo)
        else:
            print("SP insuficiente para usar essa habilidade!")
    except (ValueError, IndexError):
        print("Escolha inválida.")

@property
def ataque(self):
    return self.ataque_base + self.ataque_temporario

@property
def defesa(self):
    return self.defesa_base + self.defesa_temporaria

def atacar(self, inimigo, chefe):
    dano = max(self.ataque + random.randint(1, 5) - inimigo.defesa, 0)
    inimigo.vida -= dano
    print(f"{self.nome} ataca {inimigo.nome}, causando {dano} de dano!")

# Exemplos de habilidades
def corte_rapido(self, inimigo):
    print(f"{self.nome} usa Corte Rápido! ⚔️")
    dano = max(int(self.ataque * 1.5 + random.randint(1, 5) - inimigo.defesa), 0)
    inimigo.vida -= dano
    print(f"{inimigo.nome} recebeu {dano} de dano!")


def rugido_de_guerra(self, inimigo):
 if hasattr(self, 'rugido_ativo') and self.rugido_ativo:
    print("A habilidade já está ativa!")
    return  # Sai da função sem aplicar o efeito novamente

 print(f"{self.nome} usa Rugido de Guerra! 💪")
 inimigo.defesa -= 3  # Reduz a defesa do inimigo
 print(f"A defesa de {inimigo.nome} foi reduzida em 3!")
 self.rugido_ativo = True  # Marca a habilidade como ativa


def super_armadura(self, inimigo):
    print(f"{self.nome} usa Super Armadura! 🛡️")
    if not self.armadura_ativa:  # Verifica se a armadura já está ativa
        self.armadura_ativa = True
        self.vida_extra = 25  # Vida extra concedida pela barreira
        self.vida += self.vida_extra  # Adiciona a vida extra ao total de vida
        print(f"{self.nome} ganhou {self.vida_extra} pontos de vida extras! Vida atual: {self.vida}.")
    else:
        print("A Super Armadura já está ativa!")

def aplicar_dano(self, dano):
    if self.armadura_ativa:
        # Verifica se a vida extra está presente e se o dano não excede a vida extra
        if self.vida_extra > 0:
            if dano < self.vida_extra:
                self.vida_extra -= dano  # Reduz o valor da vida extra
                dano = 0  # Nenhum dano é absorvido pela vida normal
            else:
                # Caso o dano seja maior que a vida extra, subtraímos o restante da vida normal
                dano -= self.vida_extra
                self.vida_extra = 0  # A vida extra foi consumida
                self.armadura_ativa = False  # Desativa a armadura
                print(f"A Super Armadura foi desativada, pois a vida extra foi consumida.")

    # Aplica o dano ao personagem, levando em conta que a armadura pode estar desativada
    self.vida -= dano
    print(f"{self.nome} recebeu {dano} de dano! Vida atual: {self.vida}")

def golpe_fatal(self, inimigo):
    print(f"{self.nome} usa Golpe Fatal! ⚡")
    dano_bruto = int(self.ataque * 2 + random.randint(1, 5) - inimigo.defesa)  # Dano dobrado para esse ataque
    dano = max(dano_bruto, 0)
    inimigo.vida -= dano
    print(f"{inimigo.nome} recebeu {dano} de dano!")

def passo_sombrio(self, inimigo):
 if hasattr(self, 'passo_sombrio_ativo') and self.passo_sombrio_ativo:
    print("A habilidade já está ativa!")
    return  # Sai da função se já estiver ativa

 print(f"{self.nome} usa Passo Sombrio! 🖤")
 sucesso_fuga = random.random() < 0.5  # Aumenta as chances de fugir
 if sucesso_fuga:
    print(f"{self.nome} conseguiu fugir com sucesso!")
    self.passo_sombrio_ativo = True  # Marca como usada
    return True  # Indica que o jogador fugiu com sucesso
 else:
    print(f"{self.nome} não conseguiu fugir.")
    self.passo_sombrio_ativo = True  # Marca como usada
    return False


def rasgo_de_bolso(self, inimigo):
 if hasattr(self, 'rasgo_ativo') and self.rasgo_ativo:
    print("A habilidade já está ativa!")
    return  # Impede o uso da habilidade novamente

 print(f"{self.nome} usa Rasgo de Bolso! 🕴️")
 dano_bruto = int(self.ataque * 1.5 + random.randint(1, 5) - inimigo.defesa)
 dano = max(dano_bruto, 0)  # Garante que o dano não seja negativo
 inimigo.vida -= dano

 ouro = random.randint(5, 30)  # Determina a quantidade de ouro roubado
 self.ouro += ouro  # Adiciona ao ouro do jogador
 print(f"{inimigo.nome} recebeu {dano} de dano! {self.nome} roubou {ouro} moedas!")

 self.rasgo_ativo = True

def tiro_precisao(self, inimigo):
    print(f"{self.nome} usa Tiro Precisão! 🎯")
    dano_bruto = int(self.ataque * 1.3 + random.randint(1, 5) - inimigo.defesa)
    dano = max(dano_bruto, 0)
    inimigo.vida -= dano
    print(f"{inimigo.nome} recebeu {dano} de dano preciso! Vida atual: {inimigo.vida}")

def flecha_explosiva(self, inimigo):
    print(f"{self.nome} usa Flecha Explosiva! 💥")
    dano_bruto = int(self.ataque * 2 + random.randint(1, 5) - inimigo.defesa)
    dano = max(dano_bruto, 0)
    inimigo.vida -= dano
    print(f"{inimigo.nome} recebeu {dano} de dano explosivo! Vida atual: {inimigo.vida}")

def amigo_da_floresta(self, inimigo):
 print(f"{self.nome} usa Amigo da Floresta! 🌳")
# Aumenta a chance de poupar o inimigo
 sucesso_poupar = random.random() < 0.5  # 50% de chance de poupar o inimigo

 if sucesso_poupar:
    self.amigo_da_floresta_ativo = True  # Habilidade ativa quando tiver sucesso
    print(f"{self.nome} conseguiu poupar {inimigo.nome}!")
    item = inimigo.drop_aleatorio()
    if item:
        self.inventario.append(item)
        print(f"O inimigo deixou {item['nome']} para trás.")
    else:
        print(f"{inimigo.nome} não tinha itens especiais para poupar.")
    return True  # Retorna True para encerrar a batalha
 else:
    print(f"{self.nome} não conseguiu poupar {inimigo.nome}.")
    self.amigo_da_floresta_ativo = False  # Habilidade inativa quando não tiver sucesso
    return False  # Retorna False para a batalha continuar




def comprar_item(self, item):
 if 'valor_compra' not in item:
    print(f"❌ O item '{item['nome']}' não possui o atributo 'valor_compra'.")
    return

 if item['valor_compra'] <= self.ouro:
    self.ouro -= item['valor_compra']
    self.inventario.append(item)
    print(f"✅ Você comprou {item['nome']}!")
 else:
    print("❌ Você não tem ouro suficiente para comprar este item.")



def vender_item(self):
   if not self.inventario:
     print("❌ Você não possui itens para vender.")
     return

   print("⬇️ Escolha um item para vender ⬇️:")
   for idx, item in enumerate(self.inventario):
     valor_venda = item.get("valor_venda", "N/A")
     print(f"{idx + 1}) {item['nome']} - Valor de venda: {valor_venda} moedas")

   try:
      escolha = int(input("Digite o número do item que deseja vender: ")) - 1
      if escolha < 0 or escolha >= len(self.inventario):
        print("❌ Escolha inválida.")
        return

      item_escolhido = self.inventario[escolha]
      if "valor_venda" not in item_escolhido:
        print(f"❌ O item '{item_escolhido['nome']}' não pode ser vendido (atributo 'valor_venda' ausente).")
        return

      self.ouro += item_escolhido["valor_venda"]
      print(f"✅ Você vendeu {item_escolhido['nome']} por {item_escolhido['valor_venda']} moedas!")
      self.inventario.pop(escolha)

   except ValueError:
    print("❌ Entrada inválida. Por favor, digite um número.")



def usar_item(self):
    itens_usaveis = [item for item in self.inventario if item['tipo'] == 'usavel']
    if not itens_usaveis:
        print("❌ Você não possui itens usáveis.")
        return

    print("⬇️ Escolha um item para usar ⬇️:")
    for idx, item in enumerate(itens_usaveis):
        print(f"{idx + 1}) {item['nome']} - {item['descricao']}")
    escolha = int(input("Número do item: ")) - 1
    if 0 <= escolha < len(itens_usaveis):
     item = itens_usaveis[escolha]
     if item['nome'] == "Poção de Vida Pequena ❣️":
      self.vida += item['efeito']
      print(f"Você usou {item['nome']} e recuperou {item['efeito']} pontos de vida 🧫")
      self.inventario.remove(item)
     elif item['nome'] == "Poção de Força 💪":
      self.ataque_temporario += item['efeito']
      print(f"Você usou {item['nome']} e aumentou seu ataque em {item['efeito']} pontos para esta batalha 🧪")
      self.inventario.remove(item)
     elif item['nome'] == "Poção de Resistência 🛡️":
      self.defesa_temporaria += item['efeito']
      print(f"Você usou {item['nome']} e aumentou sua defesa em {item['efeito']} pontos para esta batalha 🧪")
      self.inventario.remove(item)
     elif item['nome'] == "Poção de Vida Grande ❣️":
      self.vida += item['efeito']
      print(f"Você usou {item['nome']} e recuperou {item['efeito']} pontos de vida 🧫")
      self.inventario.remove(item)
    else:
     print("❌ Escolha inválida! Certifique-se de escolher um número válido.")



def resetar_bonus_temporarios(self):
    self.ataque_temporario = 0
    self.defesa_temporaria = 0

def equipar_item(self):
# Filtra os itens de tipo 'equipavel' no inventário
 equipamentos = [item for item in self.inventario if item['tipo'] == 'equipavel']

 if not equipamentos:
    print("❌ Você não possui equipamentos para equipar.")
    return

 print("Escolha um equipamento para usar:")
 for idx, item in enumerate(equipamentos):
    print(f"{idx + 1}) {item['nome']} - {item['descricao']} (Exclusivo para: {item['classe_exclusiva']})")

 escolha = int(input("Número do equipamento: ")) - 1
 if 0 <= escolha < len(equipamentos):
    item = equipamentos[escolha]

    # Permite equipar o item se a classe do jogador corresponder ou se o item for para "todos"
    if item['classe_exclusiva'] != self.classe and item['classe_exclusiva'] != "todas as classes":
        print(f"❌ {self.nome}, você não pode equipar {item['nome']} pois é exclusivo para a classe {item['classe_exclusiva']}.")
        return

    # Remove o item do inventário e equipa o item na categoria apropriada
    self.inventario.remove(item)  # Usa 'self.inventario' em vez de 'equipamentos'
    self.equipamentos[item['categoria']] = item

    # Ajusta os atributos do jogador de acordo com o item equipado
    if item['categoria'] == 'arma':
        self.ataque_base += item['efeito']
        print(f"✅ Você equipou {item['nome']} e aumentou seu ataque em {item['efeito']} ⬆️")
    elif item['categoria'] == 'armadura':
        self.defesa_base += item['efeito']
        print(f"✅ Você equipou {item['nome']} e aumentou sua defesa em {item['efeito']} ⬆️")
 else:
    print("❌Escolha inválida❌")



def ver_equipamentos(self):
    print("Seus Equipamentos:")
    for categoria, equipamento in self.equipamentos.items():
        if equipamento:
            print(f"{categoria.capitalize()}: {equipamento['nome']}")
        else:
            print(f"{categoria.capitalize()}: ❌ Nenhum")





def ganhar_xp(self, xp_ganho):
 """Adiciona XP ao jogador e verifica se ele sobe de nível."""
 self.xp += xp_ganho
 nivel_anterior = self.nivel
 while self.xp >= self.xp_up:
    self.xp -= self.xp_up
    self.nivel += 1
    self.xp_up += 10
    print(f"{self.nome} subiu para o nível {self.nivel}!")
    self.aumentar_atributos()  # Chama o método para aumentar os atributos

def aumentar_atributos(self):
 """Aumenta atributos com base na classe do jogador ao subir de nível."""
 if self.classe == "Guerreiro":
    self.vida_máxima += 5
    self.vida += 5  # Garante que a vida atual também aumente
    self.sp_máximo += 1
    self.sp += 1  # Garante que o SP atual também aumente
    self.ataque_base += 1
    self.defesa_base += 3

 elif self.classe == "Assassino":
    self.vida_máxima += 1
    self.vida += 1
    self.sp_máximo += 1
    self.sp += 1
    self.ataque_base += 3
    self.defesa_base += 1

 elif self.classe == "Arqueiro":
    self.vida_máxima += 3
    self.vida += 3
    self.sp_máximo += 1
    self.sp += 1
    self.ataque_base += 2
    self.defesa_base += 2

# Garante que os valores não ultrapassem limites arbitrários (se necessário)
 self.vida = min(self.vida, self.vida_máxima)
 self.sp = min(self.sp, self.sp_máximo)

 print(f"Atributos de {self.nome} atualizados: Vida Máxima: {self.vida_máxima}, SP Máximo: {self.sp_máximo}.")


def adicionar_ouro(self, ouro_ganho):
    self.ouro += ouro_ganho
    print(f"{self.nome} agora tem {self.ouro} moedas de ouro! 🪙")




class chefe:
    """Classe que representa os chefes no jogo."""
    def __init__(self, nome, vida, dano, habilidades, recompensa, regiao, inimigos):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.dano = dano
        self.habilidades = habilidades  # Lista de habilidades especiais
        self.recompensa = recompensa  # Ouro e/ou item ao derrotar o chefe
        self.regiao = regiao  # Nome da região do chefe
        self.inimigos = inimigos  # Lista de inimigos específicos da região



def usar_habilidade(self, jogador):
    """Usa uma habilidade especial no jogador."""
    habilidade = random.choice(self.habilidades)
    print(f"✨ {self.nome} usa a habilidade especial: {habilidade['nome']}!")
    jogador.vida -= habilidade['dano']
    print(f"💢 {habilidade['efeito']} Causou {habilidade['dano']} de dano em {jogador.nome}.")

def foi_derrotado(self):
    """Verifica se o chefe foi derrotado."""
    return self.vida <= 0

def recompensa_jogador(self, jogador):
    """Concede a recompensa ao jogador ao derrotar o chefe."""
    jogador.ouro += self.recompensa['ouro']
    print(f"🎉 {jogador.nome} recebeu {self.recompensa['ouro']} de ouro!")
    if 'item' in self.recompensa:
        print(f"🎁 {jogador.nome} encontrou um item: {self.recompensa['item']}!")
        jogador.itens.append(self.recompensa['item'])

def enfrentar_chefe(self, jogador, chefe, regiao_atual, regioes):
    """Realiza a batalha contra o chefe e gerencia o avanço."""
    print(f"\n⚔️ Batalha Final contra {chefe.nome} na região: {regioes[regiao_atual]['nome']}!")
    batalha(jogador, chefe, mostrar_status_inimigo=False)

    if jogador.vida > 0:
        jogador.regiao_atual += 1
        if regiao_atual < len(regioes):
            print(f"\n🌍 Você avançou para a próxima região: {regioes[regiao_atual]['nome']}!")
        else:
            print("\n🎉 Você venceu todas as regiões! Agora é hora de enfrentar inimigos infinitos!")
            regiao_atual = len(regioes) - 1  # Mantém o jogador na última região
    else:
        print("💀 Você foi derrotado na batalha contra o chefe!")
        return False, regiao_atual  # Indica derrota
    return True, regiao_atual  # Indica vitória e continua o jogo


def lutar(self, jogador, regioes, regiao_atual):
    """Simula a luta entre o jogador e o chefe."""
    print(f"\n⚔️ A batalha contra o chefe {self.nome} começa!")
    while self.vida > 0 and jogador.vida > 0:
        # Jogador ataca o chefe
        self.vida -= jogador.dano
        print(f"⚡ {jogador.nome} ataca {self.nome}, causando {jogador.dano} de dano!")

        # Chefe contra-ataca
        if self.vida > 0:
            self.atacar(jogador)
            if self.vida > 0:
                self.usar_habilidade(jogador)

    # Verifica se o chefe foi derrotado
    if self.foi_derrotado():
        print(f"\n🎉 {jogador.nome} derrotou {self.nome}!")
        self.recompensa_jogador(jogador)

        # Atualiza a região atual
        regiao_atual += 1
        if regiao_atual < len(regioes):
            print(f"🏆 Você avançou para a região: {regioes[regiao_atual]['nome']}")
        else:
            print("Você venceu todos os chefes e completou o jogo!")
            regiao_atual = len(regioes) - 1  # Garante que não ultrapasse o número de regiões

    else:
        print(f"{self.nome} continua firme! {jogador.nome} ainda precisa lutar mais.")

    return regiao_atual

class Dia:
    def __init__(self, dia_atual=0, dia_luta_final=30):
        self.dia_luta_final = dia_luta_final  # Total de dias até o final
        self.dia_descanso = 0  # Dias gastos descansando
        self.dia_lutar = 0  # Dias gastos lutando
        self.dia_atual = dia_atual  # Dia atual no progresso

def descansar(self, dias):
    self.dia_descanso += dias
    self.dia_atual += dias

def lutar(self, dias):
    self.dia_lutar += dias
    self.dia_atual += dias

def dias_restantes(self):

    return self.dia_luta_final - self.dia_atual

def dias_mostrar_status(self):
   dia_mostrar_status = self.dia_luta_final - self.dia_atual


# Adicionando diálogos personalizados para cada tipo de inimigo
class Inimigo:
    def __init__(self, nome, vida, ataque, defesa, ouro_min, ouro_max, xp_min, xp_max, itens_poupado=None):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.ouro_min = ouro_min
        self.ouro_max = ouro_max
        self.xp_min = xp_min
        self.xp_max = xp_max
        self.itens_poupado = itens_poupado if itens_poupado else []
        self.dialogos = {
    "Goblin 👺": [
        {"tipo": "comum", "texto": "Eu roubei muitos tesouros, mas você não os terá!"},
        {"tipo": "comum", "texto": "Desista, humano! Não pode me vencer!"},
        {"tipo": "comum", "texto": "Você não passa de um inseto para mim!"},
        {"tipo": "especial", "texto": "É culpa dela nós goblins hoje termos que lutar para viver..."},
        {"tipo": "raro", "texto": "EU MATATEREI O REI PELO QUE FEZ"}
    ],
    "Esqueleto 💀": [
        {"tipo": "comum", "texto": "Só ossos... mas ainda luto!"},
        {"tipo": "comum", "texto": "Voltei dos mortos para lutar"},
        {"tipo": "comum", "texto": "Você sente medo? Deveria!"},
        {"tipo": "especial", "texto": "Eu lembro... de quando era vivo... ela era magnifica..."},
        {"tipo": "raro", "texto": "Vou te assombrar mesmo depois da morte Vossa Majestade!"}
    ],
    "Orc 👹": [
        {"tipo": "comum", "texto": "Você é pequeno demais para lutar comigo!"},
        {"tipo": "comum", "texto": "Prepare-se para a derrota!"},
        {"tipo": "comum", "texto": "Eu sou mais forte que qualquer humano!"},
        {"tipo": "especial", "texto": "Ela...me fez assim... me transformando em um MONSTRO!"},
        {"tipo": "raro", "texto": "Um dia eu fui como você, mas perdi tudo... e a culpa é dele"}
    ],
    "Slime 🫧": [
        {"tipo": "comum", "texto": "Glub, glub! Você não tem chance contra mim!"},
        {"tipo": "comum", "texto": "Sou mais forte do que pareço!"},
        {"tipo": "comum", "texto": "Você nunca derrotará um slime como eu!"},
        {"tipo": "especial", "texto": "Eu posso mostrar um dos tesouros dela... mas você tem que me poupar."},
        {"tipo": "raro", "texto": "Por favor... não quero ser destruído... já é muito humilhante viver depois do que aconteceu"}
    ],
    "Guerreiro 🤺": [
        {"tipo": "comum", "texto": "Minha força e espada pelo reino!"},
        {"tipo": "comum", "texto": "Você nunca será tão forte quanto eu!"},
        {"tipo": "comum", "texto": "A honra é tudo para um guerreiro!"},
        {"tipo": "especial", "texto": "Lutar é inútil... estamos destinados a falhar... se ela assumir o reino será nosso fim"},
        {"tipo": "raro", "texto": "Ele destruiu minha motivação de lutar"}
    ]
}


def exibir_dialogo(self):
# Verifica se o inimigo tem diálogos configurados
 if not hasattr(self, "dialogos") or self.nome not in self.dialogos:
    print(f"{self.nome} não tem diálogos configurados.")
    return

# Obtém os diálogos do inimigo
 dialogos = self.dialogos[self.nome]
 dialogos_comuns = [d["texto"] for d in dialogos if d["tipo"] == "comum"]
 dialogos_raros = [d["texto"] for d in dialogos if d["tipo"] == "raro"]
 dialogos_especiais = [d for d in dialogos if d["tipo"] == "especial"]

# Garante que há ao menos um diálogo disponível de cada tipo
 if not dialogos_comuns and not dialogos_raros and not dialogos_especiais:
    print(f"{self.nome} não possui nenhum diálogo configurado.")
    return

# Define o alcance do número aleatório entre 1 e 100
 alcance = random.randint(1, 100)

# Determina o tipo de diálogo com base no alcance
 if 1 <= alcance <= 75 and dialogos_comuns:
    dialogo_escolhido = random.choice(dialogos_comuns)
    print(f"{self.nome} diz: \"{dialogo_escolhido}\"")
 elif 76 <= alcance <= 90 and dialogos_raros:
    dialogo_escolhido = random.choice(dialogos_raros)
    print(f"{self.nome} diz: \"{dialogo_escolhido}\"")
 elif 91 <= alcance <= 100 and dialogos_especiais:
    dialogo_escolhido = dialogos_especiais[0]["texto"]
    print(f"{self.nome} diz: \"{dialogo_escolhido}\"")

    # Caso seja especial, adiciona o novo item ao inimigo
    if self.nome == "Slime 🫧":
        novo_item = {
            "nome": "Pedaço de Diário 📖",
            "tipo": "venda",
            "valor_compra": 0,
            "valor_venda": 200,
            "descricao": ("Querido diário, hoje queria confessar que me sinto meio vazia..."
                          " mesmo depois de derrotar tantos inimigos com o objetivo de salvar o reino parece que isso "
                          "não está ajudando. Me pergunto quantos mais devo matar para conseguir finalmente trazer "
                          "a paz e harmonia para meu reino...")
        }
        self.itens_poupado.append(novo_item)
        print("✨ Um novo item foi adicionado ao loot ao poupar o inimigo!")
 else:
    print(f"{self.nome} não tem um diálogo correspondente para esta chance.")





def exibir_status(self):
    print(f"{self.nome} - ❤️ Vida: {self.vida}, 🗡️ Ataque: {self.ataque}, 🛡️ Defesa: {self.defesa}")

def atacar(self, jogador, chefe):
    dano = self.ataque + random.randint(1, 5) - jogador.defesa
    dano = max(dano, 0)
    print(f"⚔️ {self.nome} ataca {jogador.nome}, causando {dano} de dano! ⚔️")
    jogador.vida -= dano

def drop_aleatorio(self):
    if self.item_poupado:
        return random.choice(self.item_poupado)
    else:
        return None

def recompensar(self, jogador):
 if self.vida <= 0:
    ouro = random.randint(self.ouro_min, self.ouro_max)
    xp = random.randint(self.xp_min, self.xp_max)
    print(f"{self.nome} deixou {ouro} moedas de ouro! 🪙")
    print(f"{jogador.nome} ganhou {xp} de XP! 📈")
    return ouro, xp
 return 0, 0  # Caso o inimigo ainda esteja vivo

class Inimigo:
    def __init__(self, nome, vida, ataque, defesa, ouro_min, ouro_max, xp_min, xp_max, itens_poupado=None):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.ouro_min = ouro_min
        self.ouro_max = ouro_max
        self.xp_min = xp_min
        self.xp_max = xp_max
        self.itens_poupado = itens_poupado if itens_poupado else []
        self.dialogos = {
            "Goblin 👺": [
                {"tipo": "comum", "texto": "Eu roubei muitos tesouros, mas você não os terá!"},
                {"tipo": "comum", "texto": "Desista, humano! Não pode me vencer!"},
                {"tipo": "comum", "texto": "Você não passa de um inseto para mim!"},
                {"tipo": "especial", "texto": "É culpa dela que nós goblins lutamos para sobreviver..."},
                {"tipo": "raro", "texto": "EU MATATEREI O REI PELO QUE FEZ"}
            ],
            "Esqueleto 💀": [
                {"tipo": "comum", "texto": "Só ossos... mas ainda luto!"},
                {"tipo": "comum", "texto": "Voltei dos mortos para lutar."},
                {"tipo": "comum", "texto": "Você sente medo? Deveria!"},
                {"tipo": "especial", "texto": "Eu lembro... de quando era vivo... ela era magnífica..."},
                {"tipo": "raro", "texto": "Vou te assombrar mesmo depois da morte Vossa Majestade!"}
            ]
            # Adicione mais diálogos conforme necessário
        }

def exibir_dialogo(self):
    if self.nome in self.dialogos:
        dialogo = random.choice(self.dialogos[self.nome])
        print(f"{self.nome}: {dialogo['texto']}")
    else:
        print(f"{self.nome} permanece em silêncio.")



class Regiao:
    def __init__(self, nome , chefe, inimigos=None, regiao_atual = 0):
        self.nome = nome
        self.regiao_atual = regiao_atual
        self.chefe = chefe
        self.inimigos = inimigos if inimigos else []

# Definindo regiões e inimigos
regioes = [
    Regiao(
        nome="Floresta 🌲",
        regiao_atual=0,
        chefe=Inimigo(
            "Slime Rei 👑🫧", vida=300, ataque=50, defesa=20, ouro_min=200, ouro_max=300, xp_min=200, xp_max=300,
            itens_poupado=[
                {"nome": "Coroa de Slime 👑", "tipo": "equipavel", "categoria": "acessório", "efeito": 15, "valor_compra": 100, "valor_venda": 80, "descricao": "Uma coroa gelatinosa que melhora sua defesa."}
            ]
        ),
        inimigos=[
            Inimigo("Slime 🫧", vida=30, ataque=12, defesa=7, ouro_min=7, ouro_max=12, xp_min=5, xp_max=10,
                    itens_poupado=[{"nome": "Pedaço de Slime 🟢", "tipo": "venda", "valor_venda": 20, "descricao": "Um pedaço de slime valioso."}]),
            Inimigo("Goblin 👺", vida=50, ataque=15, defesa=10, ouro_min=25, ouro_max=45, xp_min=10, xp_max=15,
                    itens_poupado=[{"nome": "Adaga de Ouro 🔪", "tipo": "equipavel", "categoria": "arma", "efeito": 10, "valor_compra": 60, "valor_venda": 50, "descricao": "Uma adaga cortante."}]),
            Inimigo("Esqueleto 💀", vida=40, ataque=20, defesa=8, ouro_min=10, ouro_max=15, xp_min=12, xp_max=20,
                    itens_poupado=[{"nome": "Arco Forte 🏹", "tipo": "equipavel", "categoria": "arma", "efeito": 12, "valor_compra": 60, "valor_venda": 50, "descricao": "Um arco poderoso."}]),
            Inimigo("Orc 👹", vida=70, ataque=25, defesa=20, ouro_min=25, ouro_max=35, xp_min=25, xp_max=35,
                    itens_poupado=[{"nome": "Machado de Guerra 🪓", "tipo": "equipavel", "categoria": "arma", "efeito": 12, "valor_compra": 40, "valor_venda": 30, "descricao": "Um machado robusto."}]),
            Inimigo("Guerreiro 🤺", vida=90, ataque=30, defesa=25, ouro_min=35, ouro_max=45, xp_min=30, xp_max=40,
                    itens_poupado=[{"nome": "Espada Lendária ⚔️", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_compra": 150, "valor_venda": 100, "descricao": "Uma espada lendária."}])
        ]
    ),
    Regiao(
        nome="Deserto 🏜️",
        regiao_atual=1,
        chefe=Inimigo(
            "Faraó 🤴", vida=400, ataque=60, defesa=30, ouro_min=250, ouro_max=350, xp_min=250, xp_max=350,
            itens_poupado=[
                {"nome": "Cetro Real 🪄", "tipo": "equipavel", "categoria": "arma", "efeito": 25, "valor_compra": 120, "valor_venda": 90, "descricao": "Um cetro que aumenta a magia."}
            ]
        ),
        inimigos=[
            Inimigo("Múmia 🕸️", vida=50, ataque=18, defesa=10, ouro_min=20, ouro_max=40, xp_min=15, xp_max=25,
                    itens_poupado=[{"nome": "Bandagens Velhas 🩹", "tipo": "venda", "valor_venda": 10, "descricao": "Bandagens antigas de múmias."}]),
            Inimigo("Serpente 🐍", vida=60, ataque=25, defesa=15, ouro_min=30, ouro_max=50, xp_min=20, xp_max=30,
                    itens_poupado=[{"nome": "Veneno de Serpente 🧪", "tipo": "usavel", "efeito": 15, "valor_venda": 25, "descricao": "Um veneno poderoso."}]),
            Inimigo("Sarcófago Vivo 🛡️", vida=100, ataque=30, defesa=30, ouro_min=50, ouro_max=70, xp_min=40, xp_max=60,
                    itens_poupado=[{"nome": "Fragmento de Sarcófago 🪨", "tipo": "venda", "valor_venda": 35, "descricao": "Um fragmento antigo valioso."}]),
            Inimigo("Anubis 🐕‍🦺", vida=120, ataque=35, defesa=25, ouro_min=60, ouro_max=80, xp_min=50, xp_max=70,
                    itens_poupado=[{"nome": "Amuleto de Anubis 📿", "tipo": "equipavel", "categoria": "acessório", "efeito": 20, "valor_compra": 70, "valor_venda": 50, "descricao": "Aumenta resistência mágica."}]),
            Inimigo("Set 🐆", vida=150, ataque=40, defesa=35, ouro_min=80, ouro_max=100, xp_min=60, xp_max=80,
                    itens_poupado=[{"nome": "Clava de Set ⚒️", "tipo": "equipavel", "categoria": "arma", "efeito": 30, "valor_compra": 100, "valor_venda": 75, "descricao": "Uma clava destruidora."}])
        ]
    ),
    Regiao(
        nome="Mar 🌊",
        regiao_atual=2,
        chefe=Inimigo(
            "Cthulhu 🦑", vida=500, ataque=80, defesa=40, ouro_min=300, ouro_max=400, xp_min=300, xp_max=400,
            itens_poupado=[
                {"nome": "Tentáculo de Cthulhu 🦑", "tipo": "equipavel", "categoria": "arma", "efeito": 40, "valor_compra": 200, "valor_venda": 150, "descricao": "Um tentáculo de Cthulhu que aumenta o ataque."}
            ]
        ),
        inimigos=[
            Inimigo("Sereia Estérica 🧜‍♀️", vida=60, ataque=30, defesa=20, ouro_min=50, ouro_max=80, xp_min=25, xp_max=40,
                    itens_poupado=[{"nome": "Canto Hipnótico 🎶", "tipo": "usavel", "efeito": 25, "valor_venda": 40, "descricao": "Aumenta a defesa por um tempo."}]),
            Inimigo("Peixe Espada 🐟", vida=70, ataque=40, defesa=30, ouro_min=50, ouro_max=70, xp_min=30, xp_max=45,
                    itens_poupado=[{"nome": "Escama de Peixe Espada 🗡️", "tipo": "equipavel", "categoria": "acessório", "efeito": 20, "valor_venda": 60, "descricao": "Aumenta o ataque."}]),
            Inimigo("Tubarão Branco 🦈", vida=100, ataque=50, defesa=40, ouro_min=80, ouro_max=120, xp_min=50, xp_max=70,
                    itens_poupado=[{"nome": "Dente de Tubarão 🦷", "tipo": "venda", "valor_venda": 50, "descricao": "Um dente afiado de tubarão."}]),
            Inimigo("Cavaleiro Marinho 🐠", vida=150, ataque=60, defesa=50, ouro_min=100, ouro_max=150, xp_min=60, xp_max=80,
                    itens_poupado=[{"nome": "Espada Marinha ⚔️", "tipo": "equipavel", "categoria": "arma", "efeito": 50, "valor_compra": 150, "valor_venda": 100, "descricao": "Uma espada forjada nas profundezas do mar."}]),
            Inimigo("Peixe Lanterna 💡", vida=80, ataque=35, defesa=30, ouro_min=50, ouro_max=90, xp_min=35, xp_max=50,
                    itens_poupado=[{"nome": "Luz de Peixe Lanterna 💡", "tipo": "usavel", "efeito": 30, "valor_venda": 40, "descricao": "Aumenta a visão e a agilidade por um tempo."}])
            ]
        ),
        Regiao(
        nome="Montes Nevados ❄️",
        regiao_atual=3,
        chefe=Inimigo(
            "Yeti 🏔️",
            vida=400, ataque=60, defesa=40, ouro_min=250, ouro_max=350, xp_min=250, xp_max=350,
            itens_poupado=[
                {"nome": "Clava de Gelo 🪓", "tipo": "equipavel", "categoria": "arma", "efeito": 30, "valor_compra": 150, "valor_venda": 120, "descricao": "Uma clava gelada que aumenta a resistência."}
            ]
        ),
        inimigos=[
            Inimigo("Lobo 🐺", vida=50, ataque=20, defesa=15, ouro_min=25, ouro_max=45, xp_min=20, xp_max=30,
                    itens_poupado=[{"nome": "Pelagem de Lobo 🧥", "tipo": "equipavel", "categoria": "acessório", "efeito": 15, "valor_venda": 40, "descricao": "Aumenta a resistência ao frio."}]),
            Inimigo("Caçador 🦯", vida=70, ataque=30, defesa=20, ouro_min=40, ouro_max=60, xp_min=30, xp_max=45,
                    itens_poupado=[{"nome": "Faca de Caçador 🔪", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_venda": 50, "descricao": "Uma faca afiada de caça."}]),
            Inimigo("Urso Maior 🐻", vida=150, ataque=50, defesa=45, ouro_min=70, ouro_max=100, xp_min=50, xp_max=70,
                    itens_poupado=[{"nome": "Garra de Urso 🦾", "tipo": "equipavel", "categoria": "arma", "efeito": 35, "valor_venda": 80, "descricao": "Uma garra de urso que aumenta o dano."}]),
            Inimigo("Urso Menor 🐻", vida=120, ataque=40, defesa=35, ouro_min=50, ouro_max=80, xp_min=40, xp_max=60,
                    itens_poupado=[{"nome": "Pelagem de Urso 🧸", "tipo": "equipavel", "categoria": "acessório", "efeito": 25, "valor_venda": 60, "descricao": "Aumenta a defesa."}]),
            Inimigo("Pinguim Foguete 🐧", vida=60, ataque=25, defesa=20, ouro_min=40, ouro_max=60, xp_min=25, xp_max=35,
                    itens_poupado=[{"nome": "Missil Pinguim 🚀", "tipo": "usavel", "efeito": 30, "valor_venda": 50, "descricao": "Aumenta o ataque por um tempo."}])
        ]
    ),
    Regiao(
        nome="Entrada do Reino 🏰",
        regiao_atual=4,
        chefe=Inimigo(
            "Impavidus, o Rei 👑",
            vida=500, ataque=100, defesa=70, ouro_min=400, ouro_max=500, xp_min=350, xp_max=450,
            itens_poupado=[
                {"nome": "Coroa de Impavidus 👑", "tipo": "equipavel", "categoria": "acessório", "efeito": 40, "valor_compra": 250, "valor_venda": 200, "descricao": "A coroa do grande rei Impavidus."}
            ]
        ),
        inimigos=[
            Inimigo("Servo 🧑‍⚖️", vida=40, ataque=10, defesa=5, ouro_min=10, ouro_max=15, xp_min=5, xp_max=10,
                    itens_poupado=[{"nome": "Capa de Servo 👘", "tipo": "equipavel", "categoria": "acessório", "efeito": 5, "valor_venda": 10, "descricao": "Uma capa simples."}]),
            Inimigo("Guarda 🛡️", vida=80, ataque=25, defesa=20, ouro_min=40, ouro_max=60, xp_min=20, xp_max=30,
                    itens_poupado=[{"nome": "Espada Curta 🗡️", "tipo": "equipavel", "categoria": "arma", "efeito": 15, "valor_venda": 30, "descricao": "Uma espada curta."}]),
            Inimigo("Bobo da Corte 🤡", vida=50, ataque=10, defesa=10, ouro_min=25, ouro_max=40, xp_min=15, xp_max=25,
                    itens_poupado=[{"nome": "Chapéu de Palhaço 🎩", "tipo": "equipavel", "categoria": "acessório", "efeito": 10, "valor_venda": 15, "descricao": "Um chapéu colorido."}]),
            Inimigo("Camponês Enfurecido 👩‍🌾", vida=60, ataque=20, defesa=10, ouro_min=30, ouro_max=50, xp_min=20, xp_max=30,
                    itens_poupado=[{"nome": "Ferro de Camponês ⚒️", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_venda": 40, "descricao": "Uma ferramenta de trabalho."}]),
            Inimigo("Cavalo 🐴", vida=100, ataque=30, defesa=50, ouro_min=80, ouro_max=120, xp_min=40, xp_max=60,
                    itens_poupado=[{"nome": "Sela de Cavalo 🐴", "tipo": "equipavel", "categoria": "acessório", "efeito": 25, "valor_venda": 70, "descricao": "Uma sela de qualidade."}])
        ]
    ),
    Regiao(
        nome="Dentro do Castelo 🏰",
        regiao_atual=5,
        chefe=Inimigo(
            "Princesa Ignarus 👸",
            vida=600, ataque=120, defesa=80, ouro_min=500, ouro_max=600, xp_min=400, xp_max=500,
            itens_poupado=[
                {"nome": "Diadema Real 👑", "tipo": "equipavel", "categoria": "acessório", "efeito": 50, "valor_compra": 300, "valor_venda": 250, "descricao": "O diadema da princesa Ignarus."}
            ]
        ),
        inimigos=[
            Inimigo("Guarda Gigante 🏰", vida=100, ataque=40, defesa=30, ouro_min=60, ouro_max=90, xp_min=40, xp_max=60,
                    itens_poupado=[{"nome": "Espada Longa 🗡️", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_venda": 50, "descricao": "Uma espada gigante."}]),
            Inimigo("Nobre 🕴️", vida=60, ataque=20, defesa=15, ouro_min=30, ouro_max=50, xp_min=25, xp_max=40,
                    itens_poupado=[{"nome": "Manto de Nobre 👗", "tipo": "equipavel", "categoria": "acessório", "efeito": 15, "valor_venda": 40, "descricao": "Um manto luxuoso."}]),
            Inimigo("Burguês Endividado 💸", vida=80, ataque=25, defesa=20, ouro_min=40, ouro_max=60, xp_min=30, xp_max=50,
                    itens_poupado=[{"nome": "Carteira de Ouro 💼", "tipo": "venda", "valor_venda": 40, "descricao": "Uma carteira cheia de promissórias."}]),
            Inimigo("Cães Reais 🐕", vida=70, ataque=30, defesa=25, ouro_min=50, ouro_max=70, xp_min=30, xp_max=50,
                    itens_poupado=[{"nome": "Coleira de Ouro 🐾", "tipo": "equipavel", "categoria": "acessório", "efeito": 25, "valor_venda": 60, "descricao": "Uma coleira imponente."}]),
            Inimigo("Soldado Experiente ⚔️", vida=100, ataque=35, defesa=30, ouro_min=70, ouro_max=100, xp_min=50, xp_max=80,
                    itens_poupado=[{"nome": "Lança de Soldado 🏹", "tipo": "equipavel", "categoria": "arma", "efeito": 25, "valor_venda": 70, "descricao": "Uma lança afiada."}])
        ]
    )
]

  # Começa na floresta

class Jogo:
    
 def __int__(self):
     self.dia=1
     self.estado={}
 def incrementar_dia_lutar(self):
     self.dia_lutar+=1

 dia_lutar=0
 def menu(jogador, regioes, regiao_atual, jogo=None):
    regioes = jogador.regioes
    regiao_atual = jogador.regiao_atual
    dia_lutar+=1

def explorar(regioes, regiao_atual, jogador):
    """Gerencia a exploração e inicia batalhas quando necessário."""

regioes = ["Floresta 🌲", "Deserto 🏜️", "Mar 🌊", "Montes Nevados ❄️", "Entrada do Reino 🏰", "Dentro do Castelo 🏰"]

inimigos_por_regiao = [
{"nome": "Floresta 🌲", "inimigos": [
    Inimigo("Slime 🫧", vida=30, ataque=12, defesa=7, ouro_min=7, ouro_max=12, xp_min=5, xp_max=10,
            itens_poupado=[{"nome": "Pedaço de Slime 🟢", "tipo": "venda", "valor_venda": 20, "descricao": "Um pedaço de slime valioso."}]),
    Inimigo("Goblin 👺", vida=50, ataque=15, defesa=10, ouro_min=25, ouro_max=45, xp_min=10, xp_max=15,
            itens_poupado=[{"nome": "Adaga de Ouro 🔪", "tipo": "equipavel", "categoria": "arma", "efeito": 10, "valor_compra": 60, "valor_venda": 50, "descricao": "Uma adaga cortante."}]),
    Inimigo("Esqueleto 💀", vida=40, ataque=20, defesa=8, ouro_min=10, ouro_max=15, xp_min=12, xp_max=20,
            itens_poupado=[{"nome": "Arco Forte 🏹", "tipo": "equipavel", "categoria": "arma", "efeito": 12, "valor_compra": 60, "valor_venda": 50, "descricao": "Um arco poderoso."}]),
    Inimigo("Orc 👹", vida=70, ataque=25, defesa=20, ouro_min=25, ouro_max=35, xp_min=25, xp_max=35,
            itens_poupado=[{"nome": "Machado de Guerra 🪓", "tipo": "equipavel", "categoria": "arma", "efeito": 12, "valor_compra": 40, "valor_venda": 30, "descricao": "Um machado robusto."}]),
    Inimigo("Guerreiro 🤺", vida=90, ataque=30, defesa=25, ouro_min=35, ouro_max=45, xp_min=30, xp_max=40,
            itens_poupado=[{"nome": "Espada Lendária ⚔️", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_compra": 150, "valor_venda": 100, "descricao": "Uma espada lendária."}])
]},
{"nome": "Deserto 🏜️", "inimigos": [
        Inimigo("Múmia 🕸️", vida=50, ataque=18, defesa=10, ouro_min=20, ouro_max=40, xp_min=15, xp_max=25,
                itens_poupado=[{"nome": "Bandagens Velhas 🩹", "tipo": "venda", "valor_venda": 10, "descricao": "Bandagens antigas de múmias."}]),
        Inimigo("Serpente 🐍", vida=60, ataque=25, defesa=15, ouro_min=30, ouro_max=50, xp_min=20, xp_max=30,
                itens_poupado=[{"nome": "Veneno de Serpente 🧪", "tipo": "usavel", "efeito": 15, "valor_venda": 25, "descricao": "Um veneno poderoso."}]),
        Inimigo("Sarcófago Vivo 🛡️", vida=100, ataque=30, defesa=30, ouro_min=50, ouro_max=70, xp_min=40, xp_max=60,
                itens_poupado=[{"nome": "Fragmento de Sarcófago 🪨", "tipo": "venda", "valor_venda": 35, "descricao": "Um fragmento antigo valioso."}]),
        Inimigo("Anubis 🐕‍🦺", vida=120, ataque=35, defesa=25, ouro_min=60, ouro_max=80, xp_min=50, xp_max=70,
                itens_poupado=[{"nome": "Amuleto de Anubis 📿", "tipo": "equipavel", "categoria": "acessório", "efeito": 20, "valor_compra": 70, "valor_venda": 50, "descricao": "Aumenta resistência mágica."}]),
        Inimigo("Set 🐆", vida=150, ataque=40, defesa=35, ouro_min=80, ouro_max=100, xp_min=60, xp_max=80,
                itens_poupado=[{"nome": "Clava de Set ⚒️", "tipo": "equipavel", "categoria": "arma", "efeito": 30, "valor_compra": 100, "valor_venda": 75, "descricao": "Uma clava destruidora."}])
]},
{"nome": "Mar 🌊", "inimigos": [
        Inimigo("Sereia Estérica 🧜‍♀️", vida=60, ataque=30, defesa=20, ouro_min=50, ouro_max=80, xp_min=25, xp_max=40,
                itens_poupado=[{"nome": "Canto Hipnótico 🎶", "tipo": "usavel", "efeito": 25, "valor_venda": 40, "descricao": "Aumenta a defesa por um tempo."}]),
        Inimigo("Peixe Espada 🐟", vida=70, ataque=40, defesa=30, ouro_min=50, ouro_max=70, xp_min=30, xp_max=45,
                itens_poupado=[{"nome": "Escama de Peixe Espada 🗡️", "tipo": "equipavel", "categoria": "acessório", "efeito": 20, "valor_venda": 60, "descricao": "Aumenta o ataque."}]),
        Inimigo("Tubarão Branco 🦈", vida=100, ataque=50, defesa=40, ouro_min=80, ouro_max=120, xp_min=50, xp_max=70,
                itens_poupado=[{"nome": "Dente de Tubarão 🦷", "tipo": "venda", "valor_venda": 50, "descricao": "Um dente afiado de tubarão."}]),
        Inimigo("Cavaleiro Marinho 🐠", vida=150, ataque=60, defesa=50, ouro_min=100, ouro_max=150, xp_min=60, xp_max=80,
                itens_poupado=[{"nome": "Espada Marinha ⚔️", "tipo": "equipavel", "categoria": "arma", "efeito": 50, "valor_compra": 150, "valor_venda": 100, "descricao": "Uma espada forjada nas profundezas do mar."}]),
        Inimigo("Peixe Lanterna 💡", vida=80, ataque=35, defesa=30, ouro_min=50, ouro_max=90, xp_min=35, xp_max=50,
                itens_poupado=[{"nome": "Luz de Peixe Lanterna 💡", "tipo": "usavel", "efeito": 30, "valor_venda": 40, "descricao": "Aumenta a visão e a agilidade por um tempo."}])
]},
    {"nome": "Montes Nevados ❄️", "inimigos": [
        Inimigo("Lobo 🐺", vida=50, ataque=20, defesa=15, ouro_min=25, ouro_max=45, xp_min=20, xp_max=30,
                itens_poupado=[{"nome": "Pelagem de Lobo 🧥", "tipo": "equipavel", "categoria": "acessório", "efeito": 15, "valor_venda": 40, "descricao": "Aumenta a resistência ao frio."}]),
        Inimigo("Caçador 🦯", vida=70, ataque=30, defesa=20, ouro_min=40, ouro_max=60, xp_min=30, xp_max=45,
                itens_poupado=[{"nome": "Faca de Caçador 🔪", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_venda": 50, "descricao": "Uma faca afiada de caça."}]),
        Inimigo("Urso Maior 🐻", vida=150, ataque=50, defesa=45, ouro_min=70, ouro_max=100, xp_min=50, xp_max=70,
                itens_poupado=[{"nome": "Garra de Urso 🦾", "tipo": "equipavel", "categoria": "arma", "efeito": 35, "valor_venda": 80, "descricao": "Uma garra de urso que aumenta o dano."}]),
        Inimigo("Urso Menor 🐻", vida=120, ataque=40, defesa=35, ouro_min=50, ouro_max=80, xp_min=40, xp_max=60,
                itens_poupado=[{"nome": "Pelagem de Urso 🧸", "tipo": "equipavel", "categoria": "acessório", "efeito": 25, "valor_venda": 60, "descricao": "Aumenta a defesa."}]),
        Inimigo("Pinguim Foguete 🐧", vida=60, ataque=25, defesa=20, ouro_min=40, ouro_max=60, xp_min=25, xp_max=35,
                itens_poupado=[{"nome": "Missil Pinguim 🚀", "tipo": "usavel", "efeito": 30, "valor_venda": 50, "descricao": "Aumenta o ataque por um tempo."}])
]},
      {"nome": "Entrada do Reino 🏰", "inimigos": [
         Inimigo("Servo 🧑‍⚖️", vida=40, ataque=10, defesa=5, ouro_min=10, ouro_max=15, xp_min=5, xp_max=10,
                itens_poupado=[{"nome": "Capa de Servo 👘", "tipo": "equipavel", "categoria": "acessório", "efeito": 5, "valor_venda": 10, "descricao": "Uma capa simples."}]),
        Inimigo("Guarda 🛡️", vida=80, ataque=25, defesa=20, ouro_min=40, ouro_max=60, xp_min=20, xp_max=30,
                itens_poupado=[{"nome": "Espada Curta 🗡️", "tipo": "equipavel", "categoria": "arma", "efeito": 15, "valor_venda": 30, "descricao": "Uma espada curta."}]),
        Inimigo("Bobo da Corte 🤡", vida=50, ataque=10, defesa=10, ouro_min=25, ouro_max=40, xp_min=15, xp_max=25,
                itens_poupado=[{"nome": "Chapéu de Palhaço 🎩", "tipo": "equipavel", "categoria": "acessório", "efeito": 10, "valor_venda": 15, "descricao": "Um chapéu colorido."}]),
        Inimigo("Camponês Enfurecido 👩‍🌾", vida=60, ataque=20, defesa=10, ouro_min=30, ouro_max=50, xp_min=20, xp_max=30,
                itens_poupado=[{"nome": "Ferro de Camponês ⚒️", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_venda": 40, "descricao": "Uma ferramenta de trabalho."}]),
        Inimigo("Cavalo 🐴", vida=100, ataque=30, defesa=50, ouro_min=80, ouro_max=120, xp_min=40, xp_max=60,
                itens_poupado=[{"nome": "Sela de Cavalo 🐴", "tipo": "equipavel", "categoria": "acessório", "efeito": 25, "valor_venda": 70, "descricao": "Uma sela de qualidade."}])
]},
    {"nome": "Dentro do Castelo 🏰", "inimigos": [
       Inimigo("Guarda Gigante 🏰", vida=100, ataque=40, defesa=30, ouro_min=60, ouro_max=90, xp_min=40, xp_max=60,
                itens_poupado=[{"nome": "Espada Longa 🗡️", "tipo": "equipavel", "categoria": "arma", "efeito": 20, "valor_venda": 50, "descricao": "Uma espada gigante."}]),
        Inimigo("Nobre 🕴️", vida=60, ataque=20, defesa=15, ouro_min=30, ouro_max=50, xp_min=25, xp_max=40,
                itens_poupado=[{"nome": "Manto de Nobre 👗", "tipo": "equipavel", "categoria": "acessório", "efeito": 15, "valor_venda": 40, "descricao": "Um manto luxuoso."}]),
        Inimigo("Burguês Endividado 💸", vida=80, ataque=25, defesa=20, ouro_min=40, ouro_max=60, xp_min=30, xp_max=50,
                itens_poupado=[{"nome": "Carteira de Ouro 💼", "tipo": "venda", "valor_venda": 40, "descricao": "Uma carteira cheia de promissórias."}]),
        Inimigo("Cães Reais 🐕", vida=70, ataque=30, defesa=25, ouro_min=50, ouro_max=70, xp_min=30, xp_max=50,
                itens_poupado=[{"nome": "Coleira de Ouro 🐾", "tipo": "equipavel", "categoria": "acessório", "efeito": 25, "valor_venda": 60, "descricao": "Uma coleira imponente."}]),
        Inimigo("Soldado Experiente ⚔️", vida=100, ataque=35, defesa=30, ouro_min=70, ouro_max=100, xp_min=50, xp_max=80,
                itens_poupado=[{"nome": "Lança de Soldado 🏹", "tipo": "equipavel", "categoria": "arma", "efeito": 25, "valor_venda": 70, "descricao": "Uma lança afiada."}])
]}
]

def processar_regiao(jogador, regioes, inimigos_por_regiao, chefe):
    # Inicializa a região atual do jogador
    regiao_atual = jogador.regiao_atual
    if regiao_atual < len(regioes):
        regiao_nome = regioes[regiao_atual]

        # Encontre o dicionário correspondente ao nome da região
        regiao_dict = next((r for r in inimigos_por_regiao if r["nome"] == regiao_nome), None)

        if regiao_dict:
            inimigos_disponiveis = regiao_dict["inimigos"]

            if inimigos_disponiveis:
                # Escolha aleatória de um objeto `Inimigo`
                inimigo = random.choice(inimigos_disponiveis)

                # Chamar a batalha
                batalha(jogador, inimigo, chefe, mostrar_status_inimigo=True)
            else:
                print(f"❌ A região {regiao_nome} não possui inimigos.")
        else:
            print(f"❌ A região {regiao_nome} não foi encontrada na lista de regiões.")
    else:
        print("❌ Região inválida!")

    # Retornar a região atual, independente do resultado
    return regiao_atual




def salvar_jogo(jogador):
    try:
        with open('jogo_salvo.pkl', 'wb') as f:
            pickle.dump(jogador, f)
        print("💾 Jogo salvo com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar o jogo: {e}")


def carregar_jogo():
    try:
        with open('jogo_salvo.pkl', 'rb') as f:
            jogador_carregado = pickle.load(f)
        print("📂 Jogo carregado com sucesso!")
        return jogador_carregado
    except FileNotFoundError:
        print("❌ Nenhum jogo salvo encontrado.")
        return None
    except Exception as e:
        print(f"❌ Erro ao carregar o jogo: {e}")
        return None


def avancar_dia(jogo):
    """Avança o dia e verifica se é dia de batalha especial."""
    jogo["dia"] += 1
    if jogo["dia"] > jogo["max_dias"]:  # Reseta o ciclo no final
        jogo["dia"] = 1
        print("\n⚠️ Se prepare! A grande batalha está prestes a começar! ⚠️")
        return True
    return False


def menu(jogador, regioes, jogo):
    """
    Menu principal do jogador. Exibe as opções e gerencia as ações com base na escolha do jogador.
    """
    regiao_atual = jogador.regiao_atual
    dias = Dia()  # Criação do objeto Dia

    while True:
        # Exibição do menu principal
        print("\nEscolha uma ação:")
        print("1) 🤜💥🤛 Explorar (Lutar)")
        print("2) 💰 Ir para a loja")
        print("3) 📈 Ver status do personagem")
        print("4) 📦 Inventário")
        print("5) ⚒️ Ver e Equipar equipamentos")
        print("6) 🛏️ Descansar")
        print("7) 💾 Salvar")
        print("8) 📂 Carregar")
        print("9) 👋 Sair do jogo")

        # Validação de entrada do jogador
        try:
            escolha = int(input("? "))
            if 1 <= escolha <= 9:  # Verifica se a escolha está dentro do intervalo válido
                # Ações baseadas na escolha
                if escolha == 1:  # Explorar
                    print("🗺️ Você escolheu explorar!")
                    regiao_atual = explorar(regioes, jogador)  # Atualiza a região atual
                    dias.lutar(1)  # Avança um dia ao explorar

                elif escolha == 2:  # Loja
                    print("💰 Bem-vindo à loja!")
                    loja(jogador)

                elif escolha == 3:  # Status
                    jogador.exibir_status()
                    dias.dias_mostrar_status()  # Mostra o status dos dias
                    print(f"🌍 Região atual: {regioes[regiao_atual].nome}")  # Mostra a região atual do jogador

                elif escolha == 4:  # Inventário
                    if jogador.inventario:
                        print("📦 Inventário:")
                        for i, item in enumerate(jogador.inventario, start=1):
                            print(f"{i}) {item['nome']} - {item['descricao']}")
                    else:
                        print("❌ Seu inventário está vazio.")

                elif escolha == 5:  # Equipamentos
                    jogador.ver_equipamentos()  # Mostra os equipamentos do jogador
                    resposta = input("Deseja equipar algum item? (s/n): ").lower()
                    if resposta == "s":
                        jogador.equipar_item()

                elif escolha == 6:  # Descansar
                    resposta = input("Quer descansar por 30 moedas para restaurar vida e energia? (s/n): ").lower()
                    if resposta == "s":
                        if jogador.ouro >= 30:
                            jogador.ouro -= 30
                            jogador.vida = jogador.vida_máxima
                            jogador.sp = jogador.sp_máximo
                            print(f"{jogador.nome} descansou e restaurou toda a vida e energia!")
                            dias.dia_descanso += 1  # Incrementa o número de dias descansados
                        else:
                            print("❌ Moedas insuficientes!")
                    elif resposta == "n":
                        print("🔙 Você decidiu não descansar.")
                    else:
                        print("❌ Resposta inválida. Digite 's' ou 'n'.")

                elif escolha == 7:  # Salvar
                    print("💾 Salvando progresso do jogo...")
                    salvar_jogo(jogador)

                elif escolha == 8:  # Carregar
                    print("📂 Carregando progresso do jogo...")
                    jogador = carregar_jogo()

                elif escolha == 9:  # Sair
                    print("👋 Até a próxima!")
                    sys.exit()

            else:
                print("❌ Escolha inválida. Digite um número entre 1 e 9.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número.")

            
def menu(jogador, regioes, jogo):
    """
    Menu principal do jogador. Exibe as opções e gerencia as ações com base na escolha do jogador.
    """
    regiao_atual = jogador.regiao_atual
    dias = Dia()  # Criação do objeto Dia

    while True:
        # Exibição do menu principal
        print("\nEscolha uma ação:")
        print("1) 🤜💥🤛 Explorar (Lutar)")
        print("2) 💰 Ir para a loja")
        print("3) 📈 Ver status do personagem")
        print("4) 📦 Inventário")
        print("5) ⚒️ Ver e Equipar equipamentos")
        print("6) 🛏️ Descansar")
        print("7) 💾 Salvar")
        print("8) 📂 Carregar")
        print("9) 👋 Sair do jogo")

        # Validação de entrada do jogador
        try:
            escolha = int(input("? "))
            if 1 <= escolha <= 9:  # Verifica se a escolha está dentro do intervalo válido
                # Ações baseadas na escolha
                if escolha == 1:  # Explorar
                    print("🗺️ Você escolheu explorar!")
                    regiao_atual = explorar(regioes, jogador)  # Atualiza a região atual
                    dias.lutar(1)  # Avança um dia ao explorar

                elif escolha == 2:  # Loja
                    print("💰 Bem-vindo à loja!")
                    loja(jogador)

                elif escolha == 3:  # Status
                    jogador.exibir_status()
                    dias.dias_mostrar_status()  # Mostra o status dos dias
                    print(f"🌍 Região atual: {regioes[regiao_atual].nome}")  # Mostra a região atual do jogador

                elif escolha == 4:  # Inventário
                    if jogador.inventario:
                        print("📦 Inventário:")
                        for i, item in enumerate(jogador.inventario, start=1):
                            print(f"{i}) {item['nome']} - {item['descricao']}")
                    else:
                        print("❌ Seu inventário está vazio.")

                elif escolha == 5:  # Equipamentos
                    jogador.ver_equipamentos()  # Mostra os equipamentos do jogador
                    resposta = input("Deseja equipar algum item? (s/n): ").lower()
                    if resposta == "s":
                        jogador.equipar_item()

                elif escolha == 6:  # Descansar
                    resposta = input("Quer descansar por 30 moedas para restaurar vida e energia? (s/n): ").lower()
                    if resposta == "s":
                        if jogador.ouro >= 30:
                            jogador.ouro -= 30
                            jogador.vida = jogador.vida_máxima
                            jogador.sp = jogador.sp_máximo
                            print(f"{jogador.nome} descansou e restaurou toda a vida e energia!")
                            dias.dia_descanso += 1  # Incrementa o número de dias descansados
                        else:
                            print("❌ Moedas insuficientes!")
                    elif resposta == "n":
                        print("🔙 Você decidiu não descansar.")
                    else:
                        print("❌ Resposta inválida. Digite 's' ou 'n'.")

                elif escolha == 7:  # Salvar
                    print("💾 Salvando progresso do jogo...")
                    salvar_jogo(jogador)

                elif escolha == 8:  # Carregar
                    print("📂 Carregando progresso do jogo...")
                    jogador = carregar_jogo()

                elif escolha == 9:  # Sair
                    print("👋 Até a próxima!")
                    sys.exit()

            else:
                print("❌ Escolha inválida. Digite um número entre 1 e 9.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número.")

def loja(jogador):
    itens = [
        {"nome": "Adaga Simples 🔪", "tipo": "equipavel", "categoria": "arma", "classe_exclusiva": "Assassino", "efeito": 5, "valor_compra": 20, "valor_venda": 10, "descricao": "Uma arma simples e cortante."},
        {"nome": "Espada Básica ⚔️", "tipo": "equipavel", "categoria": "arma", "classe_exclusiva": "Guerreiro", "efeito": 5, "valor_compra": 30, "valor_venda": 15, "descricao": "Espada confortável para guerreiros."},
        {"nome": "Arco Básico 🏹", "tipo": "equipavel", "categoria": "arma", "classe_exclusiva": "Arqueiro", "efeito": 5, "valor_compra": 25, "valor_venda": 12, "descricao": "Arco ideal para combates à distância."},
        {"nome": "Poção de Vida Pequena ❣️", "tipo": "usavel", "efeito": 20, "valor_compra": 25,"valor_venda": 10, "descricao": "Uma poção que recupera 20 pontos de vida."},
        {"nome": "Armadura de Couro 🎽", "tipo": "equipavel", "categoria": "armadura", "classe_exclusiva": "todas as classes", "efeito": 5, "valor_compra": 40, "valor_venda": 20, "descricao": "Armadura leve, porém eficiênte."},
        {"nome": "Armadura de Ferro 🛡️", "tipo": "equipavel", "categoria": "armadura", "classe_exclusiva": "todas as classes", "efeito": 15, "valor_compra": 100, "valor_venda": 60, "descricao": "Resistente até o último uso."},
        {"nome": "Poção de Força 💪", "tipo": "usavel", "efeito": 10, "valor_compra": 20, "valor_venda": 10, "descricao": "Uma poção que aumenta o ataque temporariamente."},
        {"nome": "Poção de Resistência 🛡️", "tipo": "usavel", "efeito": 5, "valor_compra": 20, "valor_venda": 10, "descricao": "Uma poção que aumenta a defesa temporariamente."}
    ]

    while True:
        print("-------------------------")
        print(" 💲  Bem-vindo à loja! 💲 ")
        print("-------------------------")
        print("1)  Comprar item")
        print("2)  Vender item")
        print("3)💨  Sair da loja")

        try:
            escolha = int(input("? "))
        except ValueError:
            print("❌ Escolha inválida. Por favor, digite um número.")
            continue

        if escolha == 1:
            while True:
                print("\nItens disponíveis para compra:")
                print(f"{jogador.nome} tem {jogador.ouro} moedas.")  # Exibe as moedas do jogador

                for i, item in enumerate(itens):
                    print(f"{i + 1}) {item['nome']} - {item['valor_compra']} moedas")

                try:
                    escolha_item = int(input("Escolha um item para comprar (ou 0 para sair): ")) - 1
                except ValueError:
                    print("❌ Escolha inválida. Por favor, digite um número.")
                    continue

                if escolha_item == -1:
                    print("Você saiu do menu de compra.")
                    break
                elif 0 <= escolha_item < len(itens):
                    jogador.comprar_item(itens[escolha_item])
                    print(f"Saldo atual: {jogador.ouro} moedas.")  # Mostra saldo após compra
                else:
                    print("❌ Escolha inválida.")

        elif escolha == 2:
            while True:
                if not jogador.inventario:  # Verifica se o inventário está vazio
                    print("❌ Seu inventário está vazio. Nada para vender.")
                    break

                print("\nItens disponíveis para venda:")
                for i, item in enumerate(jogador.inventario):
                    print(f"{i + 1}) {item['nome']} - {item['valor_venda']} moedas")

                try:
                    escolha_item = int(input("Escolha um item para vender (ou 0 para sair): ")) - 1
                except ValueError:
                    print("❌ Escolha inválida. Por favor, digite um número.")
                    continue

                if escolha_item == -1:
                    print("Você saiu do menu de venda.")
                    break
                elif 0 <= escolha_item < len(jogador.inventario):
                    item_vendido = jogador.inventario[escolha_item]
                    #jogador.vender_item(item_vendido) # This should be already done for us
                    jogador.vender_item()

                    #print(f"Você vendeu {item_vendido['nome']} por {item_vendido['valor_venda']} moedas.") # This should be already done for us
                else:
                    print("❌ Escolha inválida.")

        elif escolha == 3:
            print("👋 Você saiu da loja.")
            break
        else:
            print("❌ Escolha inválida.")

def batalha(jogador, inimigo, chefe): # Retirado mostrar_status_inimigo do parametro
    """Simulates a battle between the player and an enemy."""

    # Verifica se o inimigo é um objeto Inimigo válido
    if not isinstance(inimigo, Inimigo):
        print("Erro: O inimigo fornecido não é válido!")
        return  # Encerra a função se o inimigo não for válido
        # Retira as variaveis rasgo_ativo etc

    jogador.rasgo_ativo = False
    jogador.rugido_ativo = False
    jogador.passo_sombrio_ativo = False
    jogador.amigo_da_floresta_ativo = False

    print(f"🔥 Uma batalha começou entre {jogador.nome} e {inimigo.nome}! 🔥")
    jogador.atacou = False
    jogador.acoes_restantes_na_batalha = 5
    is_chefe = inimigo.tipo == "chefe"

    while jogador.vida > 0 and inimigo.vida > 0:
        # Menu para escolhas do jogador
        print("\nEscolha sua ação:")
        print("1) ⚔️ Atacar")
        print("2) ✨ Usar habilidade")
        print("3) 🧪 Usar item")
        if not is_chefe: # So pode poupar e fugir se não for chefe
            print("4) 🤝 Poupar inimigo")
            print("5) 💬 Conversar")
            print("6) 🏃‍♂️ Fugir")

        try:
            escolha = int(input("? "))
        except ValueError:
            print("❌ Escolha inválida. Digite um número válido.")
            continue

        if escolha == 1:  # Atacar
            jogador.atacar(inimigo)
            jogador.atacou = True # Só pode poupar quem não foi atacado
            if inimigo.vida > 0: #Sempre verificar se inimigo ta vivo
                inimigo.atacar(jogador)

        elif escolha == 2:  # Usar habilidade
            jogador.usar_habilidade(inimigo)

            if inimigo.vida > 0: #Sempre verificar se inimigo ta vivo
                inimigo.atacar(jogador)

        elif escolha == 3:  # Usar item
            jogador.usar_item()
            if inimigo.vida > 0: #Sempre verificar se inimigo ta vivo
                inimigo.atacar(jogador)

        elif escolha == 4 and not is_chefe:  # Poupar inimigo
            if jogador.atacou: # Só pode poupar quem não foi atacado
                print("❌ Não é mais possivel poupar o inimigo pois você já atacou.")

            elif jogador.acoes_restantes_na_batalha > 0: # Verifica se o jogador tem acoes
                jogador.acoes_restantes_na_batalha -= 1
                print(f"Você pode poupar o inimigo mais {jogador.acoes_restantes_na_batalha} vezes.")

                if random.random() < 0.2:  # 20% de chance de sucesso
                    print(f"{jogador.nome} poupou {inimigo.nome}!")
                    break # Encerra a batalha se poupar
                else: #Poupar sem sucesso
                    print("O inimigo não foi convencido a se render.")
                    if inimigo.vida > 0: #Sempre verificar se inimigo ta vivo
                        inimigo.atacar(jogador)
            else:
                print("❌ Você não pode mais poupar o inimigo.")

        elif escolha == 5:  # Conversar
            print(f"{jogador.nome} tenta conversar com {inimigo.nome}.")
            if hasattr(inimigo, 'exibir_dialogo'):
                inimigo.exibir_dialogo()
            else:
                print(f"{inimigo.nome} não parece disposto a conversar.")
            if inimigo.vida > 0: #Sempre verificar se inimigo ta vivo
                inimigo.atacar(jogador)

        elif escolha == 6 and not is_chefe:  # Fugir
            if random.random() < 0.4:  # 40% de chance de sucesso
                print(f"{jogador.nome} conseguiu fugir! 💨")
                jogador.resetar_bonus_temporarios()
                return  # Encerra a função batalha
            else:
                print(f"{inimigo.nome} bloqueia sua fuga!")
                if inimigo.vida > 0: #Sempre verificar se inimigo ta vivo
                    inimigo.atacar(jogador)
        else:
            print("❌ Escolha inválida.")
        # Exibir status
        jogador.exibir_status()
        inimigo.exibir_status() #Mostra status do inimigo


    # Resultado da batalha -> Inside While

    if jogador.vida <= 0:
        print("💀 GAME OVER! 💀")
        return #Encerra funcao

    elif inimigo.vida <= 0:
        print(f"🎉 {inimigo.nome} foi derrotado! 🎉")
        recompensa = inimigo.recompensar(jogador)
        if recompensa:
            ouro, xp_ganho = recompensa
            jogador.ouro += ouro
            jogador.ganhar_xp(xp_ganho)
        return #Encerra funcao





if __name__ == "__main__": 
    iniciar_jogo()