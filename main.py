"""
Name: Untitled Game Project
Date Started: 1/11/2019
Genre: Undecided
Brief Project Description: My first ever attempt at making a game, yet to be given a title,
 functionality comes before anything else
"""

__author__ = "Christopher J Prince"

import os
import sys
import world_building
from kivy.resources import resource_add_path, resource_find
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.core.window import Window
from Classes import Player
from Classes import BackPack
from Classes import StashBox


class UntitledGameApp(App):

    def __init__(self, **kwargs):
        """
        Construct the game app class
        """
        super().__init__(**kwargs)
        # self.

    def build(self):
        """
        Build the Kivy GUI.
        """
        self.title = "Untitled Game"
        self.root = Builder.load_file('main.kv')
        return self.root

    def press_new_game(self, name):
        self.root.ids.game_box.clear_widgets()
        player = Player(name)

    def press_load(self):
        pass

    def press_save(self):
        pass


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))

    UntitledGameApp().run()
