with open('Input/Letters/starting_letter.txt', mode='r') as starting_letter:
    with open('Input/Names/invited_names.txt', mode='r') as names:
        letter = starting_letter.read()
        names = names.read().split('\n')
        for name in names:
            letter = letter.replace('[name]', name)
            with open(f'Output/ReadyToSend/letter_for_{name}.txt', mode='w') as output:
                output.write(letter)
