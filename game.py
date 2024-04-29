class Quiz:
    def __init__(self,query,answer):
        self.query=query
        self.answer=answer
        
questions=[
    Quiz("What does the 'len()' function do?\n(a) Returns the length of a string\n(b) Returns the largest element of a list\n(c) Returns the smallest element of a list\n(d) Returns the sum of a list\n", "a"),
    Quiz("What is the output of 'print('Hello'[::-1])' in Python?\n(a) Hello\n(b) olleH\n(c) elloH\n(d) H\n", "b"),
    Quiz("Which keyword is used to define a function in Python?\n(a) func\n(b) def\n(c) define\n(d) function\n", "b"),
]


def run_quiz(questions):
    
    score=0
    print('\n----- WELCOME TO THE QUIZ -----\n')
    
    for question in questions:
        answer=input(question.query)
        if answer.lower()==question.answer:
            print('\nSahiii jawabbb !!!\n')
            score+=1
        else:
            print('\nGalat Jawab ..\n')
            
    if score==0:
        print(f'Your score is {score} . try harder next time !!\n')
    elif score==1:
        print(f'Your score is {score} . atleast you managed to score 1 !!\n')
    elif score==2:
        print(f'Your score is {score} . you are good at this game !!\n')
    elif score==3:
        print(f'Your score is {score} . you are unbeatable !!!!!\n')
        
run_quiz(questions)
