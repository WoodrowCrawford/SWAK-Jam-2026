label CC1_5:

    scene morning_CG with Dissolve (1.0)
    play music "audio/SFX/morningsfxhouse.mp3" fadein 1.0 #Credits for now : SFXHOUSE
    play sound "audio/sfx/Bedsheet2.mp3"
    n "Hey sleepy-head, are you alright?"
    "I stir up from slumber, feeling her warm hand on my forehead brushing away strands of hair."
    n "You were shaking head to toes, buttercup."
    mc "Oh… It was just a nightmare, sorry to worry you. I’m okay now."
    n "Okay… If you say so."
    "I quickly get up, avoiding any further prying."
    mc "Are the boys still sleeping?"
    n "Snoring up a storm, as usual. Basil rolled over and crushed Mikhail, so I doubt he will be breathing for much longer."
    #(laughing)
    mc "I’d love to save him but alas, I have chores to do before leaving. We should let them rest while they can."
    n "It’ll be faster if I help, so let me know what I can do."
    mc "Thank you. I already cleaned the house yesterday so I only need to go check on the chickens this morning."

    scene exteriorCottage_BG with Dissolve(1.0)
    "Nina and I both take a basket and go outside, where chickens are hunting for worms. Their feathers, covered in morning dew’s pearls, make their warm colors brighter."

    show mc happy:
        left2
    show nina happy:
        right3
    with dissolve
    "I crouch to pet some of them, gently brushing off their heads and petting little chicks in my hands while Nina is fetching fresh eggs from their nests in the coop."
    "I look around and choose one of the chickens that has not been laying as much as she used to, and I wrap my hand around her neck and take her back to the kitchen."

    show mc happy mouth open
    mc "You can put the eggs over there, thank you Nina."

    show mc happy
    "I lay the chicken on the table, and hold it down with one hand as she squirms under the pressure. I grab the cleaver and swiftly put an end to it."
    show nina terrified
    # play knife sound here
    # maybe add a red screen shake effect here
    show screen red_screen
    play sound "audio/SFX/Knife_Splatter.mp3"
    #stop music fadeout 0.5
    stop music fadeout 0.5
    pause 0.9
    show nina sad
   
    "Warm blood splashes on my face as I look at the last spasm of what was just seconds before a living creature. I watch the blood pool into a little basin, waiting patiently for the carcass to bleed out."
    show mc neutral
    n "Urgh… I don’t know how you can do that so easily… I always ask Basilio to do it…"
    #(laughing coldly)
    show mc pensive
    mc "Why? Roast chicken is your favourite. This is a necessary step for that, don’t you think?"
    show nina confused Ver2
    show nina happy
    n "You’re not wrong, but still… Ugh, I’m gonna be sick. I’m going to go pick up some herbs."
    hide nina
    show mc at center
    "I nod as Nina hurries out the door, and I move the basin out of the way to start cleaning the bird."
    show mc pensive worried
    play music "audio/OST/creepy.mp3" fadein 1.0
    "As I silently pluck the feathers off its body, an uneasy feeling crawls its way up my spine to the back of my neck."
    show mc scared version2
    "Someone is watching me. I can feel their eyes on me."
    #sound effect here maybe?
    show mc scared
    "Vines slowly wrap around my ankles as a wet and disgusting trail of saliva sneaks up between my shoulder blades."

    menu:
        "Turn around":
            $ points_end_3 += 1
            show mc:
                xalign -0.05
            "This can’t be real. I take a deep breath and turn around."
            stop music fadeout 1.0
            show mikh happy at center
            show mc neutral
            "Mikhail is there, his bed hair sticking out hilariously. I peek down at my ankles and of course, there’s nothing holding me in place."
            show mc sad
            "Gods, I must be tired."
            show mc neutral
            show mikh annoyed
            m "Good morning… *yawns* I just woke up and I’m already so tired…"

        "Brandish the knife":
            $ points_end_1 += 1
            $ points_end_2 += 1
            show mc:
                xalign -0.05
            show mikh scared at right
            "Adrenaline takes over, and I lunge for the knife that was near the sink. I jerk around to face the monster, only to find Mikhail standing there, caught off guard. His hands shoot up in surrender."
            "I lower the knife in disbelief at myself."
            show mc scared version2
            show mikh sad
            mc "M-Mikhail, I’m so sorry, I…"
            show mc sad head move
            show mikh sad mo
            m "Whoa! didn’t mean to scare you, I’m sorry…"
            show mc blushing mouth open
            show mikh sad
            mc "No it’s okay ! I… I mean… I’m the one who’s sorry, I didn’t want to…"
            show mc sad
            show mikh sad
            m "Hey, it’s fine… I did show up behind you without warning, didn’t I?"
            hide mc
            hide mikh
            "I put back the knife on the counter like it’s on fire. I’m in disbelief, and horrified. How could I point a knife at my friend?"

    show mc sad mouth open at left
    show mikh blushing at center
    mc "Haha… Yeah, rough night, huh? I must be still half-asleep myself… I’m sorry…"
    m "Hold on…"
    show mikh dark
    pause 0.2
    show mikh blushing
    pause 0.2
    show mikh dark
    pause 0.2
    show mikh blushing
    show mc scared
    "His hands reach towards me and I…" #MIKHAIL GLITCHING TO MONSTER FORM

    menu:
        "Slap his hand away ":
            $ points_end_1 += 1
            $ points_end_2 += 1
            play sound "audio/SFX/Slap_Realistic.mp3"
            show mc scared version2
            show mikh sad
            "Without a second thought, I slap his hand away. His surprised expression turns into a hurt one."
            show mc sad
            show mikh sad mo
            m "Sorry… Didn’t mean to startle you again… I just wanted to wipe the blood from your face."
            stop music
            show mc sad mouth open
            show mikh sad
            mc "Oh…! Gods, what am I doing… I’m so sorry Mikhail."
            show mc pensive worried
            show mikh happy
            m "Hey it’s okay, I should have just told you what I was doing."
            scene black with Dissolve(1.0)
            "I feel guilty, but also glad he didn’t get the chance to touch me. I don’t know how I would have reacted."

        "Let him":
            $ points_end_3 += 1
            stop music
            show mc blushing
            show mikh happy
            "I try to stay still, repeating over and over “it was only a nightmare [mc_name], it was ONLY a nightmare. You don’t need to be afraid.” in my head."
            "Mikhail’s hand brushes my cheek, tainting his fingers red."
            show mc happy
            show mikh happy
            "A sigh of relief escapes my lips, as I realize he only wanted to clean my face."
            m "Wait, I’ll get a clean towel."
            show mc sad head move
            scene black with Dissolve(1.0)
            "How could I think he was trying to hurt me? I need to stop thinking about that stupid dream. Thankfully the fresh towel calms me down, bringing me back to reality."

    scene interiorCottage_BG with Fade(0.5, 0.5, 0.5)
    show mc happy at left:
        xalign -0.02
    show mikh happy at right:
        xalign 1.05
    play music "audio/OST/Cozy.mp3"
    "I chop and cover the fresh meat with salt to preserve it and pack it."
    mc "I’ll go and put it away in the cellar."
    #(with a flair for the dramatic)
    m "My liege, let me do that for you."
    "I can’t help but laugh with him."
    play music "audio/OST/Cozy.mp3"
    "The unease from the previous night is fading away, and with it that awful dream I had. I hope to forget it soon."
    "We can’t appreciate the silence for too long as we hear a long annoyed sigh coming from the living room."
    hide mc
    hide mikh
    show nina pissed at center
    n "Gods above and below… Really?"
    "We go check what the problem is and it’s no other than Basilio, sitting on the floor and holding our picnic basket hostage against his chest."
    show bas pensive mo at right
    b "Come oooon pleeeeeaaaaaase!"
    n "Ugh, I can’t believe I have to say this:"
    n "Basilio, you cannot bring a whole ass gratin  with us. How would you eat it anyway???"
    with hpunch
    b "With my bare hands? like a REAL MAN?!"
    show nina embarrassed at left:
        xzoom  -1
    n "You’re no better than an animal, even dogs have more manners than you."
    b "How can you say no to this marvelous piece of art!"
    "The thick, glossy cream, the savory soft potatoes, and of the delicate crunch of the sauteed onions… And who could forget la pièce de résistance - The smoked and melted RRRRRRAAAAAAAAAAAAAACLETTE!!"
    show mikh happy:
        xalign 0.7
    show bas :
        xalign 1.2
    #(interrupting)
    m "-Actually, I already packed polenta e salame while the girls were outside. Does that sound good to everyone?"
    show nina :
        xalign 0.3
    show mc happy at left
    mc "Sounds good."
    n "Definitely agree."
    show bas sad
    "Basilio, disappointed, cuddles the basket for one last time. Like a mother abandoning her child, he puts it down on the table and sheds a single tear."
    b "See you later, my sweet…"

    jump CC1_6

