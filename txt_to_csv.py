import os
import csv

name = "pytanka z X"
folder = "./db/"
files = os.listdir(folder)
# images = os.listdir('./img') -- zdjecia musisz sb sam dodac, bo cos nie dziala

def write_to_csv(files):
    for idx, file in enumerate(files):
        with open(folder + file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            lines = list(map(lambda x: x.replace(',', ' '), lines))

            answer = lines[0][2:-1]
            question = lines[1]
            answers = lines[2:]

            answers_str = ""
            for i in range(len(answers)):
                answers_str += answers[i]

            correct_answers = ""
            for i in range(len(answer)):
                if answer[i] == '1':
                    correct_answers += (answers[i].strip()) + '\n'

            with open(name + '.csv', 'a', newline='', encoding='utf-8') as f:
                data = [question + answers_str, correct_answers]
                csv.writer(f, quoting=csv.QUOTE_NONNUMERIC).writerow(data)

write_to_csv(files)
