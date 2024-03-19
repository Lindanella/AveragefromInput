#LindaPimpinella
#CsS175
def main():
    total = 0
    count = 0

    with open('numbers.txt') as file:
        for line_number, line in enumerate(file, start=1):
            number= float(line.strip())
            count += 1
            total += number
            print(f"I read in   {count} number(s) Current number is: {number:8.2f}Total is: {total:8.2f}")
        
    if count > 0:
        average = total / count
        print(f"Average: {average:5.1f}")
    else:
        print("No numbers found in the input file.")

if __name__ == "__main__":
    main()
