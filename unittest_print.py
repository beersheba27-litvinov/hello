__failed_count: int = 0
__passed_count: int = 0
RED = "\33[31m"
GREEN = "\33[32m"
RESET = "\33[m"


def print_test(description: str, expected: object, actual: object) -> None:
    global __passed_count, __failed_count

    if expected == actual:
        __passed_count += 1
        color = GREEN
    else:
        __failed_count += 1
        color = RED
    print(f"{color}{description}; expected is {expected}; actual is {actual}{RESET}")


def print_results():
    print(
        f"    Total:  {__failed_count + __passed_count}\n\
    {GREEN}Passed: {__passed_count}\n\
    {RED}Failed: {__failed_count}{RESET}"
    )
