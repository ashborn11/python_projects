#questions for the quiz
quiz = {
    "question1": {
        "question": "Who is the first person to recieve Arjuna Award from Kerala?",
        "answer": "T C Yohannan"
    },
    "question2": {
        "question": "How many districts of Kerala have coastline?",
        "answer": "9"
    },
    "question3": {
        "question": "Who is considered as the father of malayalam cinema?",
        "answer": "J C Daniel"
    },
    "question4": {
        "question": "Which district have longest coastline?",
        "answer": "Kannur"
    },
    "question5": {
        "question": "Who called Travancore a 'lunatic asylum'?",
        "answer": "Swami Vivekananda"
    },
    "question6": {
        "question": "Which place is known as the Cultural Capital of Kerala? ",
        "answer": "Thrissur"
    },
    "question7": {
        "question": "Asia's first arch dam that was constructed across the Kuravan and Kurathi hills?",
        "answer": "Idukki Dam"
    },
    "question8": {
        "question": "Which place is known as the 'Gateway of Highrange'?",
        "answer": "Kothamangalam"
    },
    "question9": {
        "question": "In which district of Kerala the Silent Valley National Park is located?",
        "answer": "Palakkad"
    },
    "question10": {
        "question": "Who is the founder of the University of Kerala?",
        "answer": "Balarama Varma"
    }
}

#initial score assigned 0
score = 0

#checking if answered correctly and finding total score
for key,value in quiz.items():
    print(value['question'])
    answer = input('Answer: ')

    if answer.lower() == value['answer'].lower():
        print("Correct answer")
        score = score + 1
        print("Your score is "+ str(score))
        print("")
        print("")
    else:
        print("Incorrect answer")
        print("The answer is " + value["answer"])
        print("Your score is "+ str(score))
        print("")
        print("")

print("You answered " + str(score) + " of 10 correctly")
print("Your percentage is " + str(int(score/10 * 100)) + "%")


