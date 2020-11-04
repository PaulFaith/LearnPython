from sys import argv

script, filename = argv

print(f"Ereasing file... {filename}.")
print("Press CTRL+C (^C) to stop ereasing.")
print("If you are sure to erease press RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Enter 3 lines pleas.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("Writing these to the file...")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Closing file..-.-.-.-.")
target.close()
