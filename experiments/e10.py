def greet(message):
    new_message = message.capitalize()
    print("hei hei")
    return new_message

user_entry = input("what greeting do you want? ")
greeting = greet(user_entry)

print(greeting)