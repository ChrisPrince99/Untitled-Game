"""
Name: Untitled Game Project
Date Started: 1/11/2019
Genre: Undecided
Brief Project Description: My first ever attempt at making a game, yet to be given a title,
 functionality comes before anything else
"""

__author__ = "Christopher J Prince"

import logging
import os
import sys
# import world_building
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.resources import resource_add_path

from Classes import BackPack
from Classes import Player
from Classes import StashBox


class UntitledGameApp(App):
    current_scene = StringProperty()
    DATE = datetime.now()
    LOG_FILENAME = "{}.log".format(DATE)
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

    def __init__(self, player=Player(), player_backpack=BackPack(), player_stash=StashBox(), **kwargs):
        """
        Construct the game app class
        """
        super().__init__(**kwargs)
        self.player = player
        self.player_backpack = player_backpack
        self.player_stash = player_stash
        self.game_started = False
        # self.

    def build(self):
        """
        Build the Kivy GUI.
        """
        self.title = "Untitled Game"
        self.root = Builder.load_file('main.kv')
        self.current_scene = "Welcome to my game please choose either New game or Load game."
        return self.root

    def press_new_game(self):
        self.root.ids.new_game_choice.open()

    def press_start_game(self, added_name, save_name):
        self.root.ids.game_box.clear_widgets()
        self.player = Player(added_name)
        self.player_backpack = BackPack("Basic Bag", 10)
        self.player_stash = StashBox("Chest", 20)
        self.player.save_game(save_name, self.player, self.player_backpack, self.player_stash)
        self.game_started = True
        self.press_cancel()

    def press_load(self):
        self.root.ids.load_game_choice.open()

    def press_load_game(self, save_name):
        try:
            self.player.load_game(save_name, self.player, self.player_backpack, self.player_stash)
        except Exception as e:
            logging.exception("Load failed. Error: %s", e)
        self.root.ids.game_box.clear_widgets()
        self.game_started = True
        self.press_cancel()

    def press_save(self, save_name):
        self.player.save_game(save_name, self.player, self.player_backpack, self.player_stash)

    def on_stop(self):
        if self.game_started:
            try:
                self.player.save_game("Autosave", self.player, self.player_backpack, self.player_stash)
            except Exception as e:
                logging.exception("main crashed. Error: %s", e)

    def clear_fields(self):
        """
        Clear the text input fields from the add entry popup
        If we don't do this, the popup will still have text in it when opened again
        :return: None
        """
        self.root.ids.added_name.text = ""
        self.root.ids.save_name.text = ""

    def press_cancel(self):
        """
        Handler for pressing cancel in the add entry popup
        :return: None
        """
        self.root.ids.new_game_choice.dismiss()
        self.root.ids.load_game_choice.dismiss()
        self.clear_fields()
        # self.status_text = ""

    def clear_all(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    try:
        UntitledGameApp().run()
    except Exception as e:
        logging.exception("main crashed. Error: %s", e)
