import customtkinter as ctk
import eng_to_ipa as ipa
import pyttsx3

# Configuración de la apariencia
ctk.set_appearance_mode('dark')

# Inicialización del motor de texto a voz
engine = pyttsx3.init()

# Configurar la voz en inglés y ajustar la velocidad
def configurar_voz_ingles():
    for voice in engine.getProperty('voices'):
        if 'en' in voice.languages or 'English' in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 120)  # Ajustar la velocidad de habla (el valor por defecto suele ser 200)

configurar_voz_ingles()

# Funcionalidad principal
def convertir_a_ipa():
    texto_ingresado = entrada_texto.get()
    texto_ipa = ipa.convert(texto_ingresado)
    etiqueta_texto_original.configure(text=texto_ingresado, text_color='white')
    etiqueta_resultado_ipa.configure(text=texto_ipa, text_color='green')
    entrada_texto.delete(0, 'end')

def escuchar_pronunciacion():
    texto_a_hablar = etiqueta_texto_original.cget("text")
    if texto_a_hablar:
        engine.say(texto_a_hablar)
        engine.runAndWait()

# Ventana principal
app = ctk.CTk()
app.title('Convertidor de Texto a IPA')
app.geometry('600x250')

# Etiquetas y campo de entrada
etiqueta_texto = ctk.CTkLabel(app, text='Texto para convertir:')
etiqueta_texto.pack(pady=5)

entrada_texto = ctk.CTkEntry(app, placeholder_text='Escribe tu texto aquí', width=500)
entrada_texto.pack(pady=10)

# Botones
boton_convertir = ctk.CTkButton(app, text='Convertir a IPA', command=convertir_a_ipa)
boton_convertir.pack(pady=10)

boton_escuchar = ctk.CTkButton(app, text='Escuchar Pronunciación', command=escuchar_pronunciacion)
boton_escuchar.pack(pady=10)

# Etiquetas de resultado
etiqueta_texto_original = ctk.CTkLabel(app, text='')
etiqueta_texto_original.pack(pady=0)

etiqueta_resultado_ipa = ctk.CTkLabel(app, text='')
etiqueta_resultado_ipa.pack(pady=0)

# Ejecutar la aplicación
app.mainloop()
