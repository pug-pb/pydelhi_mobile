Python Nordeste Conference 2018 Application 
===========================================

Inspired and adapted from https://github.com/pydelhi/pydelhi_mobile

> Mobile App for Python Nordeste Conference 2018

![Screenshots from app](screen.png?raw=true "Sreenshots from app")

## Kivy Installation:

- install a XUbuntu (recomended) Linux VM on Virtualbox or VMWare (both Windows and Linux)
  - on downloading Virtualbox and Extension Pack: https://www.virtualbox.org/wiki/Downloads
  - on downloading XUbuntu .iso: https://xubuntu.org/download/
  - on installing Virtualbox, Extension Pack and creating a VM: https://duckduckgo.com/?q=installing+Virtualbox+and+creating+a+VM
  - on installing XUbuntu in VM: https://duckduckgo.com/?q=installing+xubuntu+18.04+in+virtualbox
  - setup the VM with your preferences (large memory, large memory video, bi-directional clipboard, for example)
  - after installing XUbuntu, restart the VM
  - open a terminal and install git: `sudo apt install git`
  - clone this repository: `git clone https://github.com/pug-pb/pyne2018app.git`
  - go to pyne2018app (or another name you prefer) folder: `cd pyne2018app`
  - run **kivy-dev-linux.sh** (required **need-install.txt** in the same directory): `./kivy-dev-linux.sh`
  	- pay atention about the pauses at each phase of install and press <ENTER>
	- every phase take time, and patiente are required, but remember, it's just one time. (meanwhile I'm listening Sonic Youth)
  	- will install Python 3.6.x (miniconda), Kivy 1.10.0, Cython 0.23, Pillow 4.3.0, Buildozer (see need-install.txt)
  	- plus, if you like, link to download PyCharm CE in the "kivy-dev-linux.sh" file
  - (optional) install Virtualbox Guest Addictional CD:
  	- mount CD via menu
	- go to media folder (in my example it's /media/develop/VBox_GAs_5.2.2/)
	- go to root: `sudo su -`
	- run installer: `./VBoxLinuxAdditions.run`

### To activate kivy environment

   $ source activate kivy3

### To test install run the following::
   
   $ make run

   - Paste/change your images in pyne2018app/tools/theming folder
   - This command will aggregate all the png (pyne2018app/tools/theming/ images) in your file to one atlas
from which the images are loaded and run the app.

## to make apk **prefer linux**

1. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step. (first run it is take very much time)
2. Connect your mobile, enable usb debugging, Then goto pyne2018app
   folder and type `make apk`

## to sign the released apk **prefer linux**

1. Build the release: `make apk_release`
2. With the result apk in bin folder, adapt, if necessary, and run **assign-apk.sh**: `./assign-apk.sh`

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
