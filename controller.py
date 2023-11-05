from model import NoteBook
import view, text

def start():
    nb = NoteBook()
    if nb.check_restoring():
        restoring = view.input_request(text.restore_notes)
        if restoring:
            nb.restore_notes()
            view.print_message(text.notes_restored_successfully)
    while True:
        user_choice = view.print_menu(text.main_menu)
        match user_choice:
            case 1:
                if nb.notebook: view.show_notebook(nb)
                else: view.print_message(text.empty_notebook_error)
            case 2: 
                if nb.notebook:
                    view.show_notebook(nb)
                    note_id = int(view.get_id(text.note_option(text.options[0]), nb)) - 1
                    view.show_note(note_id, nb)
                else: view.print_message(text.empty_notebook_error)
            case 3:
                header = view.input_request(text.input_note_header)
                content = view.input_note_content(text.input_note_content)
                nb.create_note(header, content)
                view.print_message(text.note_action(header, text.actions[0]))
            case 4:
                if nb.notebook:
                    view.show_notebook(nb)
                    note_id = int(view.get_id(text.note_option(text.options[1]), nb)) - 1 
                    note = nb.notebook[note_id]
                    nb.delete_note(note_id)
                    view.print_message(text.note_action(note.header, text.actions[1]))
                else: view.print_message(text.empty_notebook_error)
            case 5:
                if nb.notebook:
                    view.show_notebook(nb)
                    note_id = int(view.get_id(text.note_option(text.options[2]), nb)) - 1
                    note = nb.notebook[note_id]
                    new_header = view.input_request(text.input_note_header)
                    new_content = view.input_note_content(text.edit_note_content)
                    nb.edit_note(note_id, new_header, new_content)
                    view.print_message(text.note_action(note.header, text.actions[2]))
                else: view.print_message(text.empty_notebook_error)
            case 6:
                view.print_message(text.exiting)
                nb.exit_program()

        