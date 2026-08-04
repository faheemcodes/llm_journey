for n in range(1, 30):
    if n % 3 == 0 and n % 5 == 0:
        print("LLM Output")
    elif n % 3 == 0:
        print("Prompt")
    elif n % 5 == 0:
        print("Completion")
    else:
        print(n)
        