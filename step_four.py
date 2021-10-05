
while True:
    starting_field = input("Enter cells: ")

    # check if input is correct length
    if len(starting_field) == 9:
        allowed_characters = ['X', 'O', '_']

        # check if user enters only allowed characters
        if any(x not in allowed_characters for x in starting_field):
            print("Please use only X, O or _")
            continue

        else:
            break

    elif len(starting_field) != 9:
        print('Please enter 9 symbols (X, O or _)')
        continue
    else:
        break

# i use dictionary to give possibility for entering the coordinates
field = {
    '1 1': ' ', '1 2': ' ', '1 3': ' ',
    '2 1': ' ', '2 2': ' ', '2 3': ' ',
    '3 1': ' ', '3 2': ' ', '3 3': ' '
}

# here i transfer entered symbols to game field
keys = list(field)

for c in range(len(starting_field)):
    # here i transform _ into space sign
    if starting_field[c] == '_':
        field[keys[c]] == ' '
    else:
        field[keys[c]] = starting_field[c]
    

field_entries = []

allowed_coordinates = [
    '1 1', '1 2', '1 3',
    '2 1', '2 2', '2 3',
    '3 1', '3 2', '3 3'
]

# to check if input has only digits and spaces
allowed_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

# loop for updating field
for entry in field:
    field_entries.append(entry)


def create_field():
    print('---------')
    print('| ' + field['1 1'] + ' ' + field['1 2'] + ' ' + field['1 3'] + ' |')
    print('| ' + field['2 1'] + ' ' + field['2 2'] + ' ' + field['2 3'] + ' |')
    print('| ' + field['3 1'] + ' ' + field['3 2'] + ' ' + field['3 3'] + ' |')
    print('---------')


def winner_check(sign):
    # horizontal check
    if field['1 1'] == field['1 2'] == field['1 3'] == sign:
        return True

    elif field['2 1'] == field['2 2'] == field['2 3'] == sign:
        return True

    elif field['3 1'] == field['3 2'] == field['3 3'] == sign:
        return True

    # vertical check
    elif field['1 1'] == field['2 1'] == field['3 1'] == sign:
        return True

    elif field['1 2'] == field['2 2'] == field['3 2'] == sign:
        return True

    elif field['1 3'] == field['2 3'] == field['3 3'] == sign:
        return True

    # diagonal check
    elif field['1 1'] == field['2 2'] == field['3 3'] == sign:
        return True

    elif field['1 3'] == field['2 2'] == field['3 1'] == sign:
        return True

    else:
        return False


# main game function
def tic_tac_toe():
    turns = 9 - starting_field.count('_')
    player = 'X'

    if turns <= 9:
        create_field()
        if winner_check('X'):
            print('X wins')
            exit()
        elif winner_check('O'):
            print('O wins')
            exit()
        elif turns == 9:
            print('Draw')
            exit()

    if turns % 2 == 1:
        player = 'O'

    while turns < 9:
        move = input('Enter the coordinates: ')
        digits_check = all(c in allowed_inputs for c in move)

        # input check
        if digits_check == False:
            print('You should enter numbers!')
            continue

        else:
            if move not in allowed_coordinates:
                print('Coordinates should be from 1 to 3!')
                continue
        
        # to check if cell is free
        if field[move] == ' ':
            field[move] = player
            turns += 1

        else:
            print('This cell is occupied! Choose another one!')
            continue

        create_field()

        # minimal amount of moves needed to win
        if turns >= 5:
            if winner_check(player):
                print(player + ' wins')
                break
        
        if turns == 9:
            print('Draw')
            break
        
        # to change player every move
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


if __name__ == '__main__':
    tic_tac_toe()
