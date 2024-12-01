def count_words(s: str) -> int:
    str_list = s.split()
    return len(str_list)


def get_words_frequency(s: str) -> dict[str, int]:
    result = {}
    for c in s:
        if not c.isalpha():
            continue

        c_lower = c.lower()
        if c_lower not in result:
            result[c_lower] = 0
        result[c_lower] += 1

    return result


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def main() -> None:
    file_content = read_file("books/frankenstein.txt")
    words_frequency = get_words_frequency(file_content)
    word_list = [{"char": k, "count": v} for k, v in words_frequency.items()]
    word_list.sort(reverse=True, key=lambda d: d["count"])  # type: ignore

    print(f"{count_words(file_content)} words found in the document")

    for word in word_list:
        print(f"The '{word['char']}' character was found {word['count']} times")


main()
