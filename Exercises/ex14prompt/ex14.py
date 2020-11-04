from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hola, {user_name}, I'm your leader {script}.")
print(f"Do you like me {user_name}?")
like = input(prompt)

print(f"Where do you live {user_name}?")
live = input(prompt)

print("""
You said {like} about liking me.
You live in {live}. VERY WELL!! VENGABOYS....
""")