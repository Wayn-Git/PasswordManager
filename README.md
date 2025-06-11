# Simple Password Manager

A basic Python-based password manager that stores credentials in a local text file.

## Features

- **Add Passwords**: Store username, password, and platform information
- **View Passwords**: Display all saved credentials
- **Delete Passwords**: Remove specific entries and automatically renumber remaining ones
- **Simple Interface**: Command-line based with easy-to-use prompts

## How to Use

1. **Run the program**:
   ```bash
   python password_manager.py
   ```

2. **Enter main password** (currently for display only)

3. **Choose an action**:
   - `add` - Add a new password entry
   - `view` - Display all saved passwords
   - `delete` - Remove a password entry
   - `q` - Exit the program

## File Structure

The program creates and manages a `password.txt` file in the same directory, storing entries in this format:
```
1. Username: john@email.com | Password: mypassword123 | Platform: Gmail

2. Username: johnsmith | Password: securepass456 | Platform: Facebook
```

## Functions

### `view()`
- Reads and displays all password entries from the file
- Shows "No saved passwords" if file is empty
- Handles missing file gracefully

### `add()`
- Prompts for username/email, password, and platform
- Auto-generates index numbers for new entries
- Appends new entries to the file

### `delete()`
- Shows all current entries
- Allows deletion by index number
- Automatically renumbers remaining entries
- Updates the file with reorganized data

## Requirements

- Python 3.x
- No external dependencies required

## ⚠️ Important Security Notice

**This is a basic educational project and should NOT be used for storing real passwords.**

**Security Limitations:**
- Passwords are stored in **plain text** (unencrypted)
- No actual authentication verification
- File permissions are not restricted
- No password strength validation
- Vulnerable to anyone with file system access

## Recommended Improvements

For a production-ready password manager, consider:
- Password encryption/hashing
- Secure authentication system
- Database storage instead of text files
- Password strength requirements
- Master password verification
- Backup and recovery features
- Cross-platform compatibility

## Educational Purpose

This project demonstrates:
- File I/O operations in Python
- Basic error handling with try/except
- Simple menu-driven program structure
- String manipulation and formatting
- List comprehensions for data filtering

## License

This is a simple educational project. Use and modify as needed for learning purposes.
