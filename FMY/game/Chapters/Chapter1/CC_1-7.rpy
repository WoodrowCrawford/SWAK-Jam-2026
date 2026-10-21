label CC1_7:

    scene forest_BG with Dissolve (1.0)
    "She must be nearby, I can hear her soft crying."
    "As I walk through the woods I notice movement around me: wild rabbits, squirrels and even a few foxes gather to look at me. I stop in my tracks, baffled."
    play music "audio/OST/Creepy.mp3"
    "These animals are usually pretty shy… Why aren’t they running away? And why do they look so sad?"
    "Carefully, one of the squirrels scurries to my feet and drops something before fleeing with the rest of the animals."
    "I lean down to grab what he left: it’s a single green oak leaf. What’s stranger is that I recognize the intricate patterns drawn into the leaf veins."
    "Where on Earth have I seen this before?"
    stop music fadeout 1.0
    "Nina’s weeping gets louder as I realise I had started walking again at some point. I put away the leaf in my apron pocket as I approach, finding her sitting against a rock."
    show mc neutral at left
    show nina sad at right
    "Her knees are close to her chest and her head is hidden behind her crossed arms. She’s trembling softly."
    mc "Hey, Nina… I came to make sure you’re okay."
    n "I’m okay… Sorry for running away, it was childish of me."
    n "I… I was about to wish for all of us to be happy forever and he… It’s stupid, I know this is just a legend but all I ever wanted was to always be with you guys…"
    "She sobs and looks up at me."
    n "We missed you so much [mc_name]… {i}I’ve{/i} missed you. It’s so lonely in the city without you."
    "I kneel in front of her, lending her my handkerchief."
    "Hearing those words fill me with-"

    menu:
        "Compassion":
            $ points_end_1 += 1
            $ points_end_2 += 1
            $ points_end_3 += 1
            #show mc smile
            show mc happy at left
            "I can’t help but smile while Nina wipes away her tears, and I sit down to lean against her. Seeing someone this passionate about wanting to be around their loved ones is really moving."
            "I’m grateful to be one of the people she cares about."
        
        "Confusion":
            $ points_end_1 += 1
            $ points_end_2 += 1
            $ points_end_3 += 1
            $ points_secret_info += 1
            #show mc indifferent
            show mc neutral at left
            "I can’t help but be confused. Why would she get so emotional about something like this?"
            "An old legend can’t help us against fate - we don’t get to decide what it has in store for us.It’s silly to wish for something like that, but still, I’m happy that she would wish for us to stay together."

    mc "Nina, please know that I am and will always be there for you. Wish granted or not."
    n "Thank you [mc_name]… That means a lot…"
    "We stay silent for a moment, then Nina sighs."
    show nina embarrassed at right
    n "I made a huge deal out of nothing, didn’t I? Is Bas going to be mad at me now…?"
    show mc happy at left
    mc "Of course not! He was already planning to get on his knees and beg for forgiveness, you know."
    show nina happy at right
    "We laugh for a bit. I think carefully as to what to say to make her feel better."
    mc "I think both of them will be happy to hear your real wish, Nina."
    "Nina stays silent for a moment, then she gets up and slips her hand in mine. I squeeze her back and look at her to make sure she’s alright."
    mc "You’re ready to go back to the others?"
    n "I’m ready."
    "We begin our journey to get back to our friends, hand in hand."
    show mc pensive at left
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
    hide nina
    show mc pensive worried at center
    "My heart skips a beat. Nina is sweet and caring, but this… This is a bit too intimate a touch."
    with hpunch
    "My breathing is stiff, my ears are ringing… This is not the time to feel sick…"
    "Nina?" "Look at you, my poor sweetheart. You’re so pale… you can’t even walk on those shaky legs…"
    "I whip around, startled at the pretty lady holding my hand."
    scene Hicetia_CG with Dissolve (1.0)
    nl "Why not rest a little, my dear? Here, let’s sit down for a bit. There’s no need to rush…"
    pause 1.0
    show Hicetia_CG :
        ease 1.0 zoom 0.5
    "Our eyes meet, my heart stings as if pierced by a thousand needles. Something deep inside tells me we were meant to meet each other..."
    "I should have never set foot in this cursed forest."  #like in red or something spooky, shaking effect maybe?
    scene black with Dissolve (1.0)
    "{b}THANK YOU FOR PLAYING OUR DEMO!!! See you soon ! ~{/b}"

    return