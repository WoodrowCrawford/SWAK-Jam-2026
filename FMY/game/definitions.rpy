
## This file contains the definitions for the game, including variables and character definitions.

default mc_name = ""

default flirted_with_mikhail = False
default points_end_1 = 0
default points_end_2 = 0
default points_end_3 = 0
default points_secret_info = 0

default accepted_drink = False

## Character Definitions
define h = Character("Hicetia")
define b = Character("Basilio")
define mc = Character("[mc_name]")
define m = Character("Mikhail")
define n = Character("Nina")
define nl = Character("Noble Lady")


#transforms
transform offscreenLeft1:
    xalign -0.3

transform left1:
    xalign 0.1

transform left2:
    xalign 0.2

transform left3:
    xalign 0.3

transform left4:
    xalign 0.4


transform right1:
    xalign 0.6

transform right2:
    xalign 0.7

transform right3:
    xalign 0.8

transform right4:
    xalign 0.9

transform offscreenRight:
    xalign 1.8


init python:
    def get_current_position(image_tag):
        return renpy.get_at_list(image_tag)
