program = list(input())  # Read Brainfuck code
print(program)
tape = [0] * 2**16  # Initialize tape
pointer = 0  # Data pointer starts at 0
ip = 0  # Instruction pointer
bracket_stack = []  # Stack to track loops

while ip < len(program):
    match program[ip]:

        case '+':  # Increment the value in the current memory cell
            tape[pointer] += 1
            if tape[pointer] > 255:  # Wrap around to 0 if > 255
                tape[pointer] = 0

        case '-':  # Decrement the value in the current memory cell
            tape[pointer] -= 1
            if tape[pointer] < 0:  # Wrap around to 255 if < 0
                tape[pointer] = 255

        case '>':  # Move the pointer to the right
            pointer += 1
            if pointer >= len(tape):  # Ensure we don't go out of bounds
                pointer = 0

        case '<':  # Move the pointer to the left
            pointer -= 1
            if pointer < 0:  # Ensure we don't go out of bounds
                pointer = len(tape) - 1

        case '.':  # Output the character at the current memory cell
            print(chr(tape[pointer]), end='')

        case ',':  # Take one character input and store its ASCII value
            tape[pointer] = ord(input()[0])

        case '[':  # Start a loop: jump to matching ']' if current cell is 0
            if tape[pointer] == 0:
                open_brackets = 1
                while open_brackets > 0:
                    ip += 1
                    if program[ip] == '[':
                        open_brackets += 1
                    elif program[ip] == ']':
                        open_brackets -= 1
            else:
                bracket_stack.append(ip)  # Store the current instruction pointer

        case ']':  # End of loop: jump back to matching '[' if current cell is non-zero
            if tape[pointer] != 0:
                ip = bracket_stack[-1]  # Jump back to the matching '['
            else:
                bracket_stack.pop()  # Exit loop if current cell is 0

    ip += 1  # Move to the next instruction
