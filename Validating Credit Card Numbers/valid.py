def validate_credit_card(card_number):
    card_number = card_number.strip()

    if card_number[0] not in '456':
        return "Invalid"

    if not all(c.isdigit() or c == '-' for c in card_number):
        return "Invalid"

    if '-' in card_number:
        groups = card_number.split('-')
        if len(groups) != 4 or any(len(group) != 4 for group in groups):
            return "Invalid"
    else:
        if len(card_number) != 16 or not card_number.isdigit():
            return "Invalid"

    card_number = card_number.replace('-', '')

    for i in range(len(card_number) - 3):
        if card_number[i] == card_number[i + 1] == card_number[i + 2] == card_number[i + 3]:
            return "Invalid"

    return "Valid"


n = int(input())

for _ in range(n):
    card_number = input().strip()
    print(validate_credit_card(card_number))