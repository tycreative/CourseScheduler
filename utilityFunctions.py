# Helper function to convert value to an integer
def toInt(value):
    try:
        return int(value)
    except ValueError:
        return 0



# Helper function to format list for display
def joinList(values, conjunction):
    if values == []:
        return ""

    if len(values) == 1:
        return str(values[0])

    if len(values) == 2:
        return f"{values[0]} {conjunction} {values[1]}"

    output = ""
    for i in range(len(values) - 1):
        output += str(values[i]) + ", "
    return f"{output}{conjunction} {values[-1]}"



# Helper function to get yes/no input from a user
def getOption(prompt, a, b):
    while True:
        print("\n" + prompt)
        option = input()

        if option.lower() == a.lower():
            return True
        elif option.lower() == b.lower():
            return False
        print(f"Please enter either '{a}' or '{b}'.")



# Helper function to get number in range from user
def getNumber(prompt, minimum, maximum):
    while True:
        print("\n" + prompt)
        value = toInt(input())

        if value == 0:
            print("Please enter in a number.")
        elif value > minimum and value < maximum:
            return value
        else:
            print(f"Please enter a number between {minimum} and {maximum}.")



# Helper function to get filename from a user
def getFile(prompt, formats, blank = False):
    while True:
        try:
            print("\n" + prompt)
            filename = input()

            # Check if input is blank and blanks are allowed
            if blank and filename == "":
                return filename

            # Check if input has needed format
            elif "." not in filename:
                print("Specified file missing associated file format.\nPlease check your spelling and try again.")

            # Check if input has appropriate format
            elif "." + filename.split(".")[1].lower() not in formats:
                print("Incompatible file type, allowed formats are: " + joinList(formats, "or") + "\nPlease try again with appropriate file type.")

            # Try to open provided file
            else:
                with open(filename, "r") as file:
                    file.close()
                    return filename

        except FileNotFoundError:
            print("Unable to find specified file.\nPlease check your spelling and try again.")
        except IOError:
            print("Unable to open specified file.\nPlease close other programs and try again.")
        except Exception:
            print("Unexpected error occurred opening specified file.\nPlease check validity of provided file and try again.")