Simple File Cipher
==================

Description
-----------
This is a small, educational program that "encrypts" files by modifying bytes using a short, repeating randomly generated key. THIS IS NOT A SECURE cryptographic algorithm and should not be used to protect sensitive data.

Requirements
------------
- Python 3.7+ (standard library is sufficient)

Installation
------------
1. Clone the repository or copy the project files into a folder.
2. No additional packages are required.

Running
-------
1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

An interactive menu will ask you to choose:
- `1` — encrypt a file (optionally create a backup)
- `2` — decrypt a file (requires the key)
- `3` — quit

Usage examples
--------------
- Encrypt without backup:
  - choose `1`, answer `N`, and provide the filename
- Encrypt with backup:
  - choose `1`, answer `Y`, and provide the filename (a file named `backup_<filename>` will be created)
- Decrypt:
  - choose `2`, provide the filename and the key (the key is printed after encryption in the form of numbers separated by `-`)

Security notice
---------------
- This algorithm is educational only. Although `secrets` improves randomness, the method of adding byte values with a repeating short key is not secure.
- Do not use this program to encrypt real sensitive data.

Development and testing
-----------------------
- Add tests under a `tests/` folder and run them with `pytest`.

Contact / Author
----------------
Educational project — modify and experiment freely.
