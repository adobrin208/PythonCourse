while True:
    #obtinem date de la utilizator si eliminam spatiile
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            #file = open('todo.txt', 'r')
            #todos = file.readlines()
            #file.close()

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            #file = open('todo.txt', 'w')
            #file.writelines(todos)
            #file.close()

            with  open('todo.txt', 'w') as file:
                file.writelines(todos)


        case 'show':
            #file = open('todo.txt', 'r')
            #todos= file.readlines()
            #file.close()

            with open('todo.txt', 'r') as file:
             todos= file.readlines()

            #new_todos = []
            #for item in todos:
              #  new_item = item.strip('\n')
              #  new_todos.append(new_item)
            #print(todos)

            new_todos = [item.strip('\n') for item in todos]



            for index, item in enumerate(new_todos):
                row = f"{index+1}-{item.capitalize()}"
                print(row)
        case 'edit':
            number = int(input("number of the todo to edit: "))
            number = number-1

            with open('todo.txt', 'r') as file:
                todos= file.readlines()

            print('Here is todos existing', todos)

            new_todo = input("Enter new todo ")
            todos[number] = new_todo + '\n'

            print("Here is how it will be", todos)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            index= number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            todos.pop(number-1)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break

print("bye")
