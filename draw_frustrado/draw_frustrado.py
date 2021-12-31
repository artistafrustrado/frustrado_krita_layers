# BBD's Krita Script Starter Feb 2018

from krita import Extension
from krita import * 

EXTENSION_ID = 'pykrita_draw_frustrado'
MENU_ENTRY = 'Draw Frustrado'


class Draw_frustrado(Extension):

    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)
        print("Run")

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(EXTENSION_ID, MENU_ENTRY, "tools/scripts")
        # parameter 1 = the name that Krita uses to identify the action
        # parameter 2 = the text to be added to the menu entry for this script
        # parameter 3 = location of menu entry
        action.triggered.connect(self.action_triggered)

    def action_triggered(self):
#        pass  # your active code goes here.
        print("Draw frustrado")
        
        doc = krita.Krita.instance().activeDocument()
        root_node = doc.rootNode()

        self._doc = krita.Krita.instance().activeDocument()
        self._root_node = doc.rootNode()

        print("run")

        self.createWhiteLayer()
        self.createReferenceLayer()
        self.createLineworkLayer()

    def createWhiteLayer(self):

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

        node_name = "Background"
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
