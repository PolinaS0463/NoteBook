# Меню / Menu:
# ----------------------------------------------------------
main_menu = ["- Главное меню -",
              "Показать список заметок и папок;",
              "Открыть заметку для чтения;",
              "Создать новую заметку;",
              "Удалить заметку;",
              "Редактировать заметку;",
              "| Выход |"
              ]

# Ввод выбора выриантов / Selection options prompts:
# ----------------------------------------------------------
select_menu_item_id = "Выберите пункт меню: "
select_note_to = "Выберите заметку для "

# Подтверждения / Сonfirmations:
# ----------------------------------------------------------
restore_notes = "Ранее вы уже создавали заметки: вы хотите восстановить их и продолжить с ними работу? (ENTER для отмены): "

# Приглашения ко вводу / Input prompts:
# ----------------------------------------------------------
input_note_header = "Введите название заметки: "
input_note_content = "Введите строку (для перехода на новую строку нажмите ENTER или '-', чтобы закончить писать заметку): "
edit_note_header = "Введите новое название заметки: "
edit_note_content = "Введите новое содержание заметки (для перехода на новую строку нажмите ENTER или '-', чтобы закончить писать заметку): "
input_sample_to_search = "Введите ключевое слово для поиска: "

# Доп. текст / Extra text:
# ----------------------------------------------------------
actions = ["создана", "удалена", "отредактирована"]
options = ["чтения", "удаления", "редактирования"]
creation_date = "Дата создания:"
last_changes_date = "Дата последнего изменения:"
your_notes = "Ваши заметки: "
notes_restored_successfully = "Заметки успешно восстановлены!"

# Ошибки / Errors:
# ----------------------------------------------------------
invalid_menu_item_error = f"Введите корректный пункт меню! Пункт меню представляет собой ЧИСЛО от 1 до {len(main_menu) - 1}!"
invalid_file_name_error = "Имя файла недопустимо, или файл с таким именем уже существует! Попробуйте еще раз!"
empty_notebook_error = "Заметки пустые! Сначала создайте заметку!"

# Выход из программы / Exit the program:
# ----------------------------------------------------------
exiting = "Внимание! Выполняется выход из программы!"

# Функции / Functions:
# ----------------------------------------------------------
def note_action(name: str, action: str) -> str:
    return f"Заметка {name} успешно {action}!"

def note_option(option: str) -> str:
    return f"Выберите заметку для {option}: "

def note_not_found(sample: str) -> str:
    return f"По вашему запросу {sample} ничего не найдено!"

def invalid_note_id_error(notebook_length: int):
    return f"Заметки с таким ID не существует! ID заметки представляет собой ЧИСЛО от 1 до {notebook_length}"