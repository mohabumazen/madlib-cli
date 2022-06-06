import re

print('''      ******* Welcome to Madlib Game *********
      you'll be asked some question , please provide some answers and we will return your inputs in some context ;)
      ******** Stay Tuned! ********''')


def read_template(path):
    with open(path, 'r') as file:
        file_content = file.read().strip()
        print(file_content)
        return file_content


def parse_template(content, isInput=True):
    pattern = r"{(.*?)}"
    useful_parts = re.findall(pattern, content)
    print(f'please answer these {len(useful_parts)} questions to give you your paragraph and create it into a file ')
    i = 1
    all_user_input = []
    if (isInput == True):
        for x in useful_parts:
            input_from_user = input(f"Q{i}: please suggest {x} \n Answer: ")
            all_user_input.append(input_from_user)
            i += 1
        output = [all_user_input, useful_parts]
        return output
    else:
        return useful_parts


def merge(input_collected, placeholders_in_content, content):
    i = 0
    for x in input_collected:
        content = content.replace(placeholders_in_content[i], x, 1)
        i += 1
    content = content.replace("{", "")
    final_content = content.replace("}", "")

    message_file = "assets/message.txt".strip()
    with open(message_file, 'w') as message:
        message.write(final_content)

    print("*******Enjoy your paragraph********* \n")
    print(final_content)
    print("\n *******")

    return final_content


if __name__ == "__main__":
    content = read_template('assets/template.txt')
    items = parse_template(content)
    to_be_replaced_with = items[0]
    to_be_replaced = items[1]
    merge(to_be_replaced_with, to_be_replaced, content)
    # final_result = marge(parse_template(content),content)



