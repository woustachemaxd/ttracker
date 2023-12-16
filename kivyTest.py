from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import datetime, csv
import pygetwindow as gw

class MyScreen(BoxLayout):
    orientation = 'vertical'  # Set the orientation to vertical
    
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        
        hex_color = "#171718"  
        rgba_color = [int(hex_color[i:i+2], 16) / 255.0 for i in (1, 3, 5)] + [1.0]  
        Window.clearcolor = rgba_color
        
        self.label = Label(
            text="00hrs 00mins 00secs",
            font_name="dotbold",
            color=(1, 1, 1, 1),
            font_size=67,
        )
        self.label1 = Label(
            text="ZZZ",
            font_name="dotbold",
            color=(1, 1, 1, 1),
            font_size=67,
        )

        self.add_widget(self.label)
        self.add_widget(self.label1)

class MyApp(App):
    def build(self):
        LabelBase.register(name='dotbold', fn_regular='dotbold.ttf')
        Window.size = (500, 150)
        # Window.borderless = True
        root_widget = MyScreen()
        Clock.schedule_interval(self.update_text, 1)
        Clock.schedule_interval(self.update_time, 1)
        return root_widget

    def update_text(self, *args):
        def what_software(title):
            dash_separated = title.split('-')
            if len(dash_separated) > 1:
                return dash_separated[-1]
            else:
                return dash_separated[0]

        active_window = gw.getActiveWindowTitle()
        root_widget = self.root
        root_widget.label.text = what_software(active_window)
        
    def update_time(self, *args):
        def what_software(title):
            dash_separated = title.split('-')
            if len(dash_separated) > 1:
                return dash_separated[-1]
            else:
                return dash_separated[0]
        Dict = {}
        with open('./windowTest.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            table = list(reader)
        for i in range(1, len(table)-1):
            name = what_software(table[i][0]).strip().capitalize()
            if(table[i][2] == 'INF'):
                if(datetime.datetime.strptime(table[i][1], "%Y-%m-%d %H:%M:%S") != datetime.now().date()):
                    continue
                else:
                    end_time = datetime.datetime.now()
            else:
                end_time = datetime.datetime.strptime(table[i][2], "%Y-%m-%d %H:%M:%S")
            start_time = datetime.datetime.strptime(table[i][1], "%Y-%m-%d %H:%M:%S")
            if name != '' and name!= ' ':
                if name not in Dict:
                    Dict[name] = end_time - start_time
                else:
                    Dict[name] += end_time - start_time
        root_widget = self.root
        active_window = gw.getActiveWindowTitle()
        if active_window == '':
            root_widget.label.text = 'HOME'
            root_widget.label1.text = 'ᓚᘏᗢ'
            return
        res = Dict[what_software(active_window).strip().capitalize()]
        if res != None:
            root_widget.label1.text = str(res)
        else: 
            root_widget.label1.text = str(active_window)



if __name__ == '__main__':
    MyApp().run()
