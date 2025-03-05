def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_row = []
    bottom_row = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        num1, operand, num2 = parts

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if operand not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(num1), len(num2)) + 2

        top_row.append(num1.rjust(width))
        bottom_row.append(operand + " " + num2.rjust(width - 2))
        dashes.append('-' * width)

        if show_answers:
            result = str(eval(problem))
            results.append(result.rjust(width))

    arranged_problems = "    ".join(
        top_row) + '\n' + "    ".join(bottom_row) + '\n' + "    ".join(dashes) + '\n'

    if show_answers:
        arranged_problems += "    ".join(results)

    return arranged_problems


# print(
#     f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')

while True:
    problem = input("\nEnter a series of arithmetic problems (or 'q' to quit): ")
    if problem.lower() == 'q':
        break
    problems = problem.split(", ")
    print(arithmetic_arranger(problems, True))
    print()
