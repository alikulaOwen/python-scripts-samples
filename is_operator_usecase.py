#demonstrating is operator common use case
def say_something(word=None):
    if word is None:
        print("Aint saying shiet")
    else: 
        print(f"I was saying,'{word}'")

def main():
    word = input("Say something: ")
    say_something(word)

if __name__ == "__main__":
    main()
