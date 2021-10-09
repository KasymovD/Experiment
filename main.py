from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatIconButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.picker import MDTimePicker
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.taptargetview import MDTapTargetView

KV = open('main.kv', 'r').read()



class ContentNavigationDrawer(MDBoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    content_text = StringProperty("")


class MyApp(MDApp):
    def dob(self):
        # box = MDRectangleFlatIconButton(
        #         icon= "account-multiple",
        #         text= 'Шоро',
        #         theme_text_color= "Custom",
        #         text_color= (0,0,0,1),
        #         line_color= (0,0,0,0),
        #         icon_color= (0,0,0,1),
        #         pos_hint={"center_x": 0.4, "center_y": .88},
        #         size_hint=(2,0.08),
        #     )
        # self.root.ids.tatar.add_widget(box)
        pass

    def build(self):
        Window.size = (360, 640)
        return Builder.load_string(KV)


    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

    # def on_start(self):
        # self.root.ids.tabs.add_widget(Tab(text="One"))
        # self.root.ids.tabs.add_widget(Tab(text="Two"))
        # self.root.ids.tabs.add_widget(Tab(text="One"))
        # self.root.ids.tabs.add_widget(Tab(text="Two"))



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

    MyApp().run()
