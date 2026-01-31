define h = Character("Hicetia")
define b = Character("Basilio")
define mc = Character("[mc_name]")
define m = Character("Mikhail")
define n = Character("Nina")
define nl = Character("Noble Lady")


label start:

    scene black

    label name_select:
        $ mc_name = renpy.input("What's your name?", length=8).lower().title()
        $ mc_name = ' '.join(mc_name.split())
        if mc_name =="":
            $ mc_name = "Primrose"


    if mc_name == "":
        jump name_select

    pause 0.5
    #INTRO : 

    nvl_narrator "{i}Deep down in the forest,{w=1.5}{nw}{/i}" with Dissolve(1.0)
    nvl_narrator "{i}Where the last green leaf rests,{w=1.5}{nw}{/i}" with Dissolve(1.0)
    nvl_narrator "{i}Your cries will be heard…{/i}" with dissolve

    scene interior_cottage with Fade(1.0,0.0,1.0)

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
        xalign 0.5
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
    b "He looked as if he was about to take a shit…!"

    show bas happy
    #(quietly)
    m "…It was worth it."

    menu :

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

            "I can’t help but laugh while Basilio teases Mikhail by pinching his reddish cheeks."

            mc "Thank you Mikhail,truly, it’s a very sweet gift."

            m "Don’t mention it, after all… You’re the one who convinced me to become a tailor…"

            "Basilio suddenly falls to the ground. I gasp as he tries to reach for the table."


    show bas shocked ver2

    b "Ugh… I… I’m about to diee… If only I could have tasted a walnut pie for the last time… Even just half of it…!"

    show nina pissed mouth open:
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

    #(whispering)
    show mikh pensive mo:
        xalign 1.05

    show mc:
        linear 1.0 xalign 0.3


    m "We should leave them alone for a bit, I can help you set the table if you’d like?"

    hide mc
    hide mikh


    "I nod, following him into the kitchen. We are quietly unpacking the dishes they brought and putting the finishing touches to the walnut pie when I notice Mikhail sneak a look at me."


    show mikh sad mo
    show mc neutral:
        xalign 0.1

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

            #(laughing)
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

            #(laughing)
      
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
    scene interior_cottage with Dissolve (1.0)



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
    "Nina sighs and shakes her head, trying to pout in order to hide her smile."


    n "[mc_name], let’s get out of here before they infect us with their stupidity."

    hide mc
    hide nina
    hide mikh
    hide bas
    "We both head to my room and get ourselves ready to go to bed."
    stop music fadeout 1.0
    scene cg_bed with Dissolve (1.0)
    play sound "audio/SFX/countryside_night.mp3" fadein 1.0
    n "How’s it going between you two?"

    mc "Huh? What do you mean?"

    n "Oh come on, Basilio is being as discreet as a herd of giants running through the forest. We all know that Mikhail likes you, he’s getting more and more obvious."


    n "So… How do you feel about him?"

    menu:
        "I don’t know":
            $ points_end_3 += 1

            "I fidget with my hands."

            mc "I’m not sure, I mean… I don’t know what to say…"

            n "It’s alright, it’s just between us. If he asks you out, or rather - when he asks you out, he’ll have to accept whatever answer you decide to give him."
            "I never gave it much thought, to be honest. I don’t know much about love."

            "I’ve read all about it in my books of course, I see how my parents are together, but… Feeling my heart beat faster when my crush looks my way? The need to be close to them and to make them happy? I’ve never felt anything like that."

            "My parents have always been so protective of me, anytime I would meet someone they’d panic and keep them at arm’s length. It took them ages to even accept my friends being alone with me."

            "Perhaps they’re scared someone might hurt me, or abandon me when I’m sick."

            "In any case, Nina is right."

            "Whatever happens, only I can decide my feelings."


        "I like him":
            $ points_end_2 += 1
            "I smile sweetly as I look at the trees outside my bedroom window."

            mc "I… I like having him around."


            n "I won’t tell a soul. I promise."
            "Unless you want me to of course, but I think you should deal with it yourself because only you can know when it’s the time to let him know how you feel."

            mc "Thank you Nina, I can always count on you."

        "I see him as a friend":
            $ points_end_1 += 1

            "I stop breathing, frozen as a statue."

            "Mikhail and I? A couple?"

            "I’ve known him since forever. I always thought of him as a brother."
            "Even if I wanted to try and return those feelings, I couldn’t picture ourselves as a couple."

            "I don’t know much about love, but maybe I’d prefer…"

            "Anyway, I stutter and try to answer the question."


    mc "I-I…"

    n "It’s alright, you know. You don’t have to tell me anything and this talk stays between us. You don’t have to justify your feelings."

    mc "Thank you…"

    n "I know you, [mc_name]. I’m a hundred percent sure no matter your answer, you’ll be kind to him. Wanna talk about something else?"

    mc "Please, let’s do that…"

    "We then chat about the city and her new job. Soon it’s time to call it a day."


    "Nina stretches, extending her arms as if she’s trying to reach for the moon."

    #(yawning)
    n "Alright. Let’s get some sleep, buttercup. Wouldn’t want to let the guys prepare the picnic tomorrow… You want your kitchen in one piece, yeah?"

    mc "You’re right, goodnight Nina."

    n "Goodnight sweetheart."

    stop sound fadeout 1.0

    scene black with Dissolve(1.0)

    "Something is dripping on my face. Cool water makes its way down my cheek and onto the ground."

    "My hands brush the cold moss carefully, it must have been raining in the forest."

    "Ah… Did I fall asleep while looking for mushrooms?"

    scene dark_forest with Dissolve(1.0)

    "I look up to the clouds, frowning."

    "Above the grey clouds, a pink hue peeks out before hiding back within its rain blanket."

    "Or am I mistaken? The sky keeps changing color, going from pink to purple to even green…"

    "Either way, I can’t tell the time of the day."

    mc "I need to get home, something’s not right here…"
    play music "audio/OST/Creepy.mp3" fadein 1.0
    play sound "audio/SFX/walk_forest.mp3" fadein 0.5
    "I walk through the dormant woods, everything is so… Quiet."

    "I can almost hear my heartbeat under the noise of my quickening footsteps."

    "Where are the rabbits, the boars, the deers? Even the wolves…? Where’s everyone?"

    "Please… Anyone… Answer my silent plea. I’m frightened, cold and alone…"

    "Suddenly, as if an angel had heard me, a beautiful humming reaches my ears."

    "I start running through the forest, tripping over roots and sliding around in the mud and moss. I need to catch up to that voice, because if I don’t, then I’ll-"

    mc "Stop! Please come back! Don’t leave me here alone!"

    "Finally, I spot a figure in front of me. It looks human and… Familiar?"

    show mikh dark at center
    "???" "[mc_name], finally… I was waiting for you."

    hide mikh
    "I recognize this voice… Mikhail? He came for me?"

    show mc happy mouth open at left:
        xalign -0.02

    show mikh dark at center
    mc "Mikhail! Thank goodness you’re here. We need to get home, it’s not safe here-"

    "I reach for him, but he grabs my wrists and traps me in an embrace. It’s too tight."
    scene cg_nightmare_1 with Dissolve (1.0) #size too big

    m "Finally… No one will bother us now."

    "His voice, usually warm, makes my skin crawl. He nuzzles his face against my neck, breathing heavily like some kind of wild beast."

    m "I’ve been patient for so long, [mc_name]. I deserve a reward for playing nice this whole time, don’t I?"


    "I try to push him away, but his wandering hands make me freeze in fear."

    m "Let’s have some fun, [mc_name]…"


    # fade to black
    scene black with Dissolve (1.0)
    "He’s too strong. I can’t move. My throat closes up as he kisses my neck."

    mc "Mikhail! S- stop!" with vpunch


    #IF MC WAS FLIRTY WITH MIKHAEL:
    if flirted_with_mikhail:
        scene cg_nightmare_1 with Dissolve (1.0)
        m "Mikhail scoffs in my ear, mocking my distress as if I was little Red Riding Hood caught in the big bad wolf’s trap."

        m "Come on, don’t be shy now! You should have known before stringing me along. You know what they say, boys will be boys…"
        


    #IF MC WAS FRIENDLY TO MIKHAEL:
    else:
        show cg_nightmare_1 with Dissolve (1.0)
        "Mikhail squeezes me so tight in his arms, I can almost hear my bones cracking under the pressure."

        m "Darling… You’re acting so pure and shy but I know you."
        m "I know that in reality, deep down in your heart, you’re longing for something far more sinister than this."



    m "Now relax and don’t move…"

    scene black with Dissolve (1.0)

    "He tries to take off my clothes, and I wait for the right moment to push him off me."
    "I fall to the ground as he stumbles back."

    scene dark_forest with Dissolve (1.0)
    show mc scared version2 at center

    "This can’t be Mikhail, this… creature may look like him, but it can’t be-"
    scene monsterMIKH_CG with Dissolve (1.0) #zoom out pls

    "Roses are blooming from my friend’s eyes, tainted by blood. Vines intertwines around his limbs, contorting him like a puppet. Its bones are cracking as he writhes in pain."

    "What on Earth is this thing?!"

    "I can’t run away, my legs won’t move an inch. The thing cracks and stumbles towards me as I close my eyes and pray to whichever God can make my death as painless as it can be."


    scene black with Dissolve(1.0)
    stop music fadeout 1.0
    "Then I hear Nina’s voice calling me."


    scene interior_cottage with Dissolve (1.0)
    play music "audio/OST/Main.mp3" fadein 1.0

    show nina confused at center
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
    scene exterior_cottage with Dissolve(1.0)
    "Nina and I both take a basket and go outside, where chickens are hunting for worms. Their feathers, covered in morning dew’s pearls, make their warm colors brighter."

    show mc happy:
        xalign -0.01
    
    show nina happy:
        xalign 1.05

    "I crouch to pet some of them, gently brushing off their heads and petting little chicks in my hands while Nina is fetching fresh eggs from their nests in the coop."

    "I look around and choose one of the chickens that has not been laying as much as she used to, and I wrap my hand around her neck and take her back to the kitchen."

    mc "You can put the eggs over there, thank you Nina."

    "I lay the chicken on the table, and hold it down with one hand as she squirms under the pressure. I grab the cleaver and swiftly put an end to it."


    show nina terrified
    # play knife sound here

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
    pause 1.0
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
            show mikh scared at center
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


    show mc sad mouth open:
        xalign -0.05

    show mikh blushing at center
    mc "Haha… Yeah, rough night, huh? I must be still half-asleep myself… I’m sorry…"

    m "Hold on…"

    show mikh dark
    pause 0.3
    show mikh blushing
    pause 0.3
    show mikh dark
    pause 0.3
    show mikh blushing

    show mc scared

    "His hands reach towards me and I…" #MIKHAIL GLITCHING TO MONSTER FORM



    menu:

        "Slap his hand away ":
            $ points_end_1 += 1
            $ points_end_2 += 1

            "Without a second thought, I slap his hand away. His surprised expression turns into a hurt one."

            m "Sorry… Didn’t mean to startle you again… I just wanted to wipe the blood from your face."

            mc "Oh…! Gods, what am I doing… I’m so sorry Mikhail."

            m "Hey it’s okay, I should have just told you what I was doing."
            "I feel guilty, but also glad he didn’t get the chance to touch me. I don’t know how I would have reacted."

        "Let him":
            $ points_end_3 += 1

            "I try to stay still, repeating over and over “it was only a nightmare [mc_name], it was ONLY a nightmare. You don’t need to be afraid.” in my head."

            "Mikhail’s hand brushes my cheek, tainting his fingers red."
            "A sigh of relief escapes my lips, as I realize he only wanted to clean my face."

            m "Wait, I’ll get a clean towel."

            "How could I think he was trying to hurt me? I need to stop thinking about that stupid dream. Thankfully the fresh towel calms me down, bringing me back to reality."



    "I chop and cover the fresh meat with salt to preserve it and pack it."

    mc "I’ll go and put it away in the cellar."

    #(with a flair for the dramatic)
    m "My liege, let me do that for you."

    "I can’t help but laugh with him."

    "The unease from the previous night is fading away, and with it that awful dream I had. I hope to forget it soon."

    "We can’t appreciate the silence for too long as we hear a long annoyed sigh coming from the living room."

    n "Gods above and below… Really?"

    "We go check what the problem is and it’s no other than Basilio, sitting on the floor and holding our picnic basket hostage against his chest."

    b "Come oooon pleeeeeaaaaaase!"

    n "Ugh, I can’t believe I have to say this:"

    n "Basilio, you cannot bring a whole ass gratin  with us. How would you eat it anyway???"

    b "With my bare hands? like a REAL MAN?!"

    n "You’re no better than an animal, even dogs have more manners than you."

    b "How can you say no to this marvelous piece of art!"

    "The thick, glossy cream, the savory soft potatoes, and of the delicate crunch of the sauteed onions… And who could forget la pièce de résistance - The smoked and melted (SINGING LOUDLY)RRRRRRAAAAAAAAAAAAAACLETTE!!"

    #(interrupting)
    m "-Actually, I already packed polenta e salame while the girls were outside. Does that sound good to everyone?"


    mc "Sounds good."

    n "Definitely agree."

    "Basilio, disappointed, cuddles the basket for the last time. Like a mother abandoning her child, he puts it down on the table and sheds a single tear."

    b "See you later, my sweet…"

    scene forest with Dissolve (1.0)

    "I can’t help but smile as we hike among all these trees. Every leaf, root and burrow hides a secret."

    "I’ve heard so many legends about the mountains, our elders tell all kinds of stories after a bit of wine."

    "I would sneak out with my friends to go listen to them."

    "My parents didn’t quite like that, they’re not into that superstitious stuff. They were worried those stories would scare me, but they never did."

    "Those fairytales are a precious childhood memory I keep close to my heart."

    "Basilio is walking next to me, a soft smile on his face."

    b "Feeling nostalgic, uh? It reminds me about the time we pretended to be myth hunters."

    mc "I remember we walked  all day and found nothing but berries."

    b "Yeah, it was so fun… And tasty!"

    n "We’re kind of doing it again right now."

    b "I would have the strength to protect us all if only you had let me bring the gratin, Nina…!"

    n "Not this again…"

    "Mikhail turns to Bas."

    m "Don’t worry… I’ll protect you, my love."

    #(tearing up)
    b "Oooh my hero!"

    "Bas rushes to his prince charming’s side and holds his hand. The boys start walking in front of Nina and I, jumping around as they do."

    mc "Any ideas as to what you’re going to wish for?"

    n "Yeah, I’ve even brought offerings to maximize our chances to have them granted! What about you?"

    mc "I’m still thinking about it…"

    "That’s what I’d like to say, but my mind is only filled with uneasiness."

    "I’m not sure why, but I feel like I’m being watched. There’s not a single animal around, and I can’t even hear the birds sing nearby. Could there be a predator watching us?"

    "No, even if there was, I don’t think it would look at me this way."

    "This thing is looking at me from head to toes with… Hunger."

    "A deep, insatiable desire I can’t put my finger on."

    "If this predator decided to attack, I’d let it feed on me. There would be nothing I could do against it anyways."

    "Wait, why am I having these weird thoughts?"

    b "Careful Nina, we don’t want to step on these weird mushrooms. Here, take my hand."

    "No it’s alright, I’m just nervous."

    "I look up. A huge stone pine tree, surrounded by mushrooms, is sitting in front of us. Its needles, frail but dancing along the winds fearlessly, create an immense shadow that shields us from the sun."

    m "Wow… Every time I see it I can’t help but marvel at how majestic nature is."

    b "Nina, come on! You’re not gonna start working in the middle of the forest, are you?"

    n "This is not for work, it’s for my wish! Let me do my thing."

    "Nina rummages around inside the basket and pulls out a plain doll painted purple and green."

    n "Mikhail’s clothes: check. Basilio’s tiny bracelet : Check. [mc_name]’s flowers : Check."

    n "Alright, perfect! My wishing doll will be beautiful."

    "Tenderly, as a mother would, she dresses the wooden girl with a small piece of clothing made with care by Mikhail."

    "She crowns it with the tiny paper flowers I made for her last summer and finally straps them to its head with Basilio’s trinket."

    mc "That’s adorable."

    n "Thank you, I hope the fairy will like it."

    b "No way, you’re still praying to that chick?"

    n "You shouldn’t call her that. I’m dead serious."

    "The forest fairy is the queen of these mountains. Every year, around the end of September, the townspeople celebrate her awakening which is said to grant wishes."

    "This story has lived through the ages, not without its variants. Some walk in the forest, some dance around the campfire while others pray to the moon at night from the comfort of their homes."

    "Fairytale or not, it brings comfort and hope to people for the next year to come."

    "I circle around the tree, looking at all the offerings decaying from the elusive passage of time."

    "There’s more than just ribbons and carved wooden figures, in these gifts I see unspoken desires."

    "I hear commotion coming from the other side of the tree."

    n "Hear my plea, dear forest guardian…"

    b "FAIRY, DARLING, I WISH TO HAVE MORE MUSCLES! And maybe a fuller beard…"

    n "As… As I humbly kneel on your holy ground…"

    b "COME HERE MIMI! LET’S WISH FOR A  LENGTHY CHAMPAGNE RAIN ON OUR WEDDING DAY!"

    n "Bas…"

    b "PERHAPS YOU COULD ASK FOR A HAPPILY EVER AFTER WITH-"

    n "BASILIO, I WISH YOU COULD SHUT UP FOR ONCE!"

    "The boys are stunned, even the wind stops and holds its breath."

    "Nina is clenching her fists and tears are prickling her eyes."

    n "You couldn’t help but make fun of me, couldn’t you, Bas?"

    "I reach out to place a reassuring hand on her shoulder, but she swats my hand away."

    n "I need to be alone."

    "Nina walks away, weeping. Her doll rests against one of the roots covered in moss of the wishing tree, silently watching us."

    m "Bas…"

    b "Urgh… I’m so stupid."

    "Bas sits down in the grass, a hand on his face."

    b "She was planning this for months, and I went and ruined it with my stupid jokes."

    m "It’s okay, one look at you and she’ll know you’re sorry for acting like a dummy."

    b "Ha, I sure hope that’s the case…"

    "Bas smiles bitterly, then stands up."

    b "No, I need to apologize right now."

    mc "She needs some space, Bas. I’ll go check on her, you can apologize when we come back."

    "Basilio is clearly hesitant: he wants to tag along and find her."

    "A quick look on Mikhail’s hand patting his shoulder makes him back off."

    b "Thank you, [mc_name]… I really appreciate it."

    "I promise I will make things right."

    mc "No problem, Bas. We’ll be back before you know it."

    "I let Mikhail comfort Basilio while I go looking for Nina."

    "She must be nearby, I can hear her soft crying."

    "As I walk through the woods I notice movement around me: wild rabbits, squirrels and even a few foxes gather to look at me. I stop in my tracks, baffled."

    "These animals are usually pretty shy… Why aren’t they running away? And why do they look so sad?"

    "Carefully, one of the squirrels scurries to my feet and drops something before fleeing with the rest of the animals."

    "I lean down to grab what he left: it’s a single green oak leaf. What’s stranger is that I recognize the intricate patterns drawn into the leaf veins."

    "Where on Earth have I seen this before?"

    "Nina’s weeping gets louder as I realise I had started walking again at some point. I put away the leaf in my apron pocket as I approach, finding her sitting against a rock. Her knees are close to her chest and her head is hidden behind her crossed arms. She’s trembling softly."

    mc "Hey, Nina… I came to make sure you’re okay."

    n "I’m okay… Sorry for running away, it was childish of me."

    n "I… I was about to wish for all of us to be happy forever and he… It’s stupid, I know this is just a legend but all I ever wanted was to always be with you guys…"

    "She sobs and looks up at me."

    n "We missed you so much [mc_name]… I’ve missed you. It’s so lonely in the city without you."

    "I kneel in front of her, lending her my handkerchief."

    "Hearing those words fill me with-"

    menu:

        "Compassion":
            $ points_end_1 += 1
            $ points_end_2 += 1
            $ points_end_3 += 1


            "I can’t help but smile while Nina wipes away her tears, and I sit down to lean against her. Seeing someone this passionate about wanting to be around their loved ones is really moving."
            "I’m grateful to be one of the people she cares about."

            #show mc smile

        "Confusion":
            $ points_end_1 += 1
            $ points_end_2 += 1
            $ points_end_3 += 1
            $ points_secret_info += 1

            "I can’t help but be confused. Why would she get so emotional about something like this? An old legend can’t help us against fate - we don’t get to decide what it has in store for us. It’s silly to wish for something like that, but still, I’m happy that she would wish for us to stay together."

            #show mc indifferent

    mc "Nina, please know that I am and will always be there for you. Wish granted or not."

    n "Thank you [mc_name]… That means a lot…"

    "We stay silent for a moment, then Nina sighs."

    "I made a huge deal out of nothing, didn’t I? Is Bas going to be mad at me now…?"

    mc "Of course not! He was already planning to get on his knees and beg for forgiveness, you know."

    "We laugh for a bit. I think carefully as to what to say to make her feel better."

    mc "I think both of them will be happy to hear your real wish, Nina."

    "Nina stays silent for a moment, then she gets up and slips her hand in mine. I squeeze her back and look at her to make sure she’s alright."

    mc "You’re ready to go back to the others?"

    n "I’m ready."

    "We begin our journey to get back to our friends, hand in hand."

    "We make our way through the woods, and eventually, it feels like it has been ages since we started walking."

    "Basilio will start searching for us if it takes too much time for us to get back."

    "I’m also conscious of the time, the night might come quicker than we think, if we don’t hurry."

    "I don’t remember being this far from the wishing tree, though?"

    "Are we lost? How could we possibly get lost?"

    "A shiver runs down my spine, and I feel sick to my stomach. Why now? This is no time to feel dizzy. I keep walking as fast as I can to make sure we get back to the boys safe and sound."

    "If only I was stronger, I could take better care of Nina. I’m tired of being the one who is taken care of."

    "She is counting on me, so I must keep walking."

    "Feeling my uneasiness, her thumb trails down my hand in a soft and warm caress. She is tugging me back, silently asking  to walk a little slower."

    "Her fingers intertwine with mine, squeezing my hand softly against hers. Despite her delicate demeanor, her grip is strong enough to know she won’t easily let go."

    "My heart skips a beat. Nina is sweet and caring, but this… This is a bit too intimate a touch."

    "My breathing is stiff, my ears are ringing… This is not the time to feel sick…"

    "Nina?" "Look at you, my poor sweetheart. You’re so pale… you can’t even walk on those shaky legs…"

    "I whip around, startled at the pretty lady holding my hand."
    scene Hicetia_CG with Dissolve (1.0)
    nl "Why not rest a little, my dear? Here, let’s sit down for a bit. There’s no need to rush…"

    "Our eyes meet, my heart stings as if pierced by a thousand needles. Something deep inside tells me we were meant to meet each other..."
    "I should have never set foot in this cursed forest."  #like in red or something spooky, shaking effect maybe?

    "THANK YOU FOR PLAYING OUR DEMO!!! See you soon ! ~"


    return
