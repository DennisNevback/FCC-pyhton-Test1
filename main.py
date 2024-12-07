def arithmetic_arranger(problems, show_answers=False):
    #print(problems)
    if len(problems) > 5:
        #raise Exception('Error: Too many problems.')
        return 'Error: Too many problems.'
    else:
        top_numbers = ''
        #bottom numbers also include nominator
        bottom_numbers = ''
        spaces = ''
        lines = ''
        arithmetic_answer_full = ''

        #Check if the user wants an answer
        if show_answers==True:
            arithmetic_answer = arithmetic_calculator(problems)
            arithmetic_answer_full += arithmetic_answer
        
        #Run test to check operator
        if operator_test(problems) == False:
            return("Error: Operator must be '+' or '-'.")

        #Check if operands only contain digits
        if digit_test(problems) == False:
            return('Error: Numbers must only contain digits.')

        #Check if length excedes 4 digits
        if length_test(problems) == False:
            return('Error: Numbers cannot be more than four digits.')

        for problem in problems:
            problem_list = problem.rsplit()
            space = ' '
            line = '-'
            #find the longest length in order to align properly (max lenght 4)
            problem_longest_length = max(len(problem_list[0]), len(problem_list[2]))
            top_number = problem_list[0].rjust(problem_longest_length + 2 , ' ')
            nominator = problem_list[1]
            bottom_number = problem_list[2].rjust(problem_longest_length, ' ')
            #add new strings
            top_numbers += str(top_number) + '    '
            bottom_numbers += str(nominator) + ' ' + str(bottom_number) + '    '
            #spaces += space * (problem_longest_length + 2) + '    '
            lines += line * (problem_longest_length + 2) + '    '
        if show_answers == True:
            problems_finished = f'{top_numbers.rstrip()}\n{bottom_numbers.rstrip()}\n{lines.rstrip()}\n{arithmetic_answer_full.rstrip()}'
            return problems_finished
        else:
            problems_finished = f'{top_numbers.rstrip()}\n{bottom_numbers.rstrip()}\n{lines.rstrip()}'
            return problems_finished

def arithmetic_calculator(problems):
    answer_solved = ''
    for problem in problems:
            final_answer = str(eval(problem))
            answer_length = len(final_answer)
            problem_list = problem.rsplit()
            problem_longest_length = max(len(problem_list[0]), len(problem_list[2]))
            final_answer = final_answer.rjust(problem_longest_length + 2, ' ')
            answer_solved +=str(final_answer) + '    '
    return answer_solved

def operator_test(problems):
    for problem in problems:
        problem_list = problem.rsplit()
        if problem_list[1] == '+' or problem_list[1] == '-':
            return True
        else:
            #raise Exception ("Error: Operator must be '+' or '-'.")
            return False

def digit_test(problems):
    for problem in problems:
        problem_list = problem.rsplit()
        if problem_list[0].isdigit() and problem_list[2].isdigit():
            return True
        else:
            #raise Exception ('Error: Numbers must only contain digits.')
            return False

def length_test(problems):
    for problem in problems:
        problem_list = problem.rsplit()
        if len(problem_list[0]) <= 4 and len(problem_list[2]) <= 4:
            return True
        else:
            return False
            #raise Exception ('Error: Numbers cannot be more than four digits.')
    

#arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49"])
print(f'{arithmetic_arranger(["44 - 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"], True)}')