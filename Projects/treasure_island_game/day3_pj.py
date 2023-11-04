# Print ASCII Treasure Box
print(r'''
                                  _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')

# Welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Users first encounter: Left or Right?
user = input('''
The map's cryptic instructions emphasized the significance of this choice. Contemplating the possibilities, 
they remembered the warnings of dire consequences for taking the wrong path.
The treasure hunter stood at a crucial junction on Treasure Island, facing the first decision:
Left or Right? 
''')

# If it is anything but left, player falls into hole, Game over.
if user != "Left":
    print('''                                                                                                          
                                                                                                                                                                                                                                                                               
                                                                  ░░  ░░░░░░                                                                          
                                                        ░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░  ░░░░                                                              
                                                    ░░▒▒▓▓▓▓▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░░░                                                                  
                                                  ▒▒▒▒██▓▓▓▓▒▒▓▓▓▓░░▒▒░░▒▒░░▓▓░░░░    ░░░░░░                                                          
                                              ░░▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░                                                                    
                                              ▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒▓▓▒▒░░░░░░    ░░░░                                                          
    Hole ->                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒░░▒▒░░░░    ░░░░                                                          
                                              ░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░▒▒░░                                                                
                                                ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░                                                                  
                                                  ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒░░▓▓░░  ░░                                                            
                                                      ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒░░░░                                                              
                                                            ░░░░▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░▒▒░░░░░░                                                              
                                                                          ░░     
                                                                              
    After a moment of deliberation, the seeker decided to venture right. 
    This path seemed ominous, with thick undergrowth and a sense of foreboding. 
    The decision to take this route turned out to be perilous as the unsuspecting adventurer fell into a concealed pit, abruptly ending their journey.
    
    GAME OVER.
    ''')
# Else player made the right choice, now decides: Swim or Wait?
else:
    print('''
\nAfter careful consideration, the seeker bravely opted for the left route. As they walked, 
the path took on an enchanting ambiance, filled with ethereal glows and a sense of mystery. 
They encountered the glade where the treasure awaited, affirming that their decision to turn left was indeed a safe and rewarding choice.

Their journey continued, and they encountered a wide river blocking their way. 
Remembering the map's guidance to swim, but sees a boat of people heading towards the seeker.
The treasure hunter pondered the risks.
Swim or Wait?

''')
    # If player choose to wait, print ASCII, Game over.
    user = input()
    if user == "Wait":
        print('''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`

The seeker hesitated and decided to wait, hoping for the people help during this circumstance.
Unfortunately, the people seem to be unfriendly pirates and slaughtered the poor seekers life.

GAME OVER.
              ''')
    # Else final decision: Blue, Yellow, or Red?
    else:
        print('''
After careful consideration, the seeker decided to take the plunge and swim across the river.
The water was crystal clear, and as they swam, a shimmering school of friendly fish encircled the adventurer, 
guiding them safely to the opposite bank.

Emerging from the water, the treasure hunter felt relieved, 
confirming that their choice to swim was indeed the correct and safe one.

Advancing forward, the seeker found themselves in front of a door with three choices: blue, yellow, or red. 
Remembering the importance of this decision, they paused to weigh the implications of each color. 
Blue, Yellow, or Red?
              ''')
        
        # If either blue or red, game over. Else, Player wins.
        user = input()
        if user == "Red":
            print('''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    As the door creaked open, a fiery inferno erupted from within, consuming the treasure hunter.
 
    GAME OVER.
                  ''')
        elif user == "Blue":
            print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            
            
            
            The seeker decided to test fate and open the blue door. 
            As the door swung open, a menacing growl echoed from within, 
            and a ferocious horde of beasts leaped forth, 
            overwhelming the treasure hunter and leading to an abrupt 
            and unfortunate end to their quest.
            
            GAME OVER.
                  ''')
        else:
            print('''

  ▓██   ██▓ ▒█████   █    ██     █     █░ ██▓ ███▄    █  ▐██▌    
   ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▓██▒ ██ ▀█   █  ▐██▌    
    ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒ ▐██▌    
    ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒ ▓██▒    
    ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░██░▒██░   ▓██░ ▒▄▄     
     ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒  ░▀▀▒    
   ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░   ▒ ░░ ░░   ░ ▒░ ░  ░    
   ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░   ▒ ░   ░   ░ ░     ░    
   ░ ░         ░ ░     ░            ░     ░           ░  ░       
   ░ ░                                                           

            As the door swung open, it revealed a passage to a room filled 
            with ancient artifacts and the sought-after treasure. 
            The room was safe and filled with riches, marking the choice 
            of the yellow door as a successful and rewarding decision. 
                  ''')