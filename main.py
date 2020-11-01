def arithmetic_arranger(problems, disp=False):
    l1 = ''
    l2 = ''
    l3 = ''
    l4 = ''
    if len(problems) > 5:  #check number of problems
        return 'Error: Too many problems.'

    for i in problems:
        a = i.split()
        num1 = a[0]
        oper = a[1]
        num2 = a[2]
        if (len(num1) > 4 or len(num2) > 4):  #check length of the numbers
            return "Error: Numbers cannot be more than four digits."

        if not num1.isnumeric() or not num2.isnumeric(
        ):  # check if the input are digits
            return "Error: Numbers must only contain digits."

        if (oper == '+' or oper == '-'):  #check if operators are + or -
            if oper == "+":
                sums = str(int(num1) + int(num2))
            else:
                sums = str(int(num1) - int(num2))

            length = max(len(num1), len(num2)) + 2  # set length of line
            top = str(num1).rjust(length)
            bot = oper + str(num2).rjust(length - 1)
            lin = ''
            res = str(sums).rjust(length)
            for s in range(length):
                lin += '-'
            if i != problems[-1]:
                l1 += top + 4 * ' '
                l2 += bot + 4 * ' '
                l3 += lin + 4 * ' '
                l4 += res + 4 * ' '
            else:
                l1 += top
                l2 += bot
                l3 += lin
                l4 += res
        else:
            return "Error: Operator must be '+' or '-'."
        l1.rstrip()
        l2.rstrip()
        l3.rstrip()
        l4.rstrip()
        if disp:

            arranged_problems = l1 + '\n' + l2 + '\n' + l3 + '\n' + l4
        else:
            arranged_problems = l1 + '\n' + l2 + '\n' + l3
    return arranged_problems

a = 1
a = input("How many operations: ")
print('')
b = int(a)

y = []
print('For example: 3 + 698 \n ')
for i in range(b):
    x = input(str(i+1) + ': ')
    y.append(x)
print('')
z = arithmetic_arranger(y, True)
print(z)



