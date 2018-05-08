from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


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
                text: "Dentro da programação do Python Nordeste 2018, a Django Girls Campina grande vai acontecer em 24/05/2018, das 8:45 às 17h, na UNIFACISA. Acreditamos que a área de TI tem muito a ganhar com a entrada de mais mulheres na tecnologia. Queremos te dar a oportunidade de aprender a programar e se tornar uma de nós - mulheres programadoras! "
        ''')