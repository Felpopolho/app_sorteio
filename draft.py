from _bibliotecas import *
    
def sorteio(tela):
    frame()
    
    home = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                    )
    home.place(relx = 0 , rely = 0, relwidth=1, relheight=1)
    
    CTkLabel(tela, text='Sortear ', font=('Arial', 14, 'bold')).place(relx = 0.36 , rely = 0.1)
    qtd_sorteio = CTkEntry(tela).place(relx = 0.46 , rely = 0.11, relwidth=0.1, relheight=0.04)
    CTkLabel(tela, text='números', font=('Arial', 14, 'bold')).place(relx = 0.57 , rely = 0.1)

    CTkLabel(tela, text='Entre ', font=('Arial', 14, 'bold')).place(relx = 0.38 , rely = 0.2)
    start = CTkEntry(tela).place(relx = 0.46 , rely = 0.21, relwidth=0.1, relheight=0.04)
    CTkLabel(tela, text=' e ', font=('Arial', 14, 'bold')).place(relx = 0.57 , rely = 0.2)
    end = CTkEntry(tela).place(relx = 0.61 , rely = 0.21, relwidth=0.1, relheight=0.04)

    result = StringVar()
    result = ''

    sortear = CTkButton(tela, text='Sortear', command=lambda:sorteio(qtd_sorteio, start, end)).place(relx = 0.45 , rely = 0.3, relwidth=0.1, relheight=0.05)

    CTkLabel(tela, text='Resultado:', font=('Arial', 14, 'bold')).place(relx = 0.44 , rely = 0.4)
    CTkLabel(tela, text=result, font=('Arial', 14, 'bold')).place(relx = 0.49 , rely = 0.5)