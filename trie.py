class TrieNode:
    def __init__(self):
        # Each node holds a dictionary of child nodes and a boolean to mark the end of a word
        self.children = {}
        self.is_end_of_word = False
        self.count = 0

class Trie:
    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current.count += 1
            # If the character is not already a child, add it
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        # Mark the end of the word
        current.is_end_of_word = True
        current.count += 1

    def search(self, word: str) -> bool:
        """Return True if the word exists in the Trie, False otherwise."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        # Return True only if the current node is marked as the end of a word
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Return True if there is any word in the Trie that starts with the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def list_words(self, prefix="") -> list:
        """List all words in the Trie that start with the given prefix."""
        def dfs(node, path, words):
            # Perform a depth-first search to collect words
            if node.is_end_of_word:
                words.append("".join(path))
            for char, child in node.children.items():
                path.append(char)
                dfs(child, path, words)
                path.pop()

        # Start DFS from the node at the end of the prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []  # If prefix doesn't exist, return empty list
            current = current.children[char]

        words = []
        dfs(current, list(prefix), words)
        return words

    def prefix_stats(self):
        prefixes = []
        def dfs(node, crt_prefix):
            prefixes.append((crt_prefix, node.count))
            for char, child in node.children.items():
                dfs(child, crt_prefix + char)
        dfs(self.root, '')
        return prefixes


