field = input("Enter cells: ")

# check if input is correct length
if len(field) == 9:
    field_list = [x for x in field]
    allowed_characters = ['X', 'O', '_']

    if any(x not in allowed_characters for x in field):
        print("Please use only X, O or _")

    else:
        lines = "---------"
        first_field = "| " + field_list[0] + " " + field_list[1] + " " + field_list[2] + " |" 
        second_field = "| " + field_list[3] + " " + field_list[4] + " " + field_list[5] + " |" 
        last_field = "| " + field_list[6] + " " + field_list[7] + " " + field_list[8] + " |" 

        print(lines)
        print(first_field)
        print(second_field)
        print(last_field)
        print(lines)

elif len(field) != 9:
    print('Please enter 9 symbols')


def winner_check():
    free_cells = field.count('_')
    if rules("X"):
        print("X wins")
    elif rules("O"):
        print("O wins")
    else:
        if free_cells == 0:
            print("Draw")
        else:
            print("Unfinished game")


def rules(sign):
    # horizontal check
    if field_list[0] == field_list[1] == field_list[2] == sign:
        return True
    elif field_list[3] == field_list[4] == field_list[5] == sign:
        return True
    elif field_list[6] == field_list[7] == field_list[8] == sign:
        return True

    # vertical check
    elif field_list[0] == field_list[3] == field_list[6] == sign:
        return True
    elif field_list[1] == field_list[4] == field_list[7] == sign:
        return True
    elif field_list[2] == field_list[5] == field_list[8] == sign:
        return True
    
    # diagonal check
    elif field_list[0] == field_list[4] == field_list[8] == sign:
        return True
    elif field_list[2] == field_list[4] == field_list[6] == sign:
        return True
    else:
        return False


if __name__ == '__main__':
    winner_check()
    