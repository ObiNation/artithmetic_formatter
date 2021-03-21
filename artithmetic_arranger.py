def arithmetic_arranger(problems, statprint=False):
    # check problem list
    first = ''
    second = ''
    sumx = ''
    lines = ''

    if len(problems) >= 6:
        return 'Error: Too many problems.'
    for x in problems:
        temp = x.split()
        firstNum = temp[0]
        secondNum = temp[2]
        operands = temp[1]
        # check if numbers have less than 4 digits
        if (len(firstNum) > 4 or len(secondNum) > 4):
            return "Error: Numbers cannot be more than four digits."

        # check if numbers are numeric
        if not firstNum.isnumeric() or not secondNum.isnumeric():
            return "Error: Numbers must only contain digits."

        if (operands == '+' or operands == '-'):
            if operands == "+":
                sums = str(int(firstNum) + int(secondNum))
            else:
                sums = str(int(firstNum) - int(secondNum))
            length = max(len(firstNum), len(secondNum)) + 2
            top = str(firstNum).rjust(length)
            bottom = operands + str(secondNum).rjust(length - 1)
            line = ''
            size = str(sums).rjust(length)
            for s in range(length):
                line += '-'
            # add to the overall string
            if x != problems[-1]:
              first += top + '    '
              second += bottom + '    '
              lines += line + '    '
              sumx += size + '    '
            else:
              first += top
              second += bottom
              lines += line
              sumx += size
        else:
            return "Error: Operator must be '+' or '-'."
    if statprint:
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems
