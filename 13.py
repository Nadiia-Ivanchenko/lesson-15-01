def correct_sentence(text):
    # Перевірка чи речення закінчується крапкою
    if not text.endswith('.'):
        # Виправлення речення: велика літера на початку та додавання крапки в кінці
        text = text.capitalize() + '.'
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')