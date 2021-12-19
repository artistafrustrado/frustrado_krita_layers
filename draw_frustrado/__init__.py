from .draw_frustrado import Draw_frustrado

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = Draw_frustrado(parent = app)
app.addExtension(extension)
