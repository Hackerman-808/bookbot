def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def wordcount():
    return len((main().split()))


print(wordcount())
