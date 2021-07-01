import random
import string


def random_string_generator():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    result = ''
    for i in range(0, 11):
        result += random.choice(characters)

    return result


def unique_command_id_generator(instance):
    codeCommand_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(codeCommand=codeCommand_new_id).exists()
    if qs_exists:
        return unique_command_id_generator(instance)
    return codeCommand_new_id