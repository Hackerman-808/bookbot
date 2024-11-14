def readtext():
    # This is a one-liner option, but poses risks as without with statement things can complicate:
    # return open("books/frankenstein.txt").read()
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

    
def formatword():
    return (readtext().split())
    
    
def formatchar():
    return "".join([char for char in readtext().lower() if char.isalpha()])


def wordcount():
    return len(formatword())


def charcount():
    return {char: formatchar().count(char) for char in set(formatchar())}


def main():
    print(f"Number of words is: {wordcount()} \n{'\n'.join(f'{k}: {v}' for k, v in charcount().items())}")


main()
