#setup
init python:
    config.automatic_images = [ ' ', '_', '-', '/' ]
    config.screen_width = 1280
    config.screen_height = 720

# characters
define n = Character("Narrator", color = "#bababa")
define e = Character("Dark Angel", color = "#3d4b1d")
define s1 = Character("Scavenger 1", color = "#7e0200", image = "kaliruun")
define s2 = Character("Scavenger 2", color = "#14498c", image = "torrsylos")
define ka = Character("Kaliruun", color = "#7e0200", image = "kaliruun")
define to = Character("Torr", color = "#14498c", image = "torrsylos")
define dr = Character("Doctor", color = "#99ccff", image = "doctor")
define p1 = Character("Peacetech 1", color = "#8AFBFF", image = "peacetech1")
define p2 = Character("Peacetech 2", color = "#8AFBFF", image = "peacetech2")
define o = Character("O Dajer", color = "#eb9346", image = "odajerhospital")

default glass = 0
default cobalt = 0
default yttrium = 0
default wood = 0

default relation = ""


label start:
    scene bg westhalfmap
    python:
        tetraList = ["Glass", "Cobalt", "Yttrium", "Wood"]
        statList = ["Civility", "Fame", "Logic", "Agility", "Force"]
        kaStats = [5, 65, 25, 45, 20]
        toStats = [40, 70, 10, 30, 10]

    #testing section
    #ka "I have [tetras[0]] [tetraList[0]] + [tetras[1]] [tetraList[1]] + [tetras[2]] [tetraList[2]] + [tetras[3]] [tetraList[3]]"
    show screen gameUI

    #actual start
    n "Welcome to Torobos, wayward traveller..."
    n "Torobos is one of the many moons orbiting Helnisk, and certainly the most lawless."
    n "The entire moon is covered in desert and ocean, dotted with aspiring caravans,"
    n "Sailing over the dunes and oceans to trade their goods."
    n "Everyone is just trying to make their fame and fortune amidst the chaos of the churning sand."
    n "Some are lucky enough to be born in Havens, incredible cities filled with the best technology of the age."
    n "Others are left to suffer in the crime ridden Outposts."
    n "But no matter if you're a caravaner, Haven dweller, or Outpost scoundrel..."

    scene bg sunrise
    n "You can witness the magic of a Torobos sunrise every morning."
    n "For some, the sunrise is the harbinger of an end, rather than a beginning."
    n "An end to an entire night of semi-legal desert racing."
    scene bg sunrisefar
    n "These are called the Suda-Jay races, as they take place between the two Havens."
    scene bg sunrisefar1
    n "Powerful Haven Technocrats place their fortunes on racing bets"
    scene bg sunrisefar2
    n "Always so sure their sponsored racer will be the one to win first place."
    scene bg sunrisefar3
    n "They pay for a driver to race wildly across the desert in a highly modified, supercharged car, and for an adrenaline junkie to sit in the shotgun, with a shotgun"
    scene bg sunrise
    n "The rules are simple:"
    scene bg crash1
    n "There are no rules."
    scene bg crash2
    n "Drive."
    n "Survive."
    n "Kill."
    scene bg crash3
    n "Anything to win."
    scene bg crash4
    n "Even the best drivers fail to cross the finish line."
    scene bg crash5
    n "Fame had followed this car since its debut two years ago."
    scene bg crash6
    n "Driven by a wild woman under the name Arrow"
    scene bg crash7
    n "And shotgunned by her equally reckless lover, Dark Angel"
    scene bg crash8
    n "Names were never used by those who died so quickly."
    scene bg crash9
    n "How could anyone have survived the wreckage of the EMP?"
    scene bg crash10
    n "Almost invisible to the far eye, a small figure crawls out from beneath the overturned vehicle."
    scene bg crash11
    n "Dark Angel."
    scene bg crash12
    n "She did her job."
    n "Survive."

    show erindercrash at left

    e "I swear on Helnisks' rings..."
    e "some desert demon has it out for me."
    e "..."
    e "You're probably dead, Arrow, but even if you're not..."
    e "a driver who crashes isn't worth anything at all."
    e "We had a good run."
    e "See you in another life."

    hide erindercrash

    n "With those parting words, Dark Angel left her love and left her life."
    n "It wouldn't be long until the scavangers came around to pick at the remains and kill anyone left."
    n "She had never been the sentimental type. Always valuing her life over all else."
    n "It was the only reason she was still standing."
    n "She managed to limp off into the distance, a list of regrets already forming in her mind."
    n "Hours passed under the tyranny of the burning suns, under a sky full of other moons."
    n "The race had long since finished, leaving a trail of wreckage."
    n "Valuable wreckage."
    n "For some, such wreckage was as close as they would ever get to taste the bounties stored inside Havens."

    show kaliruun at left
    s1 "The crash should be around here."
    hide kaliruun
    show kaliruunsmile at left
    s1 "There it is!"
    show torrsylos at right
    s2 "I'm not blind, Kaliruun."
    ka "Oh you caught up."
    ka "Aren't you supposed to be a Stormrunner, Torr?"
    to "Just because I don't have as much experience running away from things doesn't mean I'm slow."
    ka "There's nothing wrong with running away from a couple of bartenders armed with hydro-cannons!"
    hide kaliruunsmile
    show kaliruun at left
    ka "Except I really would've liked to have kept that fake ID..."
    hide torrsylos
    show torrsylossmile at right
    show kaliruun at left
    ka "Not like you haven't-"
    ka "You know what?"
    ka "Nevermind."
    ka "We have a job to do."
    ka "It actually seems like the car is pretty intact. We can get some tetras from those parts."
    ka "Check the control panel, will you?"
    show torrsylos at right
    to "On it"
    to "..."
    to "Looks like the driver's still alive."
    show kaliruunsmile at left
    ka "Really? Interesting."
    to "She's gonna need Haven medics though."
    ka "Well, if we come with the one and only Arrow who's been so unfortunately injured..."
    show torrsylossmile at right
    to "... they'd have to let us in."
    ka "Exactly."

    menu:
        "Take the injured Arrow to the hospital":
            jump hospital
    label hospital:
        scene bg hospitalredo
        show doctor
        dr "Welcome to Galla, one of Suda's finest hospitals!"
        dr "I assure you we will do our absolute best to heal your loved one, as quickly as possible."
        show kaliruun at left
        show torrsylos at right
        dr "And you are...?"
        menu:
            "Her cousins.":
                jump cousins
            "Her siblings.":
                jump siblings
            "Her parents":
                jump parents
            "Her step-siblings on the third side from her second mother's first husband's Ganan mistress":
                jump complicated
    label cousins:
        $ relation = "cousin"
        hide doctor
        show kaliruunsmile at left
        ka "We're her cousins."
        show doctor at right
        hide torrsylos
        dr "I see."
        dr "Well, she's severely injured, but her patrons will cover the cost of her stay."
        ka "So..."
        ka "As her dearest cousins..."
        ka "We can stay to watch over her recovery?"
        dr "Your temporary visa will last for as long as she is in the hospital."
        ka "Thank you so much, Doctor."
        ka "Please let us know when she wakes up."
        dr "Yes, yes of course."
        ka "Then I guess we're going to get a going while you do the cure-y-thing."
        dr "Cure-y-thing?"
        show kaliruun
        hide kaliruunsmile
        hide kaliruun
        show doctor at right
        show torrsylos at left
        to "Yes. She has an enormous amount of previous experience in these matters."
        menu:
            "Pretend to be a doctor.":
                jump pretend
            "...sarcasm.":
                jump sarcasm
    label pretend:
        $ kaStats[0]+=1
        hide torrsylos
        show kaliruunsmile at left
        ka "Of course!"
        ka "I studied with none but the very best at Uskana University."
        dr "That's my alma mater!"
        dr "When did you graduate?"
        menu:
            "Yesterday":
                jump yesterday
            "A couple of turns ago":
                jump turns
            "Don't you remember me?":
                jump memory
        label yesterday:
            ka "Yesterday."
            hide kaliruunsmile
            show kaliruun at left
            ka "The celebration was cut short by the awful crash of cousin..."
            ka "Cousin."
            dr "I thought graduation was on the bright side of Helnisk's orbit."
            ka "Times change so quickly, don't they."
            ka "I remember when I was just a child..."
            ka "Helnisk's rings were full and the deserts were better swept..."
            dr "Ah, sorry, I would love to hear what I'm sure is a wonderful story, but..."
            dr "I have..."
            dr "I have patients- no!"
            dr "No, I have a meeting."
            dr "With other doctors."
            dr "Talking about doctor things."
            dr "You know, as a doctor."
            hide kaliruun
            show torrsylos at left
            to "..."
            to "Enjoy your doctor things then."
            to "We'd hate to make you late."
            dr "I- I will."
            hide doctor
            n "The doctor leaves, intent on avoiding long boring conversations."
            show kaliruun at right
            ka "He left before we could have any fun."
            jump part2
        label turns:
            ka "Well, it was a couple of turns ago."
            ka "You know how things go."
            dr "Of course, you must have a busy life as a graduate of such a university."
            hide kaliruunsmile
            show torrsylos at left
            to "Yes she's been quite busy with her..."
            to "Ventures."
            dr "Well I would love to reminnisce, I have another patient waiting for me in the next room."
            hide doctor
            n "At that, the doctor leaves, intent on avoiding boring conversations."
            jump part2
        label memory:
            $ kaStats[0] += 2
            hide kaliruunsmile
            show kaliruun at left
            ka "Don't you remember me?"
            ka "We were dissection partners for a whole year!"
            dr "We- we-"
            dr "We what?"
            ka "Come on..."
            ka "You must remember those late night study sessions."
            hide doctor
            show torrsylos at right
            to "Oh he's the one who...?"
            hide torrsylos
            show doctor at right
            dr "I- I don't understand."
            ka "As I remember, those study sessions got a bit..."
            hide kaliruun
            show torrsylossmile at left
            to "Involved."
            dr "Excuse me?"
            dr "I- I really don't think we have met before."
            hide torrsylossmile
            show kaliruun at left
            ka "I'm truly offended!"
            dr "Oh... I-I... of course!"
            dr "You... you were in my... seminar!"
            hide kaliruun
            show kaliruunsmile at left
            ka "Yes, THE seminar!"
            dr "Yes! How ever could I have forgotten..."
            dr "Please accept my sincerest apologies"
            menu:
                "I understand completely, those were very hectic times.":
                    jump understand
                "I... I thought we were more than that...":
                    jump more
            label understand:
                ka "*wink wink* I remember you were quite busy."
                ka "So have you changed at all? *raises eyebrows*"
                dr "..."
                dr "I don't know what you mean."
                ka "Ayyy you're just having too much fun aren't you?"
                dr "I've- I've really tried to change."
                dr "You know who I am though."
                dr "Please don't tell my wife."
                ka "I... I..."
                ka "Of course! Of course I do."
                hide doctor
                show torrsylos at right
                to "And of course your wife doesn't know."
                to "We wouldn't want her to know either."
                to "How much money would it take to keep it that way though?"
                menu:
                    "Extort the Doctor.":
                        jump extort
                    "Reprimand Torr":
                        jump reprimand
                label extort:
                    hide kaliruun
                    show kaliruunsmile at left
                    ka "After all, your reputation at this hospital is quite something!"
                    ka "Impressive how far you've gone since our school days."
                    to "Wouldn't want it to all go to dust would you."
                    ka "No you really wouldn't."
                    hide torrsylos
                    show doctor at right
                    dr "Please, please no."
                    dr "I swear, anything you want."
                    to "One wood."
                    hide kaliruunsmile
                    show torrsylos at left
                    dr "Per mistress???"
                    hide doctor
                    show kaliruun at right
                    ka "..."
                    to "..."
                    menu:
                        "Yes. Per mistress.":
                            jump per
                        "No. Just one is fine!":
                            jump just
                    label per:
                        ka "Yes. Per mistress."
                        hide torrsylos
                        show doctor at left
                        dr "Oh hellfires."
                        dr "I... I can't just..."
                        ka "Oh yes you can, my dear Doctor."
                        dr "Oh my..."
                        dr "Alright. I'll wire you the funds."
                        $  wood += 3
                        dr "As long as you promise I will never hear from you again."
                        ka "Lovely!"
                        ka "But we will need to check in on our cousin of course."
                        n "The Doctor grumbles and leaves, having lost much more in that room than he had ever dreamed."
                        jump part2
                    label just:
                        ka "No. Just one is fine!"
                        hide torrsylos
                        show doctor at left
                        dr "Oh thank the dunes."
                        hide doctor
                        show torrsylos at left
                        to "..."
                        ka "..."
                        hide torrsylos
                        show doctor at left
                        dr "I'll wire it to you."
                        $ wood += 1
                        dr "Just never mention it again."
                        n "The Doctor leaves hurriedly, glad to have paid a relatively small sum to push that particular problem to a later date."
                label reprimand:
                    hide kaliruunsmile
                    show kaliruun at left
                    ka "Torr! How dare you?"
                    ka "We don't do that to old friends."
                    ka "*leans over* My cousin can be a bit... tempermental."
                    ka "You know, all those years in the open desert can do things to one's mind."
                    to "Hey!"
                    hide torrsylos
                    show doctor at right
                    dr "What a duster notion of-"
                    dr "I can't even-"
                    dr "You poor thing, Doctor..."
                    ka "Doctor Kaliruun."
                    ka "And yes it's quite a struggle."
                    ka "You know how cousins are."
                    dr "Oh all too well."
                    dr "In fact, unfortunately, mine are in town for a reunion."
                    n "The doctor sighs deeply"
                    ka "Oh you, poor, poor thing."
                    hide kaliruun
                    show torrsylos at left
                    n "Torr grumbles something impolite under his breath."
                    dr "Well- uh-"
                    dr "If you would like, perhaps we could deal with them together?"
                    dr "Maybe your uh...cousin could put his duster skills to better use?"
                    to "And what skills might those be?"
                    dr "Umm... you know... those stories I've heard..."
                    to "What stories."
                    hide doctor
                    show kaliruunsmile at right
                    ka "Dearest cousin... let's try to be a little more civil shall we?"
                    to "*unintelligible grumbles*"
                    hide torrsylos
                    show doctor at left
                    dr "You see, Dr. Kaliruun, these cousins of my wife are blood suckers."
                    ka "So cool! I didn't know those were real!"
                    dr "Oh. Oh no! Not like that!"
                    hide kaliruunsmile
                    show kaliruun at right
                    dr "Not in the literal sense! Oh dunes no. I'm quite sure those still do not exist."
                    dr "More like the kind that suck everything from your Rolser-Wen Interhaven Bank account, if you catch my drift."
                    ka "*dissapointed* Aww... I wanted to meet them. Maybe they would teach me some tricks."
                    dr "*takes a step back* Umm... tricks?"
                    hide kaliruun
                    show kaliruunsmile at right
                    ka "You know, like advancements in blood transfusions, of course!"
                    dr "*sighs with relief* Of course!"
                    hide kaliruunsmile
                    show torrsylos at right
                    to "Of course. Don't care. Do you want me to kill them or not?"
                    dr "Shhh!! Hypothetically, if I were to ask of you this favor, how much would I need to compensate you in return?"
                    jump assassination
    label sarcasm:
        $ toStats[0]-=1
        to "Have you heard of this thing called sarcasm?"
        to "It's a new fad among the kids these days."
        dr "Oh ummm..."
        dr "Oh umm..."
        dr "Ah yes that was-"
        dr "I have-"
        dr "A beeper"
        dr "It's beeping for me"
        dr "Can't you hear that?"
        dr "That- um..."
        dr "Big ringing in the ears?"
        dr "I mean beeping?"
        to "..."
        hide doctor
        n "The doctor makes a rapid exit, eager to avoid awkward conversations."
        show kaliruunsmile at right
        ka "I forgot how much I loved messing with Haven idiots!"
        ka "Wow, you have a straighter face than me."
        ka "And an absolutely incredible way with people."
        to "..."
        to "I know."
        jump part2
    label siblings:
        $ kaStats[0]+=1
        $ toStats[0]+=1
        $ relation = "sister"
        hide torrsylos
        hide kaliruun
        show doctor
        dr "You're all from the same parents??"
        hide doctor
        show torrsylos at left
        show kaliruun at right
        to "Obviously."
        ka "Don't you see the resemblance?"
        hide torrsylos
        show doctor at left
        dr "Um... well..."
        ka "I'm insulted!"
        ka "We are each other's spitting images!"
        ka "Our father's perfect heirs to the..."
        ka "throne of alcoholism."
        ka "I'm sure you've heard of it, it's quite a famous title."
        dr "I'm-I'm sure it is."
        ka "Maybe we don't look like siblings!?"
        ka "No!!"
        ka "My entire identity is being disrupted."
        hide doctor
        show torrsylos at left
        to "Dearest sister, calm yourself."
        ka "Do you... do you think the rumors of father's mistresses were right after all?"
        to "Perhaps."
        to "But it really would be a shame."
        to "Especially after I decapitated all of them."
        hide kaliruun
        show doctor at right
        dr "I-I... I see you are all very close."
        to "Very."
        dr "Uhmm... Uh I'll leave you with your sister then."
        hide doctor
        n "The doctor leaves, intent on avoiding awkward conversations."
        jump police
    label parents:
        $ kaStats[0]+=1
        $ toStats[0]+=1
        $ relation = "daughter"
        hide torrsylos
        hide kaliruun
        dr "Excuse me??"
        hide doctor
        show torrsylos at left
        show kaliruun at right
        ka "What? Did I stutter?"
        ka "My dearest husband, please tell me the truth, am I just an awful public speaker?"
        to "Love of the my life..."
        to "You are the moon's best public speaker to have ever publicly spoken in a doctor's office."
        hide kaliruun
        show kaliruunsmile at right
        ka "Oh my, you still give me butterflies!"
        ka "Just like when we had our first night together..."
        to "I remember our first night involving a few more peacetech officers and jailcells, but oh..."
        to "the memories..."
        hide torrsylos
        hide kaliruunsmile
        show doctor
        dr "Well... you seem to have a very... stable... relationship."
        dr "May I get the number of your cybernetic surgeon?"
        dr "They seem to have done wonders."
        dr "How old must you be?"
        dr "Never mind... I'm so sorry."
        dr "I can be awfully impolite at times."
        hide doctor
        show kaliruunsmile at right
        show torrsylossmile at left
        ka "Oh we don't mind!"
        ka "We married... when did we marry?"
        to "The first time or the fifth time?"
        ka "Well I was thinking the third, since of course that was the most memorable."
        to "Yes."
        to "Of course."
        to "I think it must have been at least a hundred years ago."
        to "It would be hard to forget all those cannibals."
        hide torrsylossmile
        show doctor at left
        dr "Cannibals?!"
        ka "Dear doctor, have you ever been to Reckless Abandon?"
        ka "They simply have the most delicious feasts."
        dr "..."
        hide kaliruunsmile
        show torrsylossmile at right
        to "Darling..."
        to "I believe our love is just too magnificent to be understood by mere Haven doctors."
        dr "..."
        dr "I'm not a mere Haven dweller."
        dr "I did graduate top of my class from Uskana University, I will have you know."
        to "Sorry, what did you say?"
        to "Oh wait."
        to "I could cut your tongue from your mouth in a very efficient amount of time."
        hide torrsylossmile
        show kaliruunsmile at right
        ka "How romantic, my love!"
        ka "Would you mind demonstrating?"
        dr "I-I have a... meeting to attend."
        dr "Concerning tongue surgery."
        hide doctor
        show torrsylossmile at left
        to "How disappointing."
        ka "Oh, let him go, we'll see him again!"
        ka "Won't we?"
        ka "I'd love to show you the Reckless Abandon-style cooking."
        hide torrsylossmile
        show doctor at left
        dr "..."
        dr "I hope to see you again..."
        dr "In Torobos' hellfires where you belong!"
        hide doctor
        n "The Doctor scurried off, clearly very, very interested in their meeting."
        n "And in getting out before he could be reprimanded for their last statement."
        ka "I forgot how much I loved messing with Haven idiots!"
        show torrsylos at left
        ka "Also Torr, I'll have you know, I could cut his tongue out faster than you could."
        to "Doubt it."
        to "We must have a contest to settle it at some point."
        ka "Sounds like a decent plan."
        ka "After we make some solid tetras."
        jump police
    label complicated:
        $ kaStats[0]+=1
        $ toStats[0]+=1
        $ relation = "step-sibling"
        hide doctor
        hide torrsylos
        show doctor at right
        ka "Well, we're her step-siblings on the third side from her second mother's first husband's Ganan mistress."
        dr "That seems extremely...."
        dr "Specific."
        dr "You still keep in touch then?"
        ka "Oh of course!"
        ka "We're nothing like those jerks on the second side of her second mother's first husband's Ganan mistress!"
        dr "Sorry, I didnt mean to offend."
        dr "I'm just... surprised."
        dr "You must have a very nice family."
        hide kaliruun
        show torrsylos at left
        to "Obviously."
        to "Once you kill all of your third cousins, the family reunions are quite enjoyable."
        dr "..."
        dr "Hypothetically, of course."
        to "Obviously."
        dr "And hypothetically..."
        dr "If one wished to unite their family in such a manner..."
        dr "How would one acquire the right person for the job?"
        dr "Hypothetically."
        dr "Of course."
        hide doctor
        show kaliruun at right
        n "Kaliruun and Torr, if not already obvious, would be the perfect people for the job."
        n "Their years together conning, occasionally killing, and very much pirating have them well trained for any such \"hypothetical\" situation."
        menu:
            "Pretend to be oblivious":
                jump oblivious
            "Offer their services":
                jump assassination
    label oblivious:
        python:
            kaStats[0] +=1
            kaStats[1] -=1
            toStats[0] +=1
            toStats[1] -=1
        hide kaliruun
        show kaliruunsmile at right
        ka "Wow, these hypotheticals are pretty fun aren't they!"
        ka "You should join our role-playing group!"
        to "We meet on Dustdays."
        hide torrsylos
        show doctor at left
        dr "I would be so honored!"
        dr "Do you play the 7th edition module for Cyboon 4RT?"
        ka "Why yes we do!"
        ka "You should see his character, quite the seducer."
        hide kaliruunsmile
        show torrsylos at right
        to "Yes."
        to "I am."
        dr "Oh, really?"
        dr "Why, sir... I would love to see you in action."
        to "..."
        dr "Until then, I will anxiously await the meeting of our characters..."
        to "..."
        hide doctor
        n "The doctor exits"
        show kaliruunsmile at left
        to "Was the doctor flirting with me."
        ka "At this point, I think you two are married."
        jump part2
    label assassination:
        $ kaStats[1]+=2
        $ toStats[1]+=2
        hide doctor
        show torrsylos at left
        show kaliruun at right
        ka "Well..."
        ka "Hypothetically..."
        ka "It would only cost a wooden tetra per person."
        hide torrsylos
        show doctor at left
        dr "A wooden tetra!"
        dr "Per person!"
        dr "Hypothetically, that would be outrageous."
        menu:
            "Keep the price":
                jump pricy
            "Barter down":
                jump bargain
    label pricy:
        hide doctor
        show torrsylos at left
        to "Not at all."
        ka "Hypothetically, that would be extremely reasonable."
        hide torrsylos
        show doctor at left
        dr "Too bad its all going to stay very, very hypothetical."
        hide doctor
        n "The Doctor barges out of the room, in no mood to spend so much money, even if it's to address extremely frustrating relatives."
        ka "I forgot how much I loved messing with Haven idiots."
        ka "But that one doesn't know how to take a fair deal!"
        show torrsylos at left
        to "You have no right to judge."
        to "Considering."
        ka "Considering what, exactly?"
        to "..."
        to "Everything."
        ka "How dare-"
        ka "Actually, you know, that's kind of true."
        to "Exactly."
        ka "Like you have any right to judge, either?"
        to "..."
        ka "Exactly."
        n "Torr shrugs."
        n "He isn't going to deny he had inflicted his fair share of terror."
        n "After all, he was raised in one of the most prestigious desert pirate families of all time."
        jump police
    label bargain:
        hide kaliruun
        show torrsylos at right
        to "Hypothetically, murder is a crime."
        hide torrsylos
        show kaliruun at right
        ka "I'm pretty sure murder is also a crime un-hypothetically..."
        hide kaliruun
        show kaliruunsmile at right
        ka "But have no fear! We understand that hypothetical tetras can be hard to come by sometimes."
        ka "I think an understanding can be reached."
        scene bg hospitalredo
        with dissolve
        show doctor at left
        show kaliruun at right
        dr "How does 6 cobalt sound to you?"
        n "Conversion Rates: 10 glass equals 1 cobalt, 10 cobalt equals 1 Yttrium, 10 Yttrium equals 1 wood."
        menu:
            "Accept it":
                jump deal
            "Barter for higher rate":
                jump rate
    label deal:
        ka "Sounds absolutely wonderful, as long as you promise it'll be fun."
        dr "Wonderful! Here's my number..."
        dr "I'll let you know the details later."
        hide doctor
        show torrsylos at left
        to "Fine."
        $ yttrium += 2
        $ wood += 1
        n "The fine doctor leaves, content to finally deal with his frustrating relatives."
        to "We're getting ripped off."
        ka "6 cobalt is better than zero."
        ka "Plus, it shouldn't be too hard."
        ka "At least it'll be something to keep us from being bored."
        jump part2
    label rate:
        python:
            toStats[0] += 1
            kaStats[0] += 1
            toStats[1] += 2
            kaStats[1] += 2
        hide kaliruun
        show torrsylos at right
        to "That's ridiculous."
        to "An easy assassination is 8 yttrium at least"
        to "What you're offering is 10 times less than that."
        dr "Well, I don't see how you can think that's reasonable."
        hide torrsylos
        show kaliruunsmile at right
        ka "Awww, Doctor, you don't have anyone else willing to do the job, do you?"
        dr "..."
        dr "No."
        dr "But I am a doctor! Not a technocrat!"
        dr "I can't just throw wood around like that."
        ka "8 yttrium and we have a deal"
        dr "..."
        hide kaliruunsmile
        show torrsylos at right
        to "Take it or leave it."
        dr "But..."
        hide torrsylos
        show kaliruunsmile at right
        ka "You won't find a better deal in all of Helnisk's moons."
        dr "..."
        dr "Fine!"
        dr "The family reunion takes place tomorrow."
        dr "Here's my number."
        $ wood +=16
        dr "If even one of them survives-"
        ka "We know the routine."
        ka "Don't worry your little Haven head about it."
        dr "My little Haven head?!"
        dr "(deep inhale)"
        dr "I'm choosing to ignore that comment."
        dr "I will send you the details tonight, then."
        ka "Wonderful!"
        ka "Pleasure doing business with you, Doctor."
        dr "I wish I could say the same."
        hide kaliruunsmile
        show torrsylos at right
        to "The feeling's mutual."
        hide torrsylos
        show kaliruunsmile at right
        ka "Oh shush."
        dr "If even one of them survives..."
        ka "Yes. We get it. Just go already."
        dr "Fine!"
        hide doctor
        n "And with that, the fine doctor leaves."
        jump part2

    label part2:
        n "onward"

    label police:
        scene bg hospitalredo
        n "Peacetech burst in to the peaceful hospital room."
        show p1 at left
        show torrsylos at right
        p1 "No one expects the Peacetech Investigation!"
        to "*scoffs* That was quick."
        hide p1
        show kaliruun at left
        ka "I know right? I was expecting at least a day before we got officers on our ass."
        hide kaliruun
        show p1 at left
        p1 "No! No one expects the Peacetech Investigation!"
        hide torrsylos
        show kaliruunsmile at right
        ka "Whatever could we have done to warrant such an investigation?"
        ka "Oh!"
        ka "Oh is this because, we're, dare I say it..."
        ka "from outside of the Haven?"
        hide p1
        show p2 at left
        p2 "No. We do not discriminate on Haven-status."
        hide p2
        show p1 at left
        p1 "Wait I thought you said-"
        hide peacetech1
        show peacetech2 at left
        p2 "No. Like I said before. We do not discriminate on Haven-status."
        ka "What exactly did the good officer say?"
        ka "I'm ever so curious."
        hide peacetech2
        show peacetech1 at left
        p1 "Well she said that you might be-"
        hide peacetech1
        show peacetech2 at left
        p2 "I said nothing."
        hide peacetech2
        show torrsylos at left
        to "Officer, we have just dropped off our dearest..."
        ka "[relation]"
        to "Our dearest [relation] to this hospital, what seems to be the problem?"
        hide torrsylos
        hide kaliruunsmile
        show peacetech1 at left
        show peacetech2 at right
        p1 "You're under arrest!"
        p2 "*Heavy sigh* No you are not."
        p2 "We are here for a civil conversation. All we want is more information on your relation to..."
        p2 "*Squints at medical screen*"
        p2 "... O"
        p2 "O Dajer?"
        p1 "Oh! Oh my sands! Isn't she #10 on the top ten most wanted in Suda?"
        p1 "I recognize her from the Peacetech Chill Lounge and Community Station™!"
        hide peacetech1
        hide peacetech2
        show kaliruun at left
        show torrsylos at right
        to "Oh by the damned shifting sands!"
        ka "Tkha!"
        ka "Kadza whal so tkhabo khuuzu sidaghan-bak uuzi gha tkhabobai..."
        to "I take no blame for this. It was your idea start to finish."
        ka "Mine? Well sure I'll take credit if you want me to but I wasn't the one who skipped a background check on her!"
        to "She's a driver. She's Arrow. I didn't think a background check was necessary."
        ka "I mean sure everyone who's ever watched an inter-Haven broadcast puts bets on their favorite driver but that's not exactly..."
        ka "an endorsement?"
        ka "I mean am I trustworthy just cuz a lotta people know my name?"
        hide torrsylos
        hide kaliruun
        show peacetech1 at left
        show peacetech2 at right
        p2 "Enough now. Identification please."
        p1 "And then we'll put you under arrest!"
        p2 "*sighs*"
        hide peacetech1
        show kaliruun at left
        ka "... identification! Right. That thing. That ever so important document that I have..."
        ka "That I have somewhere 'round here..."
        ka "Actually well uh didn't those pirates take off with our papers and...?"
        hide kaliruun
        show torrsylos at left
        to "Yes. They took everything we had."
        to "It was a miracle we made it here."
        p2 "*louder* Identification. NOW."
        n "With that last fateful pronunciation, our dearest Arrow, O Dajer of the top 10 most wanted, bolts awake."
        n "She looks dizzy, woozy, weak, but what comes next is nothing but-"
        hide torrsylos
        hide peacetech2
        show odajerhospital at right
        o "FUCK"
        show kaliruunsmile at left
        ka "Welcome to the party!"
        hide kaliruunsmile
        show kaliruun at left
        ka "*turns to Torr* Can we go now?"
        n "The newly awakened O Dajer looks around in a daze, clearly looking for someone not there."
        o "Where's Dark Angel?"
        hide odajerhospital
        show peacetech1 at right
        p1 "*Gasp* Number 8 on the list?"
        ka "What list?"
        p1 "The top ten most wanted!"
        p1 "Oh today is so exciting!"
        hide peacetech1
        show peacetech2 at right
        p2 "When was the last time you came into contact with Dark Angel?"

    return