
  # Estrutura
  #Personagem: Classe mãe
  # Herói: Controlado pelo usuário
  # Inimigo: Adversário do usuário
  # Todos os personagens vão receber nome, vida e nível.
  
import random

class Personagem:
  def __init__(self, nome, vida, nivel) -> None:
    # Vamos usar o princípio do encapsulamento, então vamos tornar o nome privado
    # todo Por quê precisamos usar encapsulamento aqui?
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  # Como todos atributos são privados, precisamos criar um função getter, pra poder exibir os dados.
  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return self.__vida
  
  def get_nivel(self):
    return self.__nivel
  
  # Essa função vai exibir os detalhes de cada personagem, porém, cada personagem ainda têm atributos próprios.
  def exibir_detalhes(self):
    return f'Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNível: {self.get_nivel()}'
  
  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida <0:
      self.__vida = 0
      
  # Método para exibir os detalhes do ataque.     
  def atacar(self, alvo):
    # Inicialmente fizemos o dano assim, porém
    # dano = self.__nivel * 2
    # Agora vamos randomizar o dano do ataque, pra ficar mais interessante
    # A função RANDINT nos deixa selecionar um valor entre um range A e B. Nesse caso inserimos o range como os valores do nível*2 e nível*4
    dano = random.randint(self.get_nivel( * 2), self.get_nivel() * 4) # Continua baseado no nível do personagem
    alvo.receber_ataque(dano)
    print (f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano! ')
    
  
# Como sabemos que o herói vai herdar todas as características de Personagem, já ligamos os dois
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):    # Somente o herói têm habilidade, isso o diferencia do inimigo
    super().__init__(nome, vida, nivel)   # Como queremos manter o comportamento do herói, que ele crie as características, precisamos do super
    self.__habilidade = habilidade
    
    # Agora precisamos também de um getter pra recuperar a habilidade, já que ela é privada.
  def get_habilidade(self):
    return self.__habilidade
  
  # Criaremos uma função pra exibir as características especias do personagem. 
  def exibir_detalhes(self):
    return f'{super().exibir_detalhes()} \nHabilidade: {self.get_habilidade()}\n'
  
  def ataque_especial(self, alvo):
    dano = random.randint(self.get_nivel( * 5), self.get_nivel() * 8) # Continua baseado no nível do personagem,dano vai ser aumentado, pois é um ataque especial. 
    alvo.receber_ataque(dano)
    print(f'{self.get_nome} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano. ')
    
    
class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo):    # Tipo é uma categoria somente do Inimigo.
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo
    
  # Agora também precisamos de um getter pra expor esse tipo, como é privado.
  def get_tipo(self):
    return self.__tipo
  
  # Criaremos uma função pra exibir as características especias do personagem. 
  def exibir_detalhes(self):
    return f'{super().exibir_detalhes()} \nTipo: {self.get_tipo()}\n'
  

class Jogo:
  """Classe Orquestradora do Jogo"""
  
  def __init__(self) -> None:
      self.heroi = Heroi(nome='Herói', vida=100, nivel=5, habilidade='Super Força')
      self.inimigo = Inimigo(nome='Morcego', vida=50, nivel=3, tipo='Voador' ) 
      
  def iniciar_batalha(self): 
    """Fazer a Gestão da Batalha em Turnos."""
    print('Iniciando batalha!')
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0: 
      print('\nDetalhes dos Personagens')
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())
      
      input('Pressione Enter para atacar...')
      escolha = input('Escolha (1 - Ataque Normal, 2 - Ataque Especial): ')
      
      if escolha == '1':
        self.heroi.atacar(self.inimigo)
      elif escolha == '2':
        self.heroi.ataque_especial(self.inimigo)
      else:
        print('Escolha inválida. Digite novamente. ')
        
      if self.inimigo.get_vide() > 0:
        # Inimigo ataca o herói. 
        self.inimigo.atacar(self.heroi)
        
    if self.heroi.get_vida() > 0:
      print('Parabéns, você venceu a batalha. ')
    else:
      print('\nVocê foi derrotado. ')


# Agora precisamos exibir quais informações existem, tanto do herói, quanto do inimigo.
# Agora na classe mãe vamos criar o método para exibir detalhes.
# Porém, dessa maneira ainda não conseguimos mostrar as características específicas de cada,
# Então devemos criar uma outra função para essa exibição. (linha 40)
# heroi = Heroi(nome='Herói', vida=100, nivel=5, habilidade='Super Força')
# print(heroi.exibir_detalhes())

# inimigo = Inimigo(nome='Morcego', vida=50, nivel=3, tipo='Voador' ) 
# print(inimigo.exibir_detalhes())


# Criar Instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()