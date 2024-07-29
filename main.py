from dotenv import load_dotenv
from assistant import Assistant


def display_menu():
    print("===========================")
    print("[1] Who is Assistant")
    print("[2] Change Assistant Name")
    print("[3] Add Schedule")
    print("[4] Show Schedule")
    print("[5] Random Joke")
    print("[6] Send Email")
    print("[7] Exit")
    print("===========================")

def main():
    load_dotenv()
    assistant = Assistant()

    list = [1, 2, 3, 4]
    x = f"Menarik {list}"


    name = input("Set assistant name: ")
    assistant.setName(name)

    while True:
        display_menu()

        print(x)

        choice = input("Select a menu... (example: 1)")

        if choice == '1':
            # [1] Who is Assistant
            assistant.printName()
        elif choice == '2':
            # [2] Change Assistant Name
            name = input("Set assistant name: ")
            if name:
                assistant.setName(name)
            else:
                print("Name cannot be null")
        elif choice == '3':
            # [3] Add Schedule
            schedule = input("Add a schedule: ")
            if schedule:
                assistant.createSchedule(schedule)
            else:
                print("Schedule cannot be null")
        elif choice == '4':
            # [4] Show Schedule
            assistant.printSchedule()
        elif choice == '5':
            # [5] Random Joke
            assistant.printRandomJoke()
        elif choice == '6':
            # [6] Send Email
            receiver = input("Set receiver email: ")
            title = input("Set title: ")
            body = input("Set body: ")

            assistant.sendEmail(receiver, title, body)
        elif choice == '7':
            # [7] Exit
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()