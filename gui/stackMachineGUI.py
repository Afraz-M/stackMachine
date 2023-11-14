import tkinter as tk
from src.stackMachine import StackMachine

class StackMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ISA STACK MACHINE SIMULATOR")


        window_width = 400  
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")


        heading_frame = tk.LabelFrame(root, text="", font=("Arial", 14), border=0)
        heading_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2) 

        heading_label = tk.Label(heading_frame, text="ISA STACK MACHINE SIMULATOR", font=("Arial", 16, "bold"))
        heading_label.grid(row=0, column=0, padx=10, pady=10)

        
        isa_frame = tk.LabelFrame(root, text="ISA", font=("Arial", 14))
        isa_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew", ipady=20, columnspan=2) 
       
        instructions = ["PUSH\tx\t: PUSH ONTO STACK",
                        "POP  \t\t: POP FROM STACK",
                        "ADD  \t\t: ADD TOP TWO OPERANDS",
                        "SUB  \t\t: SUB TOP TWO OPERANDS",
                        "MUL  \t\t: MUL TOP TWO OPERANDS",
                        "DIV  \t\t: DIV TOP TWO OPERANDS",
                        "MOD  \t\t: MOD TOP TWO OPERANDS",
                        "OR   \t\t: BITWISE OR",
                        "AND  \t\t: BITWISE AND",
                        "XOR  \t\t: BITWISE XOR",
                        "NOT  \t\t: BITWISE NOT",
                        "LSL  \t\t: ARITHMETIC LEFT SHIFT",
                        "ASR  \t\t: ARITHMETIC RIGHT SHIFT",
                        "EXIT"]
        
        for i, instruction in enumerate(instructions):
            label = tk.Label(isa_frame, text=instruction, font=("Arial", 12))
            label.grid(row=i, column=0, sticky="w")

        
        input_frame = tk.LabelFrame(root, text="Input", font=("Arial", 14))
        input_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew", ipady=20, columnspan=2)  

        self.input_entry = tk.Entry(input_frame, width=40)  
        self.input_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.submit_button = tk.Button(input_frame, text="Submit", command=self.process_input)
        self.submit_button.grid(row=0, column=1, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


        self.stack_machine = StackMachine()

    def process_input(self):
        command = self.input_entry.get()
        push_command = self.stack_machine.evaluate_push_command(command)
        if  push_command:
            if push_command == "err":
                self.update_result_label("ERROR: PUSH value is expected")
                return
            value = int(push_command)
            self.stack_machine.push(value)
            self.update_result_label(f"PUSHED VALUE: {value}")
        elif command.lower() == 'pop':
            popped_value = self.stack_machine.pop_external()
            self.update_result_label(f"{popped_value}")
        elif command.lower() == 'add':
            self.update_result_label(self.stack_machine.add())
        elif command.lower() == 'sub':
            self.update_result_label(self.stack_machine.subtract())
        elif command.lower() == 'mul':
            self.update_result_label(self.stack_machine.multiply())
        elif command.lower() == 'div':
            self.update_result_label(self.stack_machine.divide())
        elif command.lower() == 'mod':
            self.update_result_label(self.stack_machine.modulus())
        elif command.lower() == 'or':
            self.update_result_label(self.stack_machine.bitwiseOr())
        elif command.lower() == 'and':
            self.update_result_label(self.stack_machine.bitwiseAnd())
        elif command.lower() == 'xor':
            self.update_result_label(self.stack_machine.bitwiseXor())
        elif command.lower() == 'not':
            self.update_result_label(self.stack_machine.bitwiseNot())
        elif command.lower() == 'lsl':
            self.update_result_label(self.stack_machine.bitwiseLS())
        elif command.lower() == 'asl':
            self.update_result_label(self.stack_machine.bitwiseRS())
        elif command.lower() == 'exit':
            self.stack_machine = []
            self.root.destroy()
        else:
            self.update_result_label("Invalid input")

    def update_result_label(self, text):
        self.result_label.config(text=text)


def main():
    root = tk.Tk()
    app = StackMachineApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
