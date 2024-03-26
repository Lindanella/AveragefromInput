#LindaPimpinella
#CS175
def main():
    try:
        total, count = process_file('numbers.txt')
        if count > 0:
            average = total / count
            print(f"Average: {average:5.1f}")
        else:
            print("No numbers found in the input file.")
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' cannot be opened or was not found.")
    except ValueError as e:
        print(f"Error: {e} Please ensure all values in 'numbers.txt' are numbers.")

def process_file(filename):
    total = 0
    count = 0
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                number = float(line.strip())
                count += 1
                total += number
                print(f"I read in {count} number(s). Current number is: {number:8.2f} Total is: {total:8.2f}")
            except ValueError:
                raise ValueError(f"Invalid value found on line {line_number}: '{line.strip()}' is not a valid number.")
    return total, count

if __name__ == "__main__":
    main()
