def square_sum(numbers):
    total = 0
    for number in numbers:
        num = int(number)
        if num >= 0:
            total += num ** 2
    return total

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()

    if not data or len(data) < 2:
        print("Invalid input")
        return

    caseNo = int(data[0])
    result = []
    idx = 1

    for _ in range(caseNo):
        if idx + 1 >= len(data):
            print("Invalid input")
            return

        integerNo = int(data[idx])
        numbers = data[idx + 1].split()

        if len(numbers) != integerNo:
            print("Invalid input")
            return

        result.append(square_sum(numbers))
        idx += 2

    # Print all results
    for res in result:
        print(res)

if __name__ == "__main__":
    main()

