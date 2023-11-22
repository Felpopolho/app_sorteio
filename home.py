from _bibliotecas import *
from adicionar_participantes import adicionar_participantes
from sortear_vencedor import sortar_vencedor
from visualizar_participantes import visualizar_participantes


    
def home(tela):
   
    frame()
    home = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                    )
    home.place(relx = 0 , rely = 0, relwidth=1, relheight=1)
    
    botao_adicionar = ttk.Button(home, text="Adicionar participante", command=lambda:adicionar_participantes(tela))
    botao_sortear = ttk.Button(home, text="Sortear vencedor", command=lambda:sortar_vencedor(tela))
    botao_visualizar = ttk.Button(home, text="Visualizar participantes", command=lambda:visualizar_participantes(tela))
    
    botao_sair = ttk.Button(home, text="Sair", command=lambda:tela.destroy())
    
    botao_adicionar.place(relx = 0.38 , rely = 0.2, relwidth=0.3, relheight=0.1)
    botao_sortear.place(relx = 0.38 , rely = 0.4, relwidth=0.3, relheight=0.1)
    botao_visualizar.place(relx = 0.38 , rely = 0.6, relwidth=0.3, relheight=0.1)
    
    botao_sair.place(relx = 0.88 , rely = 0.88, relwidth=0.1, relheight=0.1)
    