import tkinter as tk

# Função que será chamada ao clicar no botão
def enviar():
    # .get() pega o texto atual das variáveis
    nome = nome_var.get()
    nasc = nasc_var.get()
    fone = fone_var.get()
    end = end_var.get()
    
    
    print("Nome: " + nome)
    print("Data de Nascimento: " + nasc)
    print("Telefone: " + nome)
    print("Endereço: " + senha)
    
    # Atualiza o texto da label no frame2
    lbl.config(text="Nome: " + nome)
    lbl2.config(text="Data de Nascimento: " + nasc)
    lbl3.config(text="Telefone: " + fone)
    lbl4.config(text="Endereço: " + end)
    # Limpa os campos após o envio
    nome_var.set("")
    nasc_var.set("")
    fone_var.set("")
    end_var.set("")

janela = tk.Tk()
janela.geometry("600x400")
janela.title('Concurso de Bolsas')

# Variáveis de controle
nome_var = tk.StringVar()
nasc_var = tk.StringVar()
fone_var = tk.StringVar()
end_var = tk.StringVar()


# --- Frame 1 (Entrada de Dados) ---
frame = tk.Frame(janela, bg="#000000", bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

nome_label = tk.Label(frame, text='Digite seu nome:', font=('calibre', 10, 'bold'), bg="lightgreen")
nome_entry = tk.Entry(frame, textvariable=nome_var, font=('calibre', 10, 'normal'))

nasc_label = tk.Label(frame, text='Digite a data do seu nascimento:', font=('calibre', 10, 'bold'), bg="lightgreen")
nasc_entry = tk.Entry(frame, textvariable=nasc_var, font=('calibre', 10, 'normal'))

fone_label = tk.Label(frame, text='Digite o número do seu telefone:', font=('calibre', 10, 'bold'), bg="lightgreen")
fone_entry = tk.Entry(frame, textvariable=fone_var, font=('calibre', 10, 'normal'))

end_label = tk.Label(frame, text='Digite o seu endereço:', font=('calibre', 10, 'bold'), bg="lightgreen")
end_entry = tk.Entry(frame, textvariable=end_var, font=('calibre', 10, 'normal'))

btn_enviar = tk.Button(frame, text='Submit', command=enviar, bg="green", fg="white", font=("Arial", 12), width=10)

# Layout do Frame 1
nome_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
nome_entry.grid(row=0, column=1, padx=10, pady=5)
nasc_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
nasc_entry.grid(row=1, column=1, padx=10, pady=5)
fone_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
fone_entry.grid(row=2, column=1, padx=10, pady=5)
end_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
end_entry.grid(row=3, column=1, padx=10, pady=5)
btn_enviar.grid(row=5, column=1, pady=10)




janela.mainloop()
