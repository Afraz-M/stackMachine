class StackMachine:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop_external(self):
        if not self.stack:
            return "Error: Stack underflow"
        return f"POPPED VALUE: {self.stack.pop()}"

    def pop(self):
        if not self.stack:
            print("Error: Stack underflow")
        return self.stack.pop()

    def add(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for addition"
        else:
            operand2 = self.pop()
            operand1 = self.pop()
            result = operand1 + operand2
            self.push(result)
            return result

    def subtract(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for subtraction"
        else:
            operand2 = self.pop()
            operand1 = self.pop()
            result = operand1 - operand2
            self.push(result)
            return result

    def multiply(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for multiplication"
        else:
            operand2 = self.pop()
            operand1 = self.pop()
            result = operand1 * operand2
            self.push(result)
            return result

    def divide(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for division"
        else:
            operand2 = self.pop()
            operand1 = self.pop()
            if operand2 == 0:
                return "Error: Division by zero"
            else:
                result = operand1 / operand2
                self.push(result)
                return result

    def modulus(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for division"
        else:
            operand2 = self.pop()
            operand1 = self.pop()
            if operand2 == 0:
                return "Error: Division by zero"
            else:
                result = operand1 % operand2
                self.push(result)
                return result
    
    def evaluate_push_command(self, command):
        words = command.split()
        if len(words) > 0 and words[0].strip().upper() == "PUSH":
            if len(words) > 1:
                value_str = ' '.join(words[1:])
                try:
                    value = float(value_str)
                    return value
                except ValueError:
                    print("Error: Invalid value after 'PUSH'")
                    return "err"
            else:
                print("Error: Missing value after 'PUSH'")   
                return "err"
        return None

def main():
    stack_machine = StackMachine()

    choice = input("Do you want a Menu for ISA? ")

    if choice.lower() == "y" or choice.lower() == "yes": 

        while True:
            print("Options:")
            print("1. Push")
            print("2. Pop")
            print("3. Add")
            print("4. Subtract")
            print("5. Multiply")
            print("6. Divide")
            print("7. Modulus")
            print("8. Quit")

            choice = input("Enter your choice: ")

            if choice == '8':
                break

            if choice == '1':
                value = float(input("Enter a value to push onto the stack: "))
                stack_machine.push(value)
            elif choice == '2':
                popped_value = stack_machine.pop()
                if popped_value is not None:
                    print(f"Popped value: {popped_value}")
            elif choice == '3':
                stack_machine.add()
            elif choice == '4':
                stack_machine.subtract()
            elif choice == '5':
                stack_machine.multiply()
            elif choice == '6':
                stack_machine.divide()
            elif choice == '7':
                stack_machine.modulus()
        
        print("Goodbye!")
    
    else:

        while True:
            choice = input("Enter the Operation ")
            push_command = stack_machine.evaluate_push_command(choice)
            if  push_command:
                if push_command == "err":
                    continue
                value = int(choice[-1])
                stack_machine.push(value)
            elif choice.lower() == 'pop':
                popped_value = stack_machine.pop()
                if popped_value is not None:
                    print(f"Popped value: {popped_value}")
            elif choice.lower() == 'add':
                stack_machine.add()
            elif choice.lower() == 'sub':
                stack_machine.subtract()
            elif choice.lower() == 'mul':
                stack_machine.multiply()
            elif choice.lower() == 'div':
                stack_machine.divide()
            elif choice.lower() == 'mod':
                stack_machine.divide()
            elif choice.lower() == 'exit':
                break
            else:
                print("Invalid input")
        
        print("Goodbye!")


if __name__ == "__main__":
    main()
