from PySimpleGUI import PySimpleGUI as sg


url = "https://upload.wikimedia.org/wikipedia/commons/d/d9/Test.png"
response = requests.get(url, stream=True)
response.raw.decode_content = True
# img = ImageQt.Image.open(response.raw)
# data = image_to_data(img)
img_box = sg.Image(data=response.raw.read())

def tela_exibicao():

    sg.theme('DarkBlue2')

    janela = [
        [sg.Image(open("https://drive.google.com/file/d/1bfqXB_KcigWkRwzUZXJCGhxZD7TXaMIb/view?usp=sharing"))]
    ]


    return sg.Window('Login', finalize=True, size=(300,260), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c')