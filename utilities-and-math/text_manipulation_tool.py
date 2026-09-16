def display_menu():
    print("1. Find...")
    print("2. Replace all...")
    print("3. Replace one by one...")
    print("0. Quit...")
    print("Enter your choice [0-3]: ", end="")


def get_number(lower_limit, upper_limit):
    number = input()
    while not(number.isdigit()) and int(number) >= lower_limit and int(number) <= upper_limit:
        number = input("Incorrect data entry, please try again: ")
    return int(number)


def get_yes_no(msg):
    print(msg, end="")
    answer = input()
    while answer not in "yYnN":
        answer = input("Incorrect data entry, try again:")
    return answer.upper()


def find(text, search_text):
    occurrence_count = 0
    search_text_length = len(search_text)
    print("No location")
    print("-----------")
    location_index = text.find(search_text)
    while location_index != -1:
        occurrence_count += 1
        print(f"{occurrence_count:2} {location_index+1:4}")
        location_index = text.find(search_text, location_index + search_text_length)


def replace_all(text, search_text, new_text):
    return text.replace(search_text, new_text)


def replace_by_one_by(text, search_text, new_text):
    search_text_length = len(search_text)
    search_text_start_index = 0
    resulting_text = ""
    location_index = text.find(search_text, search_text_start_index)
    while location_index != -1:
        ans = get_yes_no(f"Do you want to replace the text in location {location_index+1} (y/Y/N/n)")
        resulting_text = resulting_text + text[search_text_start_index: location_index]
        if ans == "Y":
            resulting_text = resulting_text + new_text
        else:
            resulting_text = resulting_text + search_text
        search_text_start_index = location_index + search_text_length
        location_index = text.find(search_text, search_text_start_index)
    resulting_text = resulting_text + text[search_text_start_index:]
    return resulting_text


def main():
    text = input("Enter a piece of text:")
    out = "N"
    while out.upper() == "N":
        display_menu()
        menu_choice = get_number(0, 3)
        if menu_choice == 1:
            search_text = input("Enter the text you want to search: ")
            find(text, search_text)
        elif menu_choice == 2:
            search_text = input("Enter the text you want to search: ")
            new_text = input("Enter the text you want to replace with: ")
            a = replace_all(text, search_text, new_text)
            print(a)
        elif menu_choice == 3:
            search_text = input("Enter the text you want to search: ")
            new_text = input("Enter the text you want to replace with: ")
            a = replace_by_one_by(text, search_text, new_text)
            print(a)
        else:
            out = get_yes_no("Are you sure to quit: ")


if __name__ == '__main__':
    main()