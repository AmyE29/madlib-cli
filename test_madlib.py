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
    madlib_keywords = []
    with open('madlib.txt', 'r') as rf:
        with open('keywords.txt', 'w') as wf:
            for line in rf:
                madlib_keywords= re.findall('{([^}]*)}', line)
                if madlib_keywords!= ['']:
                    for keyword in madlib_keywords:
                        wf.write(keyword + '\n')


def get_user_words():
    """Function that asks for the user to enter silly words.
    """
    with open('keywords.txt', 'r') as rf:
        with open('new_template.txt', 'w') as wf:
            for line in rf:
                user_word = input('Enter %s : ' % line)
                re.sub('{([^}]*)}', user_word, str)
                wf.write(user_word)

if __name__ == "__main__":
    create_madlib()
    get_user_words()
