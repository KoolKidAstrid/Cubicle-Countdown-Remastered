import random
import time


class char():
    name = None
    pronouns = []
    pronounsList = [['he', 'his', 'him', 'his', 'himself'], ['she', 'her', 'her', 'hers', 'herself'], ['they', 'their', 'them', 'theirs', 'theirself'], ['xe', 'xer', 'xer', 'xers', 'xerself']]

    lvl = 1
    xp = 0
    statPoints = 27
    stats = [['STR', 8], ['DEX', 8], ['CON', 8], ['INT', 8], ['WIS', 8], ['CHA', 8]]

    skillPoints = 12
    skills = [['Athletics']]

    def modOf(self, stat):
        return round((stat-10.1)/2)

    def skillCheck(self, DC, mod):
        roll = random.randint(1, 20) + mod
        if roll >= DC:
            return True
        else:
            return False

    def printSheet(self):
        print('--\nName: ' + char.name + ' (' + char.pronouns[0] + '/' + char.pronouns[2] + '/' + char.pronouns[3] +')')
        print('Level: ' + str(char.lvl))
        print('Experience: ' + str(char.xp) + '/' + str(char.lvl*char.lvl*100))
        print('Unused Stat Points: ' + str(char.statPoints))
        for s in char.stats:
            mod = char.modOf(char, s[1])
            modText = '0'
            if mod >= 0:
                modText = '+' + str(mod)
            if mod < 0:
                modText = str(mod)
            print(s[0] + ': ' + str(s[1]) + ' (' + modText + ')')
        print('--')

#Setup#
setup = False
while setup == False:
    print('Welcome to Cubicle Countdown Remastered, which follows the story of an office employee at Cre-8 Incorporated, living in the shining corporate capital of Brasília.')
    nameBool = False
    while nameBool == False:
        char.name = input('What is your name?\n--\n').capitalize()
        answer = input('Is ' + char.name + ' correct? (y/n)\n--\n')

        if answer.lower() == 'y':
            nameBool = True
    pronounsBool = False
    while pronounsBool == False:
        print('--\nWhat pronouns does ' + char.name + ' use?')
        for p in char.pronounsList:
            print(str(char.pronounsList.index(p)+1) + ' - ' + p[0] + '/' + p[2] + '/' + p[3])
        answer = input('Type a number...\n--\n')
        if answer.isnumeric() == True:
            if int(answer) > 0 and int(answer) < 5:
                char.pronouns = char.pronounsList[int(answer)-1]
                answer2 = input('Is ' + '(' + char.pronouns[0] + '/' + char.pronouns[2] + '/' + char.pronouns[3] +')' + ' correct? (y/n)\n--\n')
                if answer2 == 'y':
                    pronounsBool = True
                else:
                    input('Invalid Input!')
            else:
                input('Invalid Input!')
        else:
            input('Invalid Input!')
    statsBool = False
    while statsBool == False:
        print('--\nUnused Stat Points: ' + str(char.statPoints))
        for s in char.stats:
            mod = char.modOf(char, s[1])
            modText = '0'
            if mod >= 0:
                modText = '+' + str(mod)
            if mod < 0:
                modText = str(mod)
            print(str(char.stats.index(s) + 1) + ' - ' + s[0] + ': ' + str(s[1]) + ' (' + modText + ')')
        if char.statPoints == 0:
            print('--\ntype \'done\' to complete\n--')
        answer = input('What stat to add points to? (type a number)\n--\n')
        if answer == 'done' and char.statPoints == 0:
            statsBool = True
        elif answer.isnumeric():
            if int(answer) > 0 and int(answer) < 7:
                num = char.stats[(int(answer)-1)]
                answer2 = input('You have selected ' + num[0] + '.  How many points would you like to add or subtract?\n--\n')
                if answer2.isnumeric() or (answer2[0] == '-' and answer2[1:].isnumeric()):
                    if num[1] + int(answer2) > 20 or num[1] + int(answer2) < 0:
                        input('Stats may not be greater than 20 or less than 7.')
                    elif int(answer2) > char.statPoints:
                        input('You can\'t spend more points than you have!')
                    else:
                        char.stats[int(answer)-1][1] += int(answer2)
                        char.statPoints -= int(answer2)
                else:
                    input('Invalid Input!')
            else:
                input('Invalid Input!')
        else:
            input('Invalid Input!')

    char.printSheet(char)
