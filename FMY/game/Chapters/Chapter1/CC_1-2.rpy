label CC1_2:

    "I nod, following him into the kitchen. We are quietly unpacking the dishes they brought and putting the finishing touches to the walnut pie when I notice Mikhail sneak a look at me."
    show mikh sad mo at right
    show mc neutral at left
    m "We were thinking of taking you to the wishing tree tomorrow, but… I can always tell them to back off if you are too sick to go."

    menu:
        "Tease him":
            $ points_end_2 += 1
            show mc happy mouth open
            show mikh blushing
            mc "Oh! I’m sure everything will be okay, Prince Charming will come to the rescue if I need him. I’m not worried."
            show mikh annoyed
            m "Wait, you remember that …?"
            show mc happy
            show mikh happy
            mc "How could I forget! you carried me all the way home from Nina’s house despite the snow storm raging outside. You even gave me your coat so I wouldn’t get too sick."
            m "Yeah I remember… Your parents told me I looked like a prince from a fairytale, but honestly… standing there in my wet clothes made me feel like a stray cat more than anything."
            mc "Don’t say that! You really were like a prince, and it was really nice of you to take me home in such a blizzard. I don’t know what I would have done without your help."

        "Reassure him ":
            $ points_end_3 += 1
            show mc neutral mouth open
            show mikh pensive
            mc "Ah, really? Nah, I think I’ll be okay, I really want to get out and have some fun with you guys. You have no idea how boring it is walking around the house all day, only going out to do my chores."
            show mc neutral
            show mikh pensive mo
            m "I understand… Your parents still don’t allow you to go in the forest on your own, huh? I mean… Even though we’re adults now."
            show mc blushing mouth open
            show mikh happy
            mc "I know, right? They still freak out whenever I ask them to let me go pick mushrooms. Maybe they’re afraid of the wild boars that often come and steal our carrots, but it’s too much."
            show mc happy
            show mikh happy mo
            m "Hmm, wild boars you say? We’ll be fine as long as Nina is with us."
            show mc happy mouth open
            mc "I know, right? Once she gives them the death stare, it’s all over. Poor things."
            "We both laugh. It feels like the old times, when we were all neighbours… Going to the same school…"
            show mc neutral
            show mikh pensive mo
            m "Do you hear something?"
            show mc pensive
            show mikh blushing
            mc "No? Should I?"
            show mc happy
            show mikh happy mo
            m "No, it’s silent. It seems they both calmed down. Come on, let’s bring them the food."

    hide mc
    hide mikh
    "When we get back to the living room, Nina and Basilio are sitting next to each other. Basilio is pretending to be asleep, faking loud snores while Nina is mixing a pack of cards in her hands."
    show mc happy at left:
        xalign -0.02
    show nina happy mouth open at center:
        xalign 0.5
    n "Let’s play a game while we have dinner! Hey [mc_name], look - I did the art myself! Do you like them?"
    mc "Sure! Let's play!"

    # fade to black
    scene black with Dissolve (1.0)

    #IF OBTAINED AT LEAST ONE ENDING : Skip the game?

    #[CARD GAME GAMEPLAY : Vecia] Out of game for now

    #"Some lines to add to make the game more alive?"


    #show bas nonchalant
    #n "Basilio, stop looking over everyone’s shoulders."


    #show mikh happy mo at left
    #m "Nina? Did you draw this detail on the back to recognize this card?"

    #show nina embarrassed
    #n "…No."


    #IF MC WINS :


    #"Ha! I win!"

    #n "I was so close…! Ugh, well done."

    #b "It’s time to crown our queen of cards! …Uhh, we don’t have anything to give you, so I guess you’ll have to imagine it."

    #"I lower my head, waiting for my hypothetical reward."

    #"Basilio juggles the imaginary crown with his hands before fake-dropping it dramatically."

    #b "NOOOOO, Careful everyone!"

    #"Nina smacks a hand to her forehead, unamused by the buffoon’s show. Mikhail gestures to catch it mid-air and places it on my head."

    #"I wipe fake tears under my eyes."

    #mc "Thank you, thank you… It’s such a great honor. Now, for my speech-"

    #n "Nope, not this again- I’m going to stop you right there."
    #########################################################################################


    # fade back to the cottage scene
    scene interiorCottage_BG with Dissolve (1.0)

    show mc happy at left:
        xalign -0.02
    show mikh happy at left:
        xalign 0.2
        xzoom -1.0
    show nina happy at center:
        xalign 0.7
    show bas happy at right:
        xalign 1.05

    n "It’s getting late, we better get some sleep before tomorrow’s great escape."
    show mc neutral
    show nina confused Ver2
    show mikh annoyed
    show bas nonchalant
    b "Yeah I agree. So… Mimi? I guess you’ll share the bedroom with [mc_name] tonight… You rascal."
    "Mikhail startles at the remark, flustered. Then he leans in towards Basilio with a sly smirk on his face."
    show mc blushing
    show nina confused Ver2
    show mikh flirty
    show bas shocked ver2
    m "I thought you’d rather spend the night with me, big boy…"
    #(winking)
    show mc happy mouth open
    show nina embarrassed
    show bas happy mo
    b "Ohoho, Now we’re talking! Sorry Nina, duty calls."
    show mc happy
    show mikh happy
    show bas happy
    show nina pissed mouth open
    "Nina sighs and shakes her head, trying to pout in order to hide her smile."
    n "[mc_name], let’s get out of here before they infect us with their stupidity."
    hide mc
    hide nina
    hide mikh
    hide bas
    "We both head to my room and get ourselves ready to go to bed."
    stop music fadeout 1.0

    jump CC1_3