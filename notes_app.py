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
        print("Конфликт")
    def view_note(): pass
    def delete_note(): pass
    def done_note(): pass
    all_functions()