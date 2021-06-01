from krita import *
#import krita *

## And add the extension to Krita's list of extensions:
Krita.instance().addExtension(krita.LayersFrustrados.instance())

class LayersFrustrados:

    def __init__(self, Krita):
        print("__init__ 01")
        self._doc = krita.Krita.instance().activeDocument()
        self._root_node = self._doc.rootNode()
        print("__init__")

    def run(self):

#        doc = Krita.activeDocument()
        doc = krita.Krita.instance().activeDocument()
        root_node = doc.rootNode()

        print("run")

        self.createWhiteLayer()
        self.creatererenceLayer()
        self.createRelineworksLayer()

    def createWWiteLayer(self):

        info = krita.InfoObject()
        info.setProperty("color","#FFFFFF")
        selection = krita.Selection();
        selection.select(0, 0, self._doc.width(), self._doc.height(), 255)
        node = self._doc.createFillLayer("white", "color", info, selection)
        self._root_node.addChildNode(node, None)
        self._doc.refreshProjection()

        print("white")

    def createReferenceLayer(self):

        references = self._doc.createGroupLayer("references")
        self._root_node.addChildNode(references, None)

        node_name = "background"
        background = self._doc.nodeByName(node_name)
        background.setVisible(False)

        dupe = background.duplicate()
        dupe.setName("reference")
        dupe.setLocked(True)
        dupe.setOpacity(200)
        dupe.setAlphaLocked(True)
        dupe.setVisible(True)

        references.addChildNode(dupe, None)


    def createLineworkLayer(self):

        linework = self._doc.createGroupLayer("linework")
        self._root_node.addChildNode(linework, None)

        layer = self._doc.createNode("blacks", "paintLayer")
        linework.addChildNode(layer, None)
        self._doc.refreshProjection()

        layer = self._doc.createNode("lineart", "paintLayer")
        linework.addChildNode(layer, None)
        self._doc.refreshProjection()
    
        print("/////////////////////////////")

