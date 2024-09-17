

def read_source_code():
    try:
        
        with open(r'C:\Users\Raja\Desktop\Semester 5\Compilation Technique\Class Exercise Week 1\Question1.py', 'r') as file:
            while True:
                char = file.read(1) 
                if not char:
                    break
                print(char, end='')  
    except Exception as e:
        print(f"An error occurred: {e}")

read_source_code()
