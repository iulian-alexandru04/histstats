from trie import Trie


def get_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


file_path = '/home/iulian/.bash_history'
trie = Trie()
for line in get_lines(file_path):
    if len(line) > 100:
        continue
    trie.insert(line)

sts = trie.prefix_stats()
sts.sort(key=lambda e: len(e[0])*e[1], reverse=True)
for pref, cnt in sts:
    print(pref, cnt)

