import time

message = [
    "Hola, soy el tio y tu?",
    "Encantado de conocerlo",
    "Como estas?",
    "Me alegro de que estes bien",
    "¡Cuidado! Has usado una palabra advertida. Esto es tu 1ª advertencia.",
    "A que te dedicas?",
    "Eso es genial",
    "O es un buen lugar para quedarse",
    "Creo que eres una buena persona",
    "Por que piensas eso?",
    "Puedes explicar?",
    "De todos modos tengo que irme ahora",
    "Fue un placer charlar contigo",
    "Es hora de crear un nuevo codepen",
    "Adios",
    ":)"
]

scrollctr = 200
i = 0


def scroll_update():
    global scrollctr
    last_element_top = display_position()
    scroll_amount = last_element_top + scrollctr
    scrollctr += 200
    display_scroll(scroll_amount)


def display_position():
    # Simulando la posición del elemento en la pantalla
    return 0


def display_scroll(amount):
    # Simulando el desplazamiento de la pantalla
    print(f"Desplazando a {amount}")


def msngr(msg):
    display_append(f"<div class='msg'><p>{msg}</p></div>")
    # Limpiar el campo de entrada
    text_input_clear()


def reply():
    global i
    if i >= 15:
        i = 15
    display_append(f"<div class='reply'><p>{message[i]}</p></div>")
    i += 1


def loader():
    display_append("<div class='lds-ellipsis'><div></div><div></div><div></div><div></div></div>")


def display_append(content):
    # Simulando la adición de contenido al elemento de visualización
    print(f"Añadiendo contenido: {content}")


def text_input_clear():
    # Simulando la limpieza del campo de entrada
    print("Limpiando campo de entrada")


# Simulando eventos de clic y teclado
msngr("Hola, soy el tio y tu?")
time.sleep(1)
loader()
time.sleep(1.6)
display_fade_out()
reply()

scroll_update()

# Aquí puedes continuar simulando los demás eventos según sea necesario
