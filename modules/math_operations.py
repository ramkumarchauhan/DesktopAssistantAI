def solve_math_problem(problem):
    try:
        result = eval(problem)
        print(f"The result of {problem} is {result}.")
    except Exception as e:
        print(f"Error solving the math problem: {e}")
