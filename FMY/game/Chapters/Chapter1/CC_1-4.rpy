label CC1_4:

    "Something is dripping on my face. Cool water makes its way down my cheek and onto the ground."
    "My hands brush the cold moss carefully, it must have been raining in the forest."
    "Ah… Did I fall asleep while looking for mushrooms?"

    scene darkForest_BG with Dissolve(1.0)
    play music "audio/OST/Creepy.mp3" fadein 1.0
    "I look up to the clouds, frowning."
    "Above the grey clouds, a pink hue peeks out before hiding back within its rain blanket."
    "Or am I mistaken? The sky keeps changing color, going from pink to purple to even green…"
    "Either way, I can’t tell the time of the day."

    show mc scared at center
    with dissolve
    mc "I need to get home, something’s not right here…"

    play sound "audio/SFX/Steps_Forest1.mp3" fadein 0.5
    "I walk through the dormant woods, everything is so… Quiet."
    "I can almost hear my heartbeat under the noise of my quickening footsteps."
    "Where are the rabbits, the boars, the deers? Even the wolves…? Where’s everyone?"
    "Please… Anyone… Answer my silent plea. I’m frightened, cold and alone…"

    #have the mc look at the camera here
    voice "audio/VOICES/FAE/faegiggle.mp3"
    pause 1
    show mc scared version2
    with dissolve
    voice sustain
    pause 2.6
    "Suddenly, as if an angel had heard my prayers, a soft giggling reaches my ears."

    show mc terrified
    play sound "audio/SFX/Steps_Forest2.mp3"
    "I start running through the forest, tripping over roots and sliding around in the mud and moss. I need to catch up to that voice, because if I don’t, then I’ll-"
    mc "Stop! Please come back! Don’t leave me here alone!"

    play voice "audio/VOICES/FAE/faegiggle.mp3" volume 0.2
    voice sustain
    pause 4
    show mc scared
    with dissolve
    "Finally, I spot a figure in front of me. It looks human and… Familiar?"

    show mikh dark at right
    with dissolve
    "???" "[mc_name], finally… I was waiting for you."
    "I recognize this voice… Mikhail? He came for me?"

    show mc happy mouth open
    mc "Mikhail! Thank goodness you’re here. We need to get home, it’s not safe here-"

    hide mc
    show mikh dark:
        easein 0.7 right3
    show mc scared
    "I reach for him, but he grabs my wrists and traps me in an embrace. It’s too tight."

    # i feel like we can add some more effects here to make it more impactful
    scene monsterMIKH_CG with Dissolve (1.0) #size too big
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
        show monsterMIKH_CG with Dissolve (1.0)
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

    # take this part out for now
    #scene darkForest_BG with Dissolve (0.6)
    #show mc terrified at center
    #with dissolve
    "This can’t be Mikhail, this… creature may look like him, but it can’t be-"

    scene monsterMIKH_CG with Dissolve (1.0)
    "Roses are blooming from my friend’s eyes, tainted by blood. Vines intertwines around his limbs, contorting him like a puppet. Its bones are cracking as he writhes in pain."
    "What on Earth is this thing?!"
    "I can’t run away, my legs won’t move an inch. The thing cracks and stumbles towards me as I close my eyes and pray to whichever God can make my death as painless as it can be."

    scene black with Dissolve(1.0)
    stop music fadeout 1.0
    "Then I hear Nina’s voice calling me."

    jump CC1_5