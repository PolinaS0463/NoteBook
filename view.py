import text
from model import NoteBook

def show_note(note_id: int, book: NoteBook):
    with open(book.notebook[note_id].note_path, 'r') as note:
        lines = note.readlines()
    lens = [len(line[:-1]) for line in lines]
    if lens: 
        max_len = max(lens)
        if len(book.notebook[note_id].header) <= 44: 
            if max_len <= 44: max_len = 44
        else: 
            if max_len <= len(book.notebook[note_id].header): max_len = len(book.notebook[note_id].header)
    if not lens:
        if len(book.notebook[note_id].header) > 44: max_len = len(book.notebook[note_id].header)
        else: max_len = 44
    print_border(max_len)
    print(book.notebook[note_id].header)
    print_dates(book.notebook[note_id].creation_date, book.notebook[note_id].last_changes_date)
    for line in book.notebook[note_id].content:
        print(line)
    print_border(max_len) 

def print_menu(menu) -> int:
    for i, item in enumerate(menu):
        if i == 0:
            print("\n" + item)
        else:
            print(f'{i}. {item}')
    while True:
        user_choice = input(text.select_menu_item_id)
        if user_choice.isdigit() and 0 < int(user_choice) < len(menu):
            return int(user_choice)
        else:
            print(text.invalid_menu_item_error)

def show_notebook(book: NoteBook) -> None:
    lens = [len(note.full(book)) for note in book.notebook]
    max_len = max(lens)
    print('\n' + '>' * max_len)
    for id in range(len(book.notebook)):
        print(book.notebook[id].full(book))
    print('>' * max_len + "\n")

def input_note_content(input_msg: str) -> list[str]:
    note_content = []
    line = ''
    while True:
        line = input_request(input_msg)
        if line != "-": note_content.append(line)
        else: break
    return note_content

def get_id(input_msg: str, book: NoteBook):
    while True:
        note_id = input_request(input_msg)
        if note_id.isdigit() and int(note_id) >= 1 and int(note_id) <= len(book.notebook): return note_id
        else: print(text.invalid_note_id_error(len(book.notebook)))

def print_dates(creation_date: str, last_changes_date: str) -> None:
    print('\n' + '*' * 44) 
    print(f"{text.creation_date} {creation_date}")
    print(f"{text.last_changes_date} {last_changes_date}")
    print('*' * 44 + '\n')

def print_message(msg: str) -> None:
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')

def print_border(border_length: int) -> None:
    print("\n" + "-" * border_length)

def input_request(msg: str) -> str:
    return input(msg)
