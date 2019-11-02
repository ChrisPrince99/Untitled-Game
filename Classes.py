from random import randint
import pickle


class Player:
    def __init__(self, name="", level=1, exp=0, exptolvl=100, gold=10, health=100, mana=40,
                 str=5, int=5, end=5, wis=5, dex=5):
        self.name = name
        self.level = level
        self.exp = exp
        self.exptolvl = exptolvl
        self.gold = gold
        self.health = health
        self.mana = mana
        self.str = str
        self.int = int
        self.end = end
        self.wis = wis
        self.dex = dex

    def __str__(self):
        return str(self)

    def __repr__(self):
        return str(self)

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.exptolvl:
            self.level_up()

    def level_up(self):
        if self.level < 50:
            self.level += 1
            self.exptolvl = (self.exptolvl * 1.5)
            str_to_add = randint(1, 5)
            self.str += str_to_add
            int_to_add = randint(1, 5)
            self.int += int_to_add
            end_to_add = randint(1, 5)
            self.end += end_to_add
            wis_to_add = randint(1, 5)
            self.wis += wis_to_add
            dex_to_add = randint(1, 5)
            self.dex += dex_to_add
            health_to_add = (self.health / self.end)
            self.health += health_to_add
            mana_to_add = (self.mana / self.int)
            self.mana += mana_to_add
        elif self.level == 50:
            self.exp = 0
            self.exptolvl = 1

    def save_game(self, save_name, player, backpack, stashbox):
        with open("{}.dat".format(save_name), 'wb') as save_file:
            pickle.dump([player.name, player.level, player.health, player.mana, player.exptolvl, player.gold,
                         player.str, player.int, player.end, player.wis, player.dex, backpack.name, backpack.size,
                         backpack.backpack, stashbox.stash, stashbox.size, stashbox.name], save_file, protocol=2)

    def load_game(self, save_name, player, backpack, stashbox):
        with open('{}.dat'.format(save_name), 'rb') as load_file:
            player.name, player.level, player.health, player.mana, player.exptolvl, player.gold, \
                player.str, player.int, player.end, player.wis, player.dex, \
                backpack.name, backpack.size, backpack.backpack, stashbox.stash, \
                stashbox.size, stashbox.name = pickle.load(load_file)


class Actor:
    def __init__(self, name=""):
        self.name = name


class Enemy(Actor):
    def __init__(self, level=0, exp=0, **kwargs):
        super().__init__(**kwargs)
        self.level = level
        self.exp = exp


class BackPack:
    def __init__(self, name="", size=10):
        self.name = name
        self.size = size
        self.backpack = []

    def __str__(self):
        return str([str(item) for item in self.backpack])

    def __iter__(self):
        return iter(self.backpack)

    def __getitem__(self, item):
        item = self.backpack[item]
        return item

    def __len__(self):
        return len(self.backpack)

    def transfer_to_stash(self, item, stashbox):
        if len(stashbox.stash) <= stashbox.size:
            stashbox.stash.append(item)
        elif len(stashbox.stash) > stashbox.size:
            return "Not enough room in your {}!".format(stashbox.name)

    def pick_up_item(self, item):
        if len(self.backpack) <= self.size:
            self.backpack.append(item)
        elif len(self.backpack) > self.size:
            return "Not enough room in your {}!".format(self.name)

    def drop_item(self, item):
        self.backpack.remove(item)


class StashBox:

    def __init__(self, name="", size=20):
        self.name = name
        self.size = size
        self.stash = []

    def __str__(self):
        return str([str(item) for item in self.stash])

    def __iter__(self):
        return iter(self.stash)

    def __getitem__(self, item):
        item = self.stash[item]
        return item

    def __len__(self):
        return len(self.stash)

    def transfer_to_backpack(self, item, backpack):
        if len(backpack.backpack) <= backpack.size:
            backpack.backpack.append(item)
        elif len(backpack.backpack) > backpack.size:
            return "Not enough room in your {}!".format(backpack.name)


class Item:
    def __init__(self):
        self.items = []
        self.backpacks = []
        self.equipment = []
        self.ore = []
        self.tools = []
        self.key_items = []


class ItemDict:
    def __init__(self):
        self.items = {}
        self.backpacks = {}
        self.equipment = {}
        self.ore = {}
        self.tools = {}
        self.key_items = {}
