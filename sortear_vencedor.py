from _bibliotecas import *
from _conn import banco_select
from random import randint 

def sortar_vencedor(tela):
    # Cria o frame
    frame()
    sortear_vencedor = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                      )
    sortear_vencedor.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.95
                  )

    # Label fixa
    Label(sortear_vencedor, text="Vencedor:", font=("arial", 12, "bold")).place(relx = 0.35 , rely = 0.1, relwidth=0.3, relheight=0.2)
    
    # Label que mostra o vencedor
    vencedor = Label(sortear_vencedor, text=f"", foreground="blue", font=("arial", 18, "bold"))
    vencedor.place(relx = 0.25 , rely = 0.3, relwidth=0.5, relheight=0.2)
    
    # Função que sorteia o vencedor
    def sortear():
        # Recupera os participantes do banco de dados
        participantes = banco_select("SELECT * FROM `participante`")
        
        # Sorteia um número aleatório
        numero_sorteado = randint(1, len(participantes))
        
        # Mostra o vencedor
        vencedor["text"] = f'{numero_sorteado} - {participantes[numero_sorteado-1][1]}'
    
    # Botão que sorteia o vencedor
    botao_mostrar = ttk.Button(sortear_vencedor, text="Sortear", command=sortear)
    # Botão que fecha o frame de adicionar_participantes participantes
    botao_voltar = ttk.Button(sortear_vencedor, text="Voltar", command=lambda:sortear_vencedor.destroy())
    
    botao_mostrar.place(relx = 0.35 , rely = 0.5, relwidth=0.3, relheight=0.2)
    botao_voltar.place(relx = 0.88 , rely = 0.88, relwidth=0.1, relheight=0.1)