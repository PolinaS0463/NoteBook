import os, sys
from genericpath import getctime, getmtime
from datetime import datetime
from pathlib import Path


class NoteBook:
    def __init__(self, notebook: list = None, notebook_path: str = "Заметки"):
        self.notebook_path = notebook_path
        if notebook is None: self.notebook: list[Note] = []
        else: self.notebook = notebook
        
    def create_note(self, note_header: str, note_content: str) -> None:
        note_path = os.path.join(self.notebook_path, note_header)
        self.notebook.append(Note(note_header, note_path, datetime.now().strftime("%d.%m.%Y, %H:%M"), datetime.now().strftime("%d.%m.%Y, %H:%M"), note_content))
        with open(note_path, 'a') as note:
            note.writelines(f"{line}\n" for line in note_content)
        
    def delete_note(self, note_id: int) -> None:
        os.remove(self.notebook[note_id].note_path)
        self.notebook.pop(note_id)

    def edit_note(self, note_id: int, new_header: str, new_content: str) -> None:
        self.notebook[note_id].header, self.notebook[note_id].content = new_header, new_content
        os.rename(self.notebook[note_id].note_path, os.path.join(self.notebook_path, new_header))
        self.notebook[note_id].note_path = os.path.join(self.notebook_path, new_header)
        self.notebook[note_id].last_changes_date = datetime.now().strftime("%d.%m.%Y, %H:%M")
        with open(self.notebook[note_id].note_path, 'w') as note:
            note.writelines(f"{line}\n" for line in new_content)
    
    def restore_notes(self) -> None:
        path = Path("Заметки")
        for note_path in path.rglob("*"):
            with open(note_path, 'r') as note:
                restore_content = note.read().splitlines() # Чтобы избежать символа \n при чтении из файла;
            restore_header = os.path.basename(note_path) # Чтобы получить название файла, например: "Заметки/Ваша_заметка", в данном случае "Ваша заметка" - название файла;
            restore_creation_date = datetime.fromtimestamp(getctime(note_path)).strftime("%d.%m.%Y, %H:%M") # Чтобы узнать дату создания
            restore_last_changes_date = datetime.fromtimestamp(getmtime(note_path)).strftime("%d.%m.%Y, %H:%M") # и последнего изменения файла;
            self.notebook.append(Note(restore_header, note_path, restore_creation_date, restore_last_changes_date, restore_content))

    def exit_program(self) -> None:
        sys.exit()

    def check_file(self, note_header: str) -> bool | str:
        if "/" in note_header: return False                        
        note_path = os.path.join(self.notebook_path, note_header)
        if os.path.exists(note_path): return False
        return note_path
    
    def check_restoring(self) -> bool:
        if len(os.listdir("Заметки")) != 0: return True # В начале программы метод проверяет, есть ли в папке "Заметки" файлы;

    def get_note_index(self, note) -> int:
        return self.notebook.index(note)

class Note:
    def __init__(self, header: str, note_path: str, creation_date: str, last_changes_date: str, content: str) -> None:
        self.header = header
        self.note_path = note_path
        self.creation_date = creation_date
        self.last_changes_date = last_changes_date
        self.content = content

    def full(self, book: NoteBook) -> str:
        return f"{book.get_note_index(self) + 1}. {self.header} - {self.creation_date} - {self.last_changes_date}"