all: install

zip:
	zip -r /tmp/draw_frustrado.zip draw_frustrado.desktop draw_frustrado 

install:
	echo "Installing plugin into user's home directory."
	cp -fR layers_frustrados* ~/.local/share/krita/pykrita/
