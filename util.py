def lines(file):
    for line in file:
        yield line
        yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':

    file = open('text_input.txt', 'r', encoding='utf-8')
    for line in blocks(file):
        print(line)