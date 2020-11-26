def add(x: float, y: float):
    print(f"{x} {y}")
    return x + y

def sub(x: float, y: float):
    return x - y

def mul(x: float, y: float):
    return x * y

def div(x: float, y: float):
    return x / y

def print_out_text(sum):
    if sum < 50:
        print("less than fifty")
    elif sum == 50:
        print("Fifty")
    elif 50 < sum < 100:
        print("Almost a hundred")
    elif sum == 100:
        print("Spot on")
    elif sum > 100:
        print("Missed the spot!")
    else:
        print("negative number")