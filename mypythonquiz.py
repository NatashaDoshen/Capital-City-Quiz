import sys


def open_file(file_name, mode):
    try:
        file = open('capitalistic.txt', 'r')
    except IOError:
        print('unable to open file', file_name,"\n")
        sys.exit()
    else:
        return file


def next_line(file):
    line = file.readline()
    return line


def next_block(file):

    question = next_line(file)
    answer =[]

    answer.append(next_line(file))
    correct = next_line(file)  # Get the correct answer number

    if correct:
        correct = correct[0]
    return question, answer, correct



def main():
    print('Welcome to the quiz.')
    name = input("What is your name ? ")
    print("Hi,", name)
    answer = input('Would you like to play guessing the capital cities quiz? Y/N ').upper()

    if answer == "Y":
        print('yay. lets get started')
    else:
        print('sorry to hear that. goodbye')
        exit()

    quiz_file = open_file('capitalistic.txt', 'r')
    score = 0
    question, answer, correct = next_block(quiz_file)
    number_question = 0
    while question:
        number_question += 1
        print(question)
        answer = input("Choose your answer? ").upper()

        if answer == correct:
            print('correct answer', end='')
            score += 1
        else:

            print('incorrect. the correct answer is',correct, "\b")

            # get next block

        question, answer, correct = next_block(quiz_file)

    quiz_file.close()
    print('the score is',score)

main()
