
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from devslib.utils import ImageButton

import os

class Zero(FloatLayout):
    
    covers = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(Zero, self).__init__(**kwargs)
        
        for i in os.listdir('covers'):
            imagepath = os.path.join('covers', i)
            print imagepath
            self.covers.add_widget(ImageButton(size_hint_x=None, width=200, source=imagepath ))
    
if __name__ == '__main__':
    from kivy.app import App
    
    class ZeroApp(App):
        def build(self):
            return Zero()
            
    ZeroApp().run()
