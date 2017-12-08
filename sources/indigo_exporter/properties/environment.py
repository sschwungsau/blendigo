import bpy

lightlayer_data_properties = [
    {
        'type': 'bool',
        'attr': 'lg_enabled',
        'name': '',
        'description': 'Enable this light layer',
        'default': True
    },
    {
        'type': 'string',
        'attr': 'name',
        'name': ''
    },
    {
        'type': 'float',
        'attr': 'gain',
        'name': 'Gain',
        'description': 'Overall gain for this light layer',
        'min': 0.0,
        'soft_min': 0.0,
        'default': 1.0,
        'precision': 4
    }
]

from .. import export
from . import register_properties_dict
@register_properties_dict
class Indigo_Lightlayer_Data_Properties(bpy.types.PropertyGroup, export.xml_builder):
    properties = lightlayer_data_properties
    
''' # needs to be put somewhere else
    {
        'type': 'operator',
        'attr': 'op_lg_add',
        'operator': 'indigo.lightlayer_add',
        'text': 'Add',
        'icon': 'ZOOMIN',
    },
'''
lightlayers_properties = [
    {
        'type': 'collection',
        'ptype': Indigo_Lightlayer_Data_Properties,
        'name': 'lightlayers',
        'attr': 'lightlayers',
        #'items': []
    },
    {
        'type': 'int',
        'name': 'lightlayers_index',
        'attr': 'lightlayers_index',
    },
    {
        'type': 'bool',
        'attr': 'ignore',
        'name': 'Merge LightLayers',
        'description': 'Enable this for final renders, or to decrease RAM usage.',
        'default': False
    },
    {
        'type': 'float',
        'attr': 'default_gain',
        'name': 'Gain',
        'description': 'Gain for the default light layer',
        'default': 1.0,
        'min': 0.0,
        'soft_min': 0.0,
        'precision': 4
    }
]

@register_properties_dict
class Indigo_Lightlayers_Properties(bpy.types.PropertyGroup):
    properties = lightlayers_properties
    
    def gain_for_layer(self, name):
        ll_gain = self.default_gain
        if name in self.lightlayers:
            ll_gain = self.lightlayers[name].gain
        return ll_gain
    
    def is_enabled(self, name):
        if name != '' and name in self.lightlayers:
            return self.lightlayers[name].lg_enabled
        return True
    
    def enumerate(self):
        en = {
            'default': 0,
        }
        if not self.ignore:
            idx = 1
            for name, lyr in self.lightlayers.items():
                if lyr.lg_enabled:
                    en[name] = idx
                    idx += 1
        return en
    