numbers = {
    0: ["zero", "zero", "ten"],
    1: ["one", "", "eleven"],
    2: ["two", "twenty", "twelve"],
    3: ["three", "thirty", "thirteen"],
    4: ["four", "forty", "fourteen"],
    5: ["five", "fifty", "fifteen"],
    6: ["six", "sixty", "sixteen"],
    7: ["seven", "seventy", "seventeen"],
    8: ["eight", "eighty", "eighteen"],
    9: ["nine", "ninety", "nineteen"]
}

num1 = 9
num2 = 99
num3 = 999


def turn_number_into_string(number):
    number = str(number)
    if len(number) == 1:
        number = "00" + number
    elif len(number) == 2:
        number = "0" + number

    return number


def main(num):
    result = []
    count = 0
    ten = False

    number_as_string = turn_number_into_string(num)

    for number in number_as_string:
        if count == 0:
            if number != "0":
                result.append(numbers.get(int(number))[count] + " hundred and ")
            else:
                result.append("")
        elif count == 1:
            if number == "1":
                ten = True
                count += 1
                result.append("")
                continue
            if number != "0":
                result.append(numbers.get(int(number))[count])
            else:
                result.append("")
        elif count == 2:
            if ten:
                result.append(numbers.get(int(number))[2])
            else:
                if number != "0":
                    result.append(numbers.get(int(number))[0])
                else:
                    result.append("")

        count += 1

    return result


result = []
for x in range(1000):
    result.append(main(x))

new_result = []

for i in result:
    if i[1] == "" and i[2] == "":
        i[0] = i[0].replace(" hundred and ", " hundred")

    i[0] = i[0].replace(" ", "")
    new_result.append(i[0] + i[1] + i[2])

string = ""
for i in new_result:
    string += i

print(len(string))
