user_text = input('please enter any text ').lower()
letter = []
letter.append(input('entre 1 letter ').lower())
letter.append(input('entre 2 letter ').lower())
letter.append(input('entre 3 letter ').lower())

print(f'letter 1 {user_text.count(letter[0])} letter 2 {user_text.count(letter[1])} letter 3 {user_text.count(letter[2])} \n  how many words {len(user_text)} firs letter {user_text[0]} ood letter {user_text[-1]} \n Phyton exist in text ? {user_text.find("Python") > 1}')



