label start:
    scene black
    stop music fadeout 1.0

    label name_select:
        $ mc_name = renpy.input("What's your name?", length=8).lower().title()
        $ mc_name = ' '.join(mc_name.split())
        if mc_name =="":
            $ mc_name = "Primrose"
    if mc_name == "":
        jump name_select
    pause 0.5
    jump CC1_1


label CC1_1:

    #INTRO :
    nvl_narrator "{i}Deep down in the forest,{w=1.5}{nw}{/i}" with Dissolve(1.0)
    nvl_narrator "{i}Where the last green leaf rests,{w=1.5}{nw}{/i}" with Dissolve(1.0)
    nvl_narrator "{i}Your cries will be heard…{/i}" with dissolve

    scene interiorCottage_BG with Fade(1.0,0.0,1.0)
    show mc neutral at center
    mc "Alright, the caramel is done. I’ll do some cleaning while it’s cooling."
    "A faint breeze comes from the open window, making me shiver and reminding me to close them before night."
    "Fall is coming soon. Farewell to the summer’s warmth, the cicada’s songs, and the dances around the bonfire…"
    "I hope mom and dad are resting at their inn, they must be exhausted from walking."
    show mc sad at center
    "I wish I could have gone with them…"
    "They looked so worried, rushing out the door and ranting of a distant family matter. I wanted to go with them, hoping to meet new relatives but I couldn’t."
    #play music "audio/OST/Main.mp3" fadein 1.0
    "This town is the only thing I’ve known my entire life."
    "Since birth, my health has been weak. I wasn’t even allowed to wander past the courtyard."
    "I’m so glad to have my wonderful family and my friends, but… deep inside I long for adventure."
    show mc happy
    "My parents sent word to my friends so that they’ll come visit while they’re away!"
    "I can’t wait, I missed them so much ever since they left to work in the city."
    show mc neutral
    "My hands find the caramel pot but my gaze focuses on the dense forest."
    show mc pensive
    "I catch a shadow moving, past the fence and into the woods. Despite the feeling of being watched, I often find peace picturing myself lost in the middle of that sea of trees."
    "Something catches my eye: a trinket on the window sill. It’s a little bracelet made from daisies."
    show mc happy
    "My parents said that I must have helped a crow when I was little, and that’s where all these little gifts come from."
    "I put it in my pocket as I picture myself as a crow-commanding witch, bringing chaos and gifts in equal measure on my many adventures."
    show mc neutral mouth open
    "Just as I was about to lose myself in my imagination, laughter and chatter brought me back to Earth."
    stop music fadeout 1.0
    hide mc
    play music "audio/OST/Badalisc.mp3" fadein (1.0)
    "???" "My feet huuuuuuuuurt…!"
    "???" "For the Gods’ sake, we’re almost there! Didn’t you tell Simone you were “the strongest man in the valley”?"
    "???" "Fine, I confess…! I LIED to get the job, okay?? How could you blame a DESPERATE man for DESPERATELY wanting a job?!?"
    "???" "Guys, guys! If you don’t keep your voices down, you can kiss our surprise goodbye."
    play music "audio/OST/Cozy.mp3" fadein 1.0
    show mc happy mouth open at center
    "I try not to laugh and fail; they’re still as loud as ever."
    "Our neighbours don’t even waste their time scolding us anymore."
    show mc happy at center
    "I pour the caramel on the sweet shortcrust pastry, humming to myself."
    "As I prepare myself to look surprised by their arrival, someone grabs my shoulder."
    show mc scared at left:
        xalign 0.4
        linear 1.0 xalign -0.05
    show bas happy at right:
        xalign 1.05
    "???" "No way! Don’t tell me you’re making your signature walnut pie? Luckyyy!"
    show mc scared at left:
        xalign -0.05
    mc "Ah-! Basilio, you scared me half to death!"
    "I turn to face my friends."
    show bas happy mo
    b "Surpriiiise! Since you can’t party outside we thought we should bring the parteey to you!"
    show nina happy at left:
        xalign 1.5
        linear 1.0 xalign 0.3
    show mc happy mouth open at left
    "Nina steps up to hug me and I squeeze her back."
    show nina happy at left:
        xalign 0.3
        easein 1.0 xalign 0.5
    "I missed my best friend so much."
    mc "Nina! It’s so good to see you!"
    show mc happy at left
    show nina happy mouth open at center
    n "Glad to see you too, buttercup."
    show nina happy at center
    "Basilio clears his throat to ask for our attention."
    show nina embarrassed
    b "Someone even brought a gift for you~"
    hide bas
    hide nina
    show mikh annoyed at right:
        xalign 1.05
    show mc happy mouth open
    m "Basil, shut up…"
    show mikh blushing at right:
        xalign 1.05
        linear 1.0 xalign 0.4
        xzoom -1
    "Despite the embarrassment, he takes a beautiful handmade package from his basket and gives it to me."
    show mikh pensive mo
    "A beautiful cyan apron unravels itself as I take it in my hands. In the corners, roses and vines intertwine in a deeper shade of green."
    show mc happy mouth open at left
    mc "Oh, Mikhail… This is so pretty! You know how much I love embroideries…"
    show mikh happy
    "Mikhail smiles bashfully, relieved to see his gift being appreciated."
    show bas happy at right:
        xalign 1.05
    b "The poor guy worked on it day and night! You should have seen his concentrated face at the shop."
    show bas lmao
    show mc neutral
    show mikh annoyed
    with hpunch
    b "He looked as if he was about to take a shit…!"
    show bas happy
    #(quietly)
    m "…It was worth it."

    menu:
        "Kiss him on the cheek.":
            $ points_end_2 += 1
            $ flirted_with_mikhail = True

            show mc happy at left:
                xalign 0.0
                linear 1.0 xalign 0.2
            show mikh blushing
            "I get closer while Basilio teases Mikhail and gently press my lips on his cheek, which instantly takes a pinkish color."
            show mc happy at left:
                xalign 0.3
                linear 1.0 xalign 0.0
            show mc happy mouth open
            mc "Thank you Mikhail, this is adorable. I’m glad to see you still love sewing."
            show mikh sad mo
            m "I-I should be the one thanking you for encouraging me to keep going…"
            show mc scared
            show mikh annoyed
            "An awkward silence falls between us, until Bas collapses to the ground. I gasp as he tries to reach for the table."

        "Warmly thank him.":
            $ points_end_1 += 1
            $ points_end_3 += 1
            $ flirted_with_mikhail = False

            show mc happy at left
            "I can’t help but laugh while Basilio teases Mikhail by pinching his reddish cheeks."
            mc "Thank you Mikhail,truly, it’s a very sweet gift."
            m "Don’t mention it, after all… You’re the one who convinced me to become a tailor…"
            "Basilio suddenly falls to the ground. I gasp as he tries to reach for the table."


    show bas shocked ver2
    b "Ugh… I… I’m about to diee… If only I could have tasted a walnut pie for the last time… Even just half of it…!"
    hide bas
    show nina embarrassed:
        xalign 0.65
    n "Basilio… Get off the floor. You’ll be fine."
    show nina pissed
    show mikh blushing
    show mc pensive
    "Basilio walks, or rather crawls to the couch to lay on it."
    "He’s pretending to be unconscious, posing like a damsel in distress from old paintings."
    show nina pissed mouth open
    show mikh blushing
    b "Only a true love’s kiss from my sweet Nina can save me now!"
    show nina embarrassed
    n "Ack- Y-you little… Then I guess you’ll have to die, Bas, ‘cause I’m NOT doing it!"
    hide nina
    hide mikh
    hide bas
    show mc:
        linear 1.0 xalign 0.5
    "Seeing Nina all flustered in front of Basilio warms my heart, their old quarrels turned into love as we grew up."
    show mc happy
    "Honestly, it makes me a little jealous - I don’t have what they have, and if I never leave this place I never will."
    show mc sad head move
    "I look down to hide how I’m feeling. I need to cheer up a little, my friends are here with me, after all."
    "I need to make the most of it."
    show mikh pensive mo:
        xalign 1.05
    show mc:
        linear 1.0 xalign 0.1
    #(whispering)
    m "{i}{size=25}We should leave them alone for a bit, I can help you set the table if you’d like?{/size}{/i}"
    hide mc
    hide mikh

    jump CC1_2
