# adapt to your preferred python version
# using a miniconda virtualenv with Python 3.6, but naming python
PYTHON = python
# needs kivy installed or in PYTHONPATH

.PHONY: theming apk clean

theming:
	$(PYTHON) -m kivy.atlas conference/data/default 1024 tools/theming/*.png
run: theming
	$(PYTHON) conference/main.py -m screen:droid2,portrait -m inspector
apk:
	buildozer android debug
apk_release:
	buildozer android release
