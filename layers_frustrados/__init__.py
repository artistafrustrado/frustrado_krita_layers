import krita
from .layersfrustrados import *

#Krita.instance().addExtension((krita.LayersFrustrados.instance()))'
#Krita.instance().addExtension((krita.LayersFrustrados.instance()))

Krita.addExtension(LayersFrustrados(krita.Krita.instance()))

