
init -1 python:
    from renpy_tracery import TraceryCharacter as TC
    # Define Tracery grammar for Eileen.
    example_grammar = {
        'greetings': ['hello', 'hi', 'hey'],
    }
    # Define Tracery grammar for narrator character.
    narrator_grammar = {
        'eileen': ['Eileen', 'dear Eileen', 'sweet Eileen'],
        'girl': ['girl', 'young lady'],
        'once': ['one day', 'one time', 'some day', 'once'],
        'moody': ['moody', 'grumpy', 'bad-tempered', 'ill-tempered']
    }

define e = TC("Eileen", grammar=example_grammar)
define narrator = TC(None, grammar=narrator_grammar)

# The game starts here.

label start:

    "This is the story about #eileen#."

    e "#greetings#"

    "#eileen.capitalize# was a pretty #girl# living next door."
    
    "#once.capitalize# I met her in the park."
    
    e "#greetings.capitalize#! How are you today?"

    "I was not very kind to her. In fact, I was #moody# that day."

    "I told her, I did not want to talk to her."

    "She cryed and ran away. I never saw my #eileen# after that day."

    return
