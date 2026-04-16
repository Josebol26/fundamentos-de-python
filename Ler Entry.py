import tkinter as tk

# Função que será chamada ao clicar no botão
def enviar():
    # .get() pega o texto atual das variáveis
    nome = nome_var.get()
    senha = senha_var.get()
    
    print("O nome é: " + nome)
    print("A senha é: " + senha)
    
    # Limpa os campos após o envio
    nome_var.set("")
    senha_var.set("")

janela = tk.Tk()
janela.geometry("600x400")
janela.title('Ler Entry')

# Criando as variáveis de controle (com parênteses!)
nome_var = tk.StringVar()
senha_var = tk.StringVar()

# Criando um Frame (moldura) para organizar o layout
frame = tk.Frame(janela, bg="lightgreen", bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

# --- Widgets dentro do Frame ---

# Rótulo e Campo de Entrada para o E-mail
nome_label = tk.Label(frame, text='Digite seu e-mail:', font=('calibre', 10, 'bold'), bg="lightgreen")
nome_entry = tk.Entry(frame, textvariable=nome_var, font=('calibre', 10, 'normal'))

# Rótulo e Campo de Entrada para a Senha
senha_label = tk.Label(frame, text='Digite sua senha:', font=('calibre', 10, 'bold'), bg="lightgreen")
senha_entry = tk.Entry(frame, textvariable=senha_var, font=('calibre', 10, 'normal'), show='*')

# Botão de Envio
btn_enviar = tk.Button(frame, text='Enviar', command=enviar)

# --- Organização usando Grid (Grade) dentro do Frame ---
nome_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
nome_entry.grid(row=0, column=1, padx=10, pady=10)

senha_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
senha_entry.grid(row=1, column=1, padx=10, pady=10)

btn_enviar.grid(row=2, column=1, pady=20)

janela.mainloop()