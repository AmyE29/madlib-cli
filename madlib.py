import re

a = """
  ###############################################
  #                                             #
  #         Welcome to my Madlib game!!         #
  #    Please answer the following questions    #
  # and you will be rewarded with a funny story #
  #                                             #
  ###############################################
"""

print(a)

def create_madlib():
    answers= []
    text = ''
    words = []
    with open('madlib.txt', 'r') as file:
        for line in file:
            text += line
            words += re.findall(r'{([^}]*)}', line)
    if answers == []:
        for word in words:
            word_prompt = re.sub(r"[{}]", '', word)
            answers.append(input('Please enter ' + word_prompt + '\n: '))
    for word in answers:
        text = re.sub(r'{([^}]*)}', word, text, 1)
    with open('new_madlibs.txt', 'w') as file:
        file.write(text)
    print(text)
    return answers

if __name__ == '__main__':
    create_madlib()
