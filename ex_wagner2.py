import CustomTkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("drak-blue")

window = customtkinter.CTk()
window.geometry('500x300')

def clique():
    print("Login efuteuado com sucesso")

text = custmtkinter.CTkLabel(window,text='Usuário')
text.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(window, placeholdertext = "seu usuário")
email.pack(padx=10,pady=10)

senha = customtkinter.CTkEntry(window, placeholdertext = "Senha", show = '*')
senha.pack(padx=10,pady=10)

button = customtkinter.CTkButton(window, text='Entrar', command=clique())
button.pack(padx=10, pady=10)

window.mainloop()