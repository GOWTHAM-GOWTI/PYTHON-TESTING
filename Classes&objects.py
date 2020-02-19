
from question import question

qus_prompt_var = [
    "what's your name \n (a)gowham \n (b) john \n (c) mike \n \n"
]

qus_var = [
    question(qus_prompt_var[0] , "a" )

]

def run_test(qus_var):
    score = 0
    for question in qus_var:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(qus_var)) + " correct ")


run_test(qus_var)