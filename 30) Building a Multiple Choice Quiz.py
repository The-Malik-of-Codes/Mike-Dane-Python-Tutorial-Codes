from question import Question

question_prompts = [
    "What is Islam?\n(a) Peace\n(b) Prayer\n(c) Hope\n\n",
    "What color are apples?\n(a) Red/Green\n(b)Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow\n\n",
    "What color are mango?\n(a) Red\n(b) Green\n(c)Yellow\n\n",
]

Questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(question_prompts)) + " correct.")


run_test(Questions)

from question import Question

print("")
question_prompts = [
    "What is Islam?\n(a) Peace\n(b) Prayer\n(c) Hope\n\n",
    "What color are apples?\n(a) Red/Green\n(b)Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow\n\n",
    "What color are mango?\n(a) Red\n(b) Green\n(c)Yellow\n\n",
    "What is Ahmad doing right now?\n(a) Sleeping\n(b) Coding\n(c) Eating\n\n",
]

Questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(question_prompts)) + " correct.")


run_test(Questions)
