# 📁 Hash Table
> A Python implementation of a hash table built from scratch, with a custom hash function, collision handling via chaining, and add, remove, and lookup operations.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![project](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Data%20Structures-red?logo=python&logoColor=white)

## 📌 About

This project implements a hash table from scratch using Python's dict as the underlying storage. A custom `hash()` function converts string keys into integer hash codes using Unicode values. When two different keys produce the same hash (a collision), the table handles it using chaining, storing both key-value pairs in a nested dictionary at that hash bucket. Built to understand how hash tables work under the hood, including hashing, collisions, and bucket-based storage.

## 🧠 What I Learned

- **Building a hash function** — Converting each character in a string to its Unicode value with `ord()` and summing them to produce a hash code, understanding that different strings can produce the same sum (e.g. `"dear"` and `"read"` both hash to `412`)
- **Collision handling with chaining** — When two keys share the same hash, storing both in a nested dictionary `{hash_key: {key1: val1, key2: val2}}` so neither is lost, this is one of the two classic collision resolution strategies
- **Nested dictionary structure** — The `collection` stores `{hash_code: {original_key: value}}`, requiring two-level lookups and inserts throughout every method
- **`ord()` for Unicode** — Using Python's built-in `ord()` to get the integer Unicode code point of any character, which is the foundation of the hash function
- **Defensive lookups** — Checking both `hash_key in self.collection` and `key in self.collection[hash_key]` before any read or delete, preventing `KeyError` when accessing nested dictionaries
- **Why hash tables matter** — Understanding that Python's own dict is a hash table internally, and that O(1) average-case lookup is only possible because of the hashing layer

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |

## 💡 How It Works

String keys are hashed by summing the Unicode values of each character. The result becomes the bucket key in `self.collection`. Each bucket is itself a dictionary, allowing multiple keys to share the same hash without overwriting each other.

```
hash("dear") = 100+101+97+114 = 412
hash("read") = 114+101+97+100 = 412  ← same hash, different key

collection = {
    412: { "dear": "friend", "read": "book" },  ← chained in same bucket
    424: { "golf": "sport" }
}
```

| Method | Description |
|--------|-------------|
| `hash(string)` | Returns the sum of Unicode values for each character |
| `add(key, value)` | Hashes the key and stores the value in the correct bucket |
| `remove(key` | Hashes the key and deletes it from its bucket if found |
| `lookup(key)` | Returns the value for a key, or None if not found |

**Example Output:**
```
HashTable().hash('golf')        # 424
HashTable().lookup('golf')      # 'sport'
HashTable().lookup('cfc')       # None
```

## 🚀 Future Improvements

- [ ] Add a `__str__` method to display the full table contents in a readable format
- [ ] Implement open addressing as an alternative collision resolution strategy to compare with chaining
- [ ] Track and display the load factor to understand when the table becomes inefficient
- [ ] Extend to support integer and tuple keys, not just strings

## 📂 Project Structure

```
hash-table/
│
├── HashTable.py    # HashTable class with example usage
└── README.md
```

*Part of my Python learning journey 🐍 — diving deeper into data structures with hashing and collision resolution*
