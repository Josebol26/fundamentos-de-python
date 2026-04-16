import tkinter as tk

janela = tk.Tk()
janela.geometry("600x400")
janela.title('Estrutura do formulário')

frame = tk.Frame(janela, bg="lightblue",width=600)
frame.place(relx=0.1,rely=0.08,relheight=0.15,relwidth=0.8)
a = tk.Label(frame, bg="lightblue", text="Frame Superior")
a.place(relx=0.4,rely=0.4)

frame2 = tk.Frame(janela, bg="green")
frame2.place(relx=0.1,rely=0.28,relheight=0.45,relwidth=0.8)
b = tk.Label(frame2, bg="green", text="Frame do Meio",fg ='white')
b.place(relx=0.4,rely=0.4)

frame3 = tk.Frame(janela, bg="yellow",width=600)
frame3.place(relx=0.1,rely=0.78,relheight=0.15,relwidth=0.8)
c = tk.Label(frame3, bg="yellow", text="Frame Inferior Direito")
c.place(relx=0.4,rely=0.4)

janela.mainloop()