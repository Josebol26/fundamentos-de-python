import tkinter as tk

janela = tk.Tk()
janela.geometry("600x400")
janela.title('Timer')

# Variável global para controlar os segundos
segundos_restantes = 60  

def atualizar_timer():
    global segundos_restantes
    
    if segundos_restantes >= 0:
        # Divide os segundos em minutos e segundos restantes
        minutos = segundos_restantes // 60
        segundos = segundos_restantes % 60
        
        # Formata para ter sempre dois dígitos (ex: 05:09)
        tempo_formatado = f"{segundos:02d}{" seg"}"
        
        lbl.config(text=tempo_formatado)
        
        # Diminui 1 segundo
        segundos_restantes -= 1
        
        # Agenda a função para rodar de novo em 1000ms (1 segundo)
        lbl.after(1000, atualizar_timer)
    else:
        lbl.config(text="Fim!", fg="red")

# --- Interface ---

# Frame Superior (Onde fica o número)
frame = tk.Frame(janela, bg="lightyellow", bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.4)

# Criando o Label dentro do Frame
lbl = tk.Label(frame, font=('Arial', 50, 'bold'), bg="lightyellow",fg = 'green')
lbl.pack(expand=True)

# Frame Inferior (Onde você pode colocar botões depois)
frame2 = tk.Frame(janela, bg="lightyellow", bd=5)
frame2.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)

# Inicia a função do timer pela primeira vez
atualizar_timer()

janela.mainloop()