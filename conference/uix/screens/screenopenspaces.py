from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import webbrowser

class ScreenOpenSpaces(Screen):
    Builder.load_string('''
<ScreenOpenSpaces>
    name: 'ScreenOpenSpaces'
    ScrollView
        ScrollGrid
            AsyncImage
                source: "data/logo/djangogirls.png"
                size_hint_y: None
                allow_stretch: True
                height: dp(100)
                mipmap: True
            BackLabel
                text: "Django Girls é uma oficina de programação gratuita para mulheres. Se você é mulher e quer aprender como fazer websites, vamos realizar uma oficina para iniciantes!"
            BackLabel
                backcolor: 0, 0, 0, 0
                text: "Na programação do Python Nordeste 2018, a Django Girls Campina Grande vai acontecer em 24/05/2018, das 8:45 às 17h. Acreditamos que a área de TI tem muito a ganhar com a entrada de mais mulheres na tecnologia."
            BoxLayout
                size_hint_y: None
                height: dp(50)
                spacing: dp(5)
                ActiveButton
                    text: 'Participe'
                    on_release:
                        webbrowser.open('http://bit.ly/participantesdgPYNE2018')
            BoxLayout
                size_hint_y: None
                height: dp(50)
                spacing: dp(5)
                ActiveButton
                    text: 'Seja mentora'
                    on_release:
                        webbrowser.open('http://bit.ly/mentoresdgPYNE2018')

        ''')
