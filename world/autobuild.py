"Builder Menu"
# from collections import OrderedDict
from evennia.utils.evmenu import EvMenu
from commands.command import MuxCommand
from tables import GYGAX, rolltable
# from tables import GYGAX, rolltable, gettable
# TODO: In future, Choose different tablesets, perhaps based on major zone
# divisions.


def menunode_start(caller):
    print "\nmenunode_Started\n"
    table = caller.ndb._menutree.table
    caller.ndb._menutree.table = ""
    override = caller.ndb._menutree.override
    caller.ndb._menutree.override = ""
    print "table = %s" % table
    print "override= %s" % override

    results = rolltable(GYGAX, table, override)
    dieroll = results[0]
    name = results[1]
    desc = results[2] or None
    recipe = results[3] or None
    caller.ndb._menutree.recipe = recipe
    print (dieroll, name, desc, recipe)
    # table is a string name of a known table
    # override is optional and sets a particular result
    text = "You rolled a %s on table %s " % (dieroll, table)
    text += "resulting in a %s" % name
    text += "\n %s" % desc
    text += "\n Build recipe:\n----------------\n"
    report = ""
    try:
        text += '\n'.join(recipe)
    except TypeError:
        report = "Type error in recipe"
        print report
    except:
        report = "Do you even have a recipe"
        print report

    caller.msg(report)

    options = ({"key": ("A", "a"),
                "desc": "Accept Destiny's Edict",
                # "goto": "menunode_process",
                "exec": _process,
                "goto": "menunode_end"
                },
               {"key": ("F", "f"),
                "desc": "Flout fickle Fortune",
                "goto": "menunode_manual"},
               {"key": ("C", "c"),
                "desc": "Cancel and move back",
                "goto": "menunode_end",
                "exec": _cancel_it})
    return text, options


def _cancel_it(caller):
    text = "You tried to cancel and moved back"
    # caller.execute_cmd("move back")
    caller.msg(text)
    return menunode_end


def _process(caller):
    """
    This collects the build commands and adds them to the manifest. If there
    are new table flags they will be reused on this node. Only when there are
    no more flags will the manifest be run.  That means the manifest could
    contain build commands from several tables.
    """
    recipe = caller.ndb._menutree.recipe
    next_table = ""
    next_node = "menunode_end"
    text = ""
    manifest = []
    for line in recipe:
        "check for @autobuild and remove it. There should be only one."
        if "@autobuild" in line:
            next_table = line.replace("@autobuild ", "")
            text += "Next table: %s" % next_table
        else:
            # caller.msg("appending line: %s" % line)
            manifest.append(line)

    "execute each command in manifest"
    for cmd in manifest:
        caller.execute_cmd(cmd)
        caller.msg("executed %s" % cmd)

    if next_table:
        caller.ndb._menutree.table = next_table
        next_node = "menunode_start"

    return next_node

'''


def menunode_clean(caller):
    """
    This should remove the cached user input
    before restarting the menu.
    """
    text = "Cleaning up! Press enter to continue."
    options = ({"desc": "Carry on!",
                "key": "_default",
                "goto": "menunode_start"})
    # caller.msg("Passing through the clean cycle!")
    return text, options

'''


def menunode_end(caller):
    "End of the menu"
    text = "Successfully closed menu"
    # caller.ndb._menutree.table = None
    return text, None
'''

def menunode_table(caller, table_no):
    """ Display all table entries in a menu, allowing player to choose any one
    by number."""
    table = gettable(GYGAX, table_no)
    # TODO make this work for all tables
    # title, die, list
    # list = name, desc, build

    # "I": ["PERIODIC CHECK", 20, [  # table name, die size
    #    (1, 2, "Continue Straight",  # low, high dice, result
    #       """
    #        -- check again in 60' (this table)""",  # desc
    #        ["@tun f", "@name here = Straight Passage"]),  # build list
    # so, the menu needs the name, desc, and build list for every item in the
    # table.
    #
    # options: name, desc, exec, goto
    menu = OrderedDict(table[2])
    title = table[0]
    options = ()
    for i in menu:
        name = i[2]
        desc = i[3]
        build = i[4]
        options.append({"name": name,
                        "desc": desc,
                        "build": build})
        text = "A menu of all options on Table %s: %s" % (table_no, title)

    return text, options

'''


class CmdAutoBuild(MuxCommand):
    """
    Automatic Build command

    This is automatically called when you enter an unfinished node.

    Idea: with arguments you can choose a particular table and even over ride
    the die-roll or result. (two separate things)
    This means the command itself can be used to navigate the tables

    """
    key = "@autobuild"

    def func(self):
        '''
        '''
        print "CmdAutoBuild started"

        table = ''
        override = None

        if self.lhs:
            table = self.lhs
            print "table = %s" % table
        else:
            table = "I"  # default to periodic check
            print "Using default periodic check"
        if self.rhs:
            override = self.rhs
            print "override = %s" % override

        # Start Menu
        EvMenu(self.caller,
               "world.autobuild",
               startnode="menunode_start",
               cmdset_mergetype="Union", cmdset_priority=1,
               auto_quit=True, auto_look=True, auto_help=True,
               cmd_on_exit="look",
               persistent=False,
               table=table,
               override=override
               )
