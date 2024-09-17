import keyword

# Function to extract Python keywords from the code in Question1.py
def extract_keywords_from_code(file_path):
    keywords_in_code = set()  
    try:
        with open(file_path, 'r') as file:
            content = file.read()  
            words = content.split()  
            for word in words:
                if word in keyword.kwlist:  
                    keywords_in_code.add(word) 
        return keywords_in_code
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()

def print_keywords_per_character(keywords):
    for kw in keywords:
        for char in kw:
            print(char, end=' ')
        print() 

def print_all_keywords(keywords):
    print(", ".join(keywords))

def display_menu():
    file_path = r'C:\Users\Raja\Desktop\Semester 5\Compilation Technique\Class Exercise Week 1\Question1.py'
    
    keywords_in_code = extract_keywords_from_code(file_path)
    
    if not keywords_in_code:
        print("No Python keywords found in the code.")
        return

    print("Please choose an option:")
    print("1. Print keywords per character")
    print("2. Print all keywords")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print_keywords_per_character(keywords_in_code)
    elif choice == '2':
        print_all_keywords(keywords_in_code)
    else:
        print("Invalid choice. Please choose 1 or 2.")

display_menu()
