all: install

install:
	echo "Installing plugin into user's home directory."
	cp -fR layers_frustrados* ~/.local/share/krita/pykrita/
