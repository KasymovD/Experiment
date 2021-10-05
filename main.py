from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.uix.taptargetview import MDTapTargetView

Builder.load_file('main.kv')

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    content_text = StringProperty("")

class MyLayout(Widget):
    pass

class AwesomeApp(MDApp):
    def build(self):
        Window.size = (360, 640)
        return MyLayout()

    def show_time_picker(self):
        '''Open time picker dialog.'''

        time_dialog = MDTimePicker()
        time_dialog.open()

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

if __name__=="__main__":

    AwesomeApp().run()
