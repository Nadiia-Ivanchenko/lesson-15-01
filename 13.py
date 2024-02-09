def correct_sentence(text):
    # Перевірка чи речення не закінчується крапкою
    if not text.endswith('.'):
        # Виправлення речення: велика літера на початку та додавання крапки в кінці
        text = text + '.'
    return text[0].upper()+text[1:]

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')