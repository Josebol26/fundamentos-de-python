import tkinter as tk

# Função que será chamada ao clicar no botão
def enviar():
    # .get() pega o texto atual das variáveis
    nome = nome_var.get()
    senha = senha_var.get()
    
    print("Email: " + nome)
    print("Senha: " + senha)
    
    # Atualiza o texto da label no frame2
    lbl.config(text="Email: " + nome)
    lbl2.config(text="Senha: " + senha)
    # Limpa os campos após o envio
    nome_var.set("")
    senha_var.set("")

janela = tk.Tk()
janela.geometry("600x400")
janela.title('Ler Entry')

# Variáveis de controle
nome_var = tk.StringVar()
senha_var = tk.StringVar()

# --- Frame 1 (Entrada de Dados) ---
frame = tk.Frame(janela, bg="lightgreen", bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.4)

nome_label = tk.Label(frame, text='Digite seu e-mail:', font=('calibre', 10, 'bold'), bg="lightgreen")
nome_entry = tk.Entry(frame, textvariable=nome_var, font=('calibre', 10, 'normal'))

senha_label = tk.Label(frame, text='Digite sua senha:', font=('calibre', 10, 'bold'), bg="lightgreen")
senha_entry = tk.Entry(frame, textvariable=senha_var, font=('calibre', 10, 'normal'), show='*')

btn_enviar = tk.Button(frame, text='Submit', command=enviar, bg="green", fg="white", font=("Arial", 12), width=10)

# Layout do Frame 1
nome_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
nome_entry.grid(row=0, column=1, padx=10, pady=5)
senha_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
senha_entry.grid(row=1, column=1, padx=10, pady=5)
btn_enviar.grid(row=2, column=1, pady=10)

# --- Frame 2 (Exibição do Resultado) ---
frame2 = tk.Frame(janela, bg="lightgreen", bd=5)
frame2.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)

# Corrigido: adicionado 'tk.' antes de Label e posicionado com pack ou grid
lbl = tk.Label(frame2, font=('calibri', 20, 'bold'), background='lightgreen', foreground='black')
lbl.pack(expand=True, fill="both")
lbl2 = tk.Label(frame2, font=('calibri', 20, 'bold'), background='lightgreen', foreground='black')
lbl2.pack(expand=True, fill="both")


janela.mainloop()
