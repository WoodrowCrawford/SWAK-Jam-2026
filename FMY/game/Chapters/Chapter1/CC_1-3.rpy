label CC1_3:
    scene bed_CG with Dissolve (1.0)
    play sound "audio/SFX/NightAmb_1.mp3" fadein 1.0
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
    n "Alright. Let’s get some sleep, buttercup. Wouldn’t want to let the guys prepare the picnic tomorrow… You want your kitchen in one piece, yeah?"
    mc "You’re right, goodnight Nina."
    n "Goodnight sweetheart."
    play sound "audio/SFX/bedsheet1.mp3"
    scene black with Dissolve(1.0)
    pause 2

    jump CC1_4