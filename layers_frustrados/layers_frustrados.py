from krita import *

#Krita.instance().setBatchmode(True)

class LayersFrustrados(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def trigger_layers_frustrados(self, window):
        layers = LayersFrustrados()
        layers.run()

    def createActions(self, window):
#        action = window.createAction("layers_frustrados", "Layers Frustrados", "tools/scripts")
        action = window.createAction("layers_frustrados", "Layers Frustrados")
        action.triggered.connect(self.trigger_layers_frustrados)

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(LayersFrustrados(Krita.instance()))


class LayersFrustrados:

    def __init__(self):
        self._doc = Krita.activeDocument()
        self._root_node = doc.rootNode()

    def run():

#        doc = Krita.activeDocument()
    #    doc = Krita.instance().activeDocument()
#        root_node = doc.rootNode()

        self.createWhiteLayer()
        self.createReferenceLayer()
        self.createReferenceLayer()

    def createWhiteLayer(self):

        info = krita.InfoObject()
        info.setProperty("color","#FFFFFF")
        selection = krita.Selection();
        selection.select(0, 0, self._doc.width(), self._doc.height(), 255)
        node = self._doc.createFillLayer("white", "color", info, selection)
        self._root_node.addChildNode(node, None)
        self._doc.refreshProjection()

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

