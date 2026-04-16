import tkinter as tk

janela = tk.Tk()
janela.geometry("600x400")
janela.title('Estrutura Base')

frame = tk.Frame(janela, bg="lightblue",width=600)
frame.place(relx=0.0,rely=0.0,relheight=1,relwidth=0.2)
a = tk.Label(frame, bg="lightblue", text="Frame Esquerdo")
a.place(relx=0.3,rely=0.1)

frame4 = tk.Frame(janela, bg="green")
frame4.place(relx=0.2,rely=0.0,relheight=0.1,relwidth=0.8)
b = tk.Label(frame4, bg="green", text="Página de código",fg='white')
b.place(relx=0.5,rely=0.1)

frame2 = tk.Frame(janela, bg="lightgreen")
frame2.place(relx=0.2,rely=0.1,relheight=0.7,relwidth=0.8)
b = tk.Label(frame2, bg="lightgreen", text="Frame Direito")
b.place(relx=0.5,rely=0.1)

frame3 = tk.Frame(janela, bg="yellow",width=600)
frame3.place(relx=0.2,rely=0.8,relheight=0.2,relwidth=0.8)
c = tk.Label(frame3, bg="yellow", text="Frame Inferior Direito")
c.place(relx=0.5,rely=0.8)

janela.mainloop()
