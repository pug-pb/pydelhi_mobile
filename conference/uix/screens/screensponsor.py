"""ScreenSponsor:
Display all the logos of the sponsors.
"""

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from network import get_data
from kivy.factory import Factory
from kivy.uix.gridlayout import GridLayout


class Sponsor(GridLayout):
    """ This is a simple StackLayout that holds the image
    """
    data = ObjectProperty(None)
    cols = 2


class ScreenSponsor(Screen):

    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
    BoxLayout
        orientation: 'vertical'
        spacing: dp(10)
        id:main
        
<Footer@BoxLayout>
    size_hint_y: None
    padding: dp(9)
    spacing: dp(9)

<Sponsor>
    orientation: 'tb-rl'
    spacing: dp(8)
    size_hint: 1, 1
    BackLabel
        text: self.parent.data['type'] + ': ' + self.parent.data['name']
        size_hint: 1, None
        height: dp(16)
        font_size:dp(14)
    SponsorImage

<SponsorImage@ButtonBehavior+AsyncImage>
    size_hint:1,1
    halign: 'center'
    padding: dp(10), dp(10)
    valign: 'middle'
    allow_stretch:True
    source: self.parent.data['logo']
    on_release:
        import webbrowser
        webbrowser.open(self.parent.data['website'])

''')

    def on_enter(self, onsuccess=False):
        """Series of actions to be performed when Schedule screen is entered
        """

        # this should update the file on disk
        sponsors = get_data('sponsors', onsuccess=onsuccess)
        if not sponsors:
            return

        sponsors = sponsors.get('0.0.1')
        main_box = self.ids.main
        main_box.clear_widgets()
        for s in sponsors:
            bl = Factory.Sponsor(size_hint_y=.8/len(sponsors), data=s)
            main_box.add_widget(bl)
        footer = Factory.Footer()
        main_box.add_widget(footer)

