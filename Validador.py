import re

# Expressão regular para validar endereços de e-mail
email_regex = r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=^_`{|}~-]{2,})*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'



# Lista de endereços de e-mail para testar
emails = [
    "dudukochen@gmail.com",
    "dudukochen@gmail.c",
    "dudukochen@-gmail.com",
    "dudu..kochen@gmail.com.com",
    "teste..teste@gmail.com",
    "email3@example.com",
    "invalid_email",
    # Adicione mais endereços de e-mail aqui
]

for email in emails:
    if re.match(email_regex, email):
        print(f"{email} é um endereço de e-mail válido.")
    else:
        print(f"{email} não é um endereço de e-mail válido.")
