from sys import argv

script, input_file =argv

def print_all(f):
  print(f.read())

def rewind(f):
  f.seek(0)

def print_a_line(line_count, f):
  print(line_count, f.readline())

current_file = open(input_file)

print("PRINTING ALL FILE:\n")

print_all(current_file)

print("GOING BAAACK!!(REWIND)")
rewind(current_file)

print("Try just 3 lines:\n")
current_line = 1
print_a_line(current_line,current_file)
current_line += 10
print_a_line(current_line,current_file)
current_line = 3
print_a_line(current_line,current_file)
