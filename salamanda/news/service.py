def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        # В REMOTE_ADDR значение айпи пользователя
        ip = request.META.get('REMOTE_ADDR')
    return ip


def add_str_tags(data):
    """Добавление ключевых слов пользователя в стороку"""
    key_word = []

    for item_dict in data:
        for key, value in item_dict.items():
            if key == 'title':
                key_word.append(value)
    string = ','.join(key_word)
    return string
