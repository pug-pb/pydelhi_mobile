'''uix.pyne2018 module which should house all common widgets.
'''

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class PyNe2018ScreenManager(ScreenManager):
	Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition

<PyNe2018ScreenManager>
	transition: WipeTransition()
''')