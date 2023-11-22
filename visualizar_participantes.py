from _bibliotecas import *
from _conn import banco_select

def visualizar_participantes(tela):
            
    # Cria o frame
    frame()
    visualizar_participantes1 = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                      )
    visualizar_participantes1.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.95
                  )
    
    # Scroll bar
    visualizar_participantes = CTkScrollableFrame(visualizar_participantes1,
                    bg_color='silver',
                    fg_color='silver', 
                    corner_radius=25,
                    border_color='black')

    visualizar_participantes.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.70
                  )      
        
    # Função que salva os participantes no banco de dados
      
    # Aqui é onde o filho chora e a mãe não vê...
    querry = f"SELECT * FROM `participante`"
    participantes = banco_select(querry)
    
    for i in range(len(participantes)):
        Label(visualizar_participantes, text=f'{i+1} - {participantes[i][1]}' ,background='silver').pack()
                                                         
    # Botão que fecha o frame de visualizar_participantes participantes
    botao_voltar = ttk.Button(visualizar_participantes1, text="Voltar", command=lambda:visualizar_participantes1.destroy())
    
    botao_voltar.place(relx = 0.65 , rely = 0.8, relwidth=0.3, relheight=0.2)