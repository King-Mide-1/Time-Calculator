import re


def arithmetic_arranger(problems, solve = False):
    if (len(problems) > 5):
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    lines = ""
    total = ""
    string = ""

    for problem in problems:
        if (re.search("[^\s0-9.+-]", problem)):
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        if (operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = ""
        result = str(sum).rjust(length)
        for i in range(length):
            line += "-"

        if problem != problems[-1]:
            first_line += top + "    "
            second_line += bottom + "    "
            lines += line + "    "
            total += result + "    "
        else:
            first_line += top
            second_line += bottom
            lines += line
            total += result
    if solve:
        string = first_line + "\n" + second_line + "\n" + lines + "\n" + total
    else:
        string = first_line + "\n" + second_line + "\n" + lines
    return string
