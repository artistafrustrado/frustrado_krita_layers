#import krita
from krita import *
#from krita import *

#Krita.instance().setBatchmode(True)

class LayersFrustrados(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("layers_frustrados", "Layers Frustrados", "tools/scripts")
        action.triggered.connect(self.trigger_layers_frustrados)

    def trigger_layers_frustrados(self):
        trigger_layers_frustrados()

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(LayersFrustrados(Krita.instance()))


def trigger_layers_frustrados():

    doc = Krita.activeDocument()
    root_node = doc.rootNode()

    info = krita.InfoObject()
    info.setProperty("color","#FFFFFF")
    selection = krita.Selection();
    selection.select(0, 0, doc.width(), doc.height(), 255)
    node = doc.createFillLayer("white", "color", info, selection)
    root_node.addChildNode(node, None)
    doc.refreshProjection()

    references = doc.createGroupLayer("references")
    root_node.addChildNode(references, None)

    linework = doc.createGroupLayer("linework")
    root_node.addChildNode(linework, None)

    node_name = "background"
    background = doc.nodeByName(node_name)
    print(background.name())
    background.setVisible(False)

    dupe = background.duplicate()
    dupe.setName("reference")
    dupe.setLocked(True)
    dupe.setOpacity(200)
    dupe.setAlphaLocked(True)
    dupe.setVisible(True)

    references.addChildNode(dupe, None)

    layer = doc.createNode("blacks", "paintLayer")
    linework.addChildNode(layer, None)
    doc.refreshProjection()

    layer = doc.createNode("lineart", "paintLayer")
    linework.addChildNode(layer, None)
    doc.refreshProjection()




    # types
    # paintlayer
    # grouplayer
    # filllayer


    #info = krita.InfoObject()
    #info.setProperty("pattern", "Cross01.pat")
    #selection = krita.Selection();
        #selection.select(0, 0, doc.width(), doc.height(), 255)
    #node = doc.createFillLayer("Pattern", "pattern", info, selection)
    #linework.addChildNode(node, None)
    #doc.refreshProjection()

    # color

    #info = krita.InfoObject()
    #info.setProperty("color","transparent")
    ##info.setProperty("color",(0, 0, 0, 0))
    #selection = krita.Selection();
    #selection.select(0, 0, doc.width(), doc.height(), 255)
    #node = doc.createFillLayer("lineart", "color", info, selection)
    #linework.addChildNode(node, None)
    #doc.refreshProjection()


    # add_new_paint_layer
    # convert_to_paint_layer

    # Document().CreateNode or Krita.instance().openDocument(“tmp/rcpg.svg”)

    #r = doc.rootNode()
    #t = doc.createNode("Transparency Mask", "transparencymask")
    #c = r.childNodes()[0] # I'm always using the "first layer" here
    #c.addChildNode(t, None)
    #doc.refreshProjection()
