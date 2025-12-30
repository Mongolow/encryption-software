
Simple File Cipher
==================

Description
-----------
This is a small, educational program that "encrypts" files by first compressing them with zlib and then applying a short, repeating numeric key to each byte. THIS IS NOT A SECURE cryptographic algorithm and should not be used to protect sensitive data.

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
- `1` — encrypt a file (optionally create a backup copy)
- `2` — decrypt a file (requires the key)
- `3` — quit

How the program works (current behavior)
--------------------------------------
- When encrypting, the program compresses file bytes using `zlib.compress()` and then shifts each byte by values from a randomly generated numeric key (values 1–255) in a repeating pattern.
- The key is printed to the console after encryption as a sequence of integers separated by `-` (for example: `3-7-1-...`). Keep this key to decrypt.
- If you choose the backup option in the interactive menu, the program creates a file named `backup_<original_filename>` in the current working directory and then encrypts the original file in place.

Limitations and important notes
-------------------------------
- Security: The used cipher is educational and not secure.
- Compression: Files are compressed before encryption. Encrypted data is high-entropy and will not compress further.
- Keys: The program prints the key in plaintext. Do not store or distribute that key next to the encrypted file without protecting it.
- Atomicity: The program currently overwrites files in place. If the process is interrupted during write, data loss or corruption is possible. Consider keeping explicit backups before running on important files.
- Paths and backups: The backup name `backup_<filename>` is created in the current working directory. If `filename` contains directory components, creation may fail or behave unexpectedly. Use simple filenames or implement a safer backup path.
- Large files: The program reads whole files into memory. Very large files may exhaust system memory.

Examples
--------
- Encrypt without backup: choose `1`, answer `N`, provide filename.
- Encrypt with backup: choose `1`, answer `Y`, provide filename — the program will create `backup_<filename>` then encrypt original.
- Decrypt: choose `2`, provide filename and the previously printed key.

Contact / Author
----------------
Educational project — modify and experiment freely. Report bugs or ask for help by editing the repository files.
