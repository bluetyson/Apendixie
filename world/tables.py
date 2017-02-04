# This file contains all the tables
# lets get one working
# table 1

TABLES = [
    ("I", "Periodic Check", [
        # Periodic Check
        # (min, max, "result_name", "description")
        (1, 2, "Continue Straight",
            " -- check again in 60' (this table)"),
        (3, 5, "Door", """(see Table II.)
            <actually roll on Table II.a first, then II.b>"""),
        (6, 10, "Side Passage",
            """(see Table III.) -- check again in 30'
            (this table)"""),
        (11, 13, "Passaeg Turns",
            """(see Table IV., check width on Table III.)
            check again in 30' (this table)"""),
        (14, 16, "Chamber",
            """(See Table V.) -- check 30' after leaving
            (this table)"""),
        (17, 17, "Stairs", "(see Table VI.)"),
        (18, 18, "Dead End",
            """(walls left, right, and ahead can be checked for Secret
            Doors, see Table V.D., footnote)"""),
        (19, 19, "Trick/Trap",
            """(See Table VII.), passage continues -- check again in
            30' (this table)"""),
        (20, 20, "Wandering Monster",
            """-- check again immeditately to see what lies ahead
            so direction of monster's approach can be determined."""),
        ]),
    ("II.a", "Location of Door", [
        # Doors location relative to passage
        (1, 6, "Left", "<door is on left side of passage>"),
        (7, 12, "Right", "<door is on right side of passage>"),
        (13, 20, "Ahead", "<passage comed to and end at this door>"),
        ]),
    ("II.b", "Space Beyond Door is:", [
        # space beyond door
        (1, 4, "Parallel passage**",
            """or 10' x 10' room if door is straight ahead.
            """),
        (5, 8, "Passage straight ahead",
            """<<What's the point then really?>>"""),
        (9, 9, "Passage 45 degrees ahead/behind***",
            """***The direction will be appropriate to existing circumstances,
            but use the direction before the slash in preference to the
            other."""),
        (10, 10, "Passage 45 degrees behind/ahead***",
            """***The direction will be appropriate to existing circumstances,
            but use the direction before the slash in preference to the
            other."""),
        (11, 18, "Room", "(Go to Table V.room)"),
        (19, 20, "Chamber", "(Go to Table V.chamber)"),
        ])
    ]
