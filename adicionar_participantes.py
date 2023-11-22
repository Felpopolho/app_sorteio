from _bibliotecas import *
from _conn import banco_default

def adicionar_participantes(tela):
            
    # Cria o frame
    frame()
    adicionar_participantes1 = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                      )
    adicionar_participantes1.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.95
                  )
    
    # Scroll bar
    adicionar_participantes = CTkScrollableFrame(adicionar_participantes1,
                    bg_color='silver',
                    fg_color='silver', 
                    corner_radius=25,
                    border_color='black')

    adicionar_participantes.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.70
                  )
    
    # Função que cria uma nova caixa de texto
    def adicionar_campo():
        
        qtd_campos = len(nomes)
        Label(adicionar_participantes, text=f"Participante nº{qtd_campos+1}", background='silver').pack()
        
        # Por algum motivo o select daqui chama combobox
        nome = ttk.Entry(adicionar_participantes, style="EstiloEntry.TEntry")
        nome.pack()
        
        # Aqui é pra escolher o número da sorte 
        Label(adicionar_participantes, text="Número da sorte:" ,background='silver').pack()
        numero = ttk.Entry(adicionar_participantes, style="EstiloEntry.TEntry")
        numero.pack()
                
        # Não, isso aqui não inclui o participante na lista pq ele ainda não existe, isso inclui o endereço de memória do widget textbox na lista pra eu acessar depois ;)
        nomes.append(nome)
        numeros.append(numero)
        
    # Função que salva os participantes no banco de dados
    def salvar():     
        # Aqui é onde o filho chora e a mãe não vê...
        for numero in numeros:
            
            # Não desperdiço código, vai ficar aqui
            # # Recupera o nome do produto daquela lista lá de cima, um por um
            # sorte = numero.get()
            
            # # Adiciona o produto (chave) e sua numero (valor) no dicionário
            # participantes[sorte] = nomes[numeros.index(numero)].get()
            querry = f"UPDATE `participante` SET `nome`='{nomes[numeros.index(numero)].get()}' WHERE numero={numero.get()}"
            banco_default(querry)
                                                    
        # Sucesso papai 👌
        messagebox.showinfo("Sucesso", "participantes adicionados com sucesso")
        
        # Fecha o frame de adicionar_participantes
        adicionar_participantes1.destroy()
                    
    # Cria as listas globais pra acessar nas funções (eu sei que é gambiarra, mas é o que tem pra hoje)
    global nomes
    global numeros

    nomes = []
    numeros = []
     
    # Botão que adiciona os campos de texto 
    botao_adicionar = ttk.Button(adicionar_participantes1, text="Adicionar participante", command=adicionar_campo)

    # Botão que salva os participantes no banco
    botao_mostrar = ttk.Button(adicionar_participantes1, text="Salvar", command=salvar)
    
    # Botão que fecha o frame de adicionar_participantes participantes
    botao_voltar = ttk.Button(adicionar_participantes1, text="Voltar", command=lambda:adicionar_participantes1.destroy())
    
    botao_adicionar.place(relx = 0.05 , rely = 0.8, relwidth=0.3, relheight=0.2)
    botao_mostrar.place(relx = 0.35 , rely = 0.8, relwidth=0.3, relheight=0.2)
    botao_voltar.place(relx = 0.65 , rely = 0.8, relwidth=0.3, relheight=0.2)