#Quiz problems
problem = {
    'easy': 'The Earth\'s _____ consists of various _____, with 78% _____, 21% _____, 0.93% _____, and others including _____ dioxide.',
    'medium': 'On August 21st, 2017, there was a total solar _____. A solar eclipse is a _____ event that occurs when the _____ of the Moon causes it to _____ the Sun. As this takes place, the Moon casts an _____ shadow on the Earth, maximizing when the eclipse reaches _____.',
    'hard': '_____ is the _____ _____ of _____ that occurs gradually over time through natural _____ and _____.'
}

#Corresponding vocab lists, meant to be used to fill in blanks to complete above problems
vocab = {
    'easy': ['carbon', 'xenon', 'oxygen', 'argon', 'gases', 'neon', 'atmosphere', 'lithium', 'nitrogen'],
    'medium': ['rotation', 'planetary', 'orbit', 'umbra', 'eclipse', 'totality', 'corona', 'obscure', 'celestial'],
    'hard': ['niche', 'genetic', 'Darwin', 'selection', 'species', 'Evolution', 'adaptation', 'survival', 'variation']
}

#Corresponding solutions to each problem
solution = {
    'easy': ['atmosphere', 'gases', 'nitrogen', 'oxygen', 'argon', 'carbon'],
    'medium': ['eclipse', 'celestial', 'orbit', 'obscure', 'umbra', 'totality'],
    'hard': ['Evolution', 'genetic', 'variation', 'species', 'selection', 'adaptation']
}

##################################

#The dialog given before each game
def gameStart():
    """
    The beginning dialog before each game
    Player can choose difficulty
    Difficulty input should be ALL CAPS
    """
    diff_setting = raw_input('Choose difficulty level: [EASY, MEDIUM, HARD] or type "exit"\n')
    if diff_setting == 'EASY':
        return gamePlay('easy')
    elif diff_setting == 'MEDIUM':
        return gamePlay('medium')
    elif diff_setting == 'HARD':
        return gamePlay('hard')
    elif diff_setting == 'exit':
        return
    else:
        gameStart()

#Plays the game by asking user to fill in each blank one by one, from start to finish
#If the correct answer is put in, the program fills in the blank and moves on to the next blank
#If the incorrect answer is given, the user is asked to try again.
#When finished, the game goes to gameEnd dialog
def gamePlay(difficulty):
    """
    This begins the game
    Different (difficulty) inputs result with different games
    Acceptable inputs: 'easy', 'medium', 'hard'
    """
    d = difficulty
    i = 0 #index
    answer = problem[d]
    totalBlanks = problem[d].count('_____')
    print 'Your problem and vocab list:\n' + str(problem[d]) + '\n' + str(vocab[d]) + '\nFill in the blanks from start to finish using the provided vocab list until the sentence is completed'
    while i < totalBlanks:
        user_input = raw_input('Fill in the blank:\n')
        if user_input == solution[d][i]:
            answer = answer.replace('_____', str(user_input), 1)
            print 'Correct!\n' + str(answer)
            i += 1
        else:
            print 'Try again!'
    print 'Well done!'
    return gameEnd()

#The dialog given at the end of each game
def gameEnd():
    """
    This is a dialog given at the end of each game
    Typing "restart" will run print gameStart()
    """
    user_input = raw_input('Type "restart" to play again. Type "exit" to close.\n')
    if user_input == 'restart':
        return gameStart()
    elif user_input == 'exit':
        return
    else:
        gameEnd()

print gameStart()
