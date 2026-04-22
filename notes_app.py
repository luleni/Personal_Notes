notes = []

def all_functions():
    while True:
        print("---Личные заметки---")
        print("1 - Создать заметку")
        print("2 - Показать все заметки")
        print("3 - Удалить заметку")
        print("4 - Отметить заметку выполненной")
        print("5 - Выход")

        choice = input("Выберите действие 1-4")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            done_note()
        elif choice == "5":
            break
        else:
            print("Неверный ввод")

if __name__ == "__all_functions__":
    def add_note():
        text = input("Введите текст заметки:")
        notes.append({"text": text, "done": False})
        print("Заметка добавлена!")
    def view_note():
        if not notes:
            print("Список пуст ^^")
        for i, note in enumerate(notes):
            status = "[X]" if note["done"] else "[ ]"
            print(f"{i}. {status} {note['text']}")
    def delete_note():
        idx = int(input("Введите номер заметки, которую хотите удалить: "))
        if 0 <= idx <= len(notes):
            notes.pop(idx)
        print("Заметка удалена!")
    def done_note():
        idx = int(input("Введите номер заметки, которую хотите отметить выполненной: "))
        if 0 <= idx <= len(notes):
            notes[idx]["done"] = True
        print("Выполнено!")
        all_functions()