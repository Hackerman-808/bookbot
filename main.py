from collections import Counter


def readtext():
    # This is a one-liner option, but poses risks as without with statement things can complicate:
    # code: return open("books/frankenstein.txt").read()
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

    
def formatword():
    return (readtext().split())
    
    
def formatchar():
    return "".join([char for char in readtext().lower() if char.isalpha()])


def wordcount():
    return len(formatword())


def charcountsort():
    return sorted(Counter(formatchar()).items(), key=lambda x: x[1], reverse=True)


def main():
    print( 
        f"\n--- Begin report of books/frankenstein.txt ---"
        f"\n\n{wordcount()} words found in the document"
        f"\n\n{'\n'.join(f'The \'{char}\' character was found {count} times' for char, count in charcountsort())}"
        f"\n\n--- End of report ---\n"
        )


main()
