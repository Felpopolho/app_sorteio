from tkinter import messagebox
import mysql.connector

def banco_select(consulta):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="app_sorteio"
        )
        
        cursor = conn.cursor()

        cursor.execute(consulta)
        resultado = cursor.fetchall()
        
        conn.commit()  
        cursor.close()
        conn.close()

        return (resultado)

    except mysql.connector.Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro: {e}")
        raise  # Levanta a exceção novamente para ser tratada no código que chamou a função
    
def banco_default(querry):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="app_sorteio"
        )
        
        cursor = conn.cursor()

        cursor.execute(querry)

        conn.commit()  
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro: {e}")
        raise  # Levanta a exceção novamente para ser tratada no código que chamou a função
