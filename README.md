Python Nordeste Conference 2018 Application 
===========================================

Inspired and adapted from https://github.com/pydelhi/pydelhi_mobile

> Mobile App for Python Nordeste Conference 2018

![Screenshots from app](screen.png?raw=true "Sreenshots from app")

## Kivy Installation:
- install a XUbuntu Linux VM on Oracle Virtualbox (both Windows and Linux)
  - on downloading Virtualbox: https://www.virtualbox.org/wiki/Downloads
  - on downloading XUbuntu .iso: https://xubuntu.org/download/
  - on installing Virtualbox and creating a VM: https://www.google.com.br/search?q=installing+Virtualbox+and+creating+a+VM&oq=installing+Virtualbox+and+creating+a+VM
  - start the VM and download **kivy-dev-linux.sh** and **need-install.txt** files from this repository
  - open a terminal and run **kivy-dev-linux.sh** (required **need-install.txt** in the same directory)
  - will install Python3.6.3 (miniconda), Kivy 1.10.0, Cython 0.23, Pillow 4.3.0, Buildozer (see need-install.txt)
  - plus, if you like, link to download PyCharm CE in the "kivy-dev-linux.sh" file

## Make sure you build the theme before using the app.
   - clone this repository: `git clone https://github.com/pug-pb/pyne2018app.git`
   - Paste/change your images in pyne2018app/tools/theming
   - Change your directory to pyne2018app
   - Run command ``make theming`` 

### To test install kivy and run the following::
    $ make run

This command will aggregate all the png (pyne2018app/tools/theming/ images) in your file to one atlas
from which the images are loaded and run the app.

## to make apk **prefer linux**

1. Install buildozer: pip install buildozer
2. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step.
3. Connect your mobile, enable usb debugging, Then goto pydelhiconf
   folder and type `make apk`

## to make ipa for ios **(not tested)**

1. Install XCode with latest updates & latest command line tools
2. pip install buildozer
3. goto the app folder and do `buildozer init`
4. edit the buildoze.spec and add details for ios
5. run `buildozer ios debug`

**How to add a screen**

Step 1: Create a new file, add the following Template for a clean Screen

	'''Module XYZ:
	This is the documentation for the Module that explains the
	main usecase of this Module and details it's usage.
	'''

	from kivy.uix.screenmanager import Screen
	from kivy.lang import Builder

	class ScreenSponsor(Screen):
	    '''This is the documentation for the Screen that explains
	    the main usecase of this Screen and details it's usage.
	    '''

	    # Here we define the UI of this screen.
	    Builder.load_string('''
<ScreenSponsor>
	name: 'ScreenSponsor'
	# your Widgets here,  we just use 2 buttons in boxlayout as demo
	BoxLayout
	    Button
	    Button
	''')

Take special note of the names::

    The `name: ScreenSponsor`, in this same as the class name `class ScreenSponsor(...)`.


Step 2: Save the file as `screensponsor.py` in the folder `<pyne2018app/conference/uix/screens>`. Take note to name the file same as the class name,  in our case `ScreenSponsor` in lowercase with .py appended at end.

That's it. Now to load this screen::

    Button:
    	on_release:
            app.load_screen('ScreenSponsor', manager=app.navigation_manager)

`manager=` is a optional parameter, which specifies which `ScreenManager` to load this screen in.
If it is omitted this screen will be loaded into the main Screen Manager Which is responsobile for loading `StartupScreen` and `NavigationScreen`.


***   Enjoy   ***
