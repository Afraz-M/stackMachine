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
   
    def bitwiseOr(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for logical OR operation"
        else:
            operand2 = self.pop()
            operand1 = self.pop()

            result = operand1|operand2
            self.push(result)
            return result
    
    def bitwiseAnd(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for logical AND operation"
        else:
            operand2 = self.pop()
            operand1 = self.pop()

            result = operand1&operand2
            self.push(result)
            return result

    def bitwiseXor(self):
        if len(self.stack) < 2:
            return "Error: Insufficient operands for logical AND operation"
        else:
            operand2 = self.pop()
            operand1 = self.pop()

            result = operand1^operand2
            self.push(result)
            return result
    
    def bitwiseNot(self):
        if len(self.stack) < 1:
            return "Error: Insufficient operands for logical NOT operation"
        else:
            operand1 = self.pop()
           
            result = ~operand1
            self.push(result)
            return result

    def bitwiseRS(self):
        if len(self.stack) < 1:
            return "Error: Insufficient operands for BITWISE RIGHT SHIFT operation"
        else:
            operand1 = self.pop()
           
            result = operand1 >> 1
            self.push(result)
            return result

    def bitwiseLS(self):
        if len(self.stack) < 1:
            return "Error: Insufficient operands for BITWISE LEFT SHIFT operation"
        else:
            operand1 = self.pop()
           
            result = operand1 << 1
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
