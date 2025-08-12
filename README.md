# Git Helper

A simple interactive Python script to help you manage your Git repositories from the command line.

## Features
- Create new branches
- Commit changes
- Push to remote
- Pull from remote
- Show status
- Stash changes
- Reset hard to a previous commit (with confirmation)

## Usage

1. Clone or download this repository:
```bash
git clone https://github.com/CiccioBro17/Git-Helper.git
```

2. Make sure you have Python and Git installed.

3. Enter the directory of the cloned repository:
```bash
cd Git-Helper
```

3. Copy the ```main.py``` file to your desired location:
```bash
cp main.py /path/to/your/directory/
```

3. Run the script in your terminal:
```bash
python3 main.py
```

4. Follow the interactive prompts to perform Git operations.

## Example Menu
```
What do you want to do?
1) Create a new branch
2) Commit changes
3) Push to remote
4) Pull from remote
5) Show status
6) Stash changes
7) Reset hard to previous commit
8) Exit
```

## Requirements
- Python 3.x
- Git must be installed and available in your PATH

## Disclaimer
This tool is intended for simple Git workflows and learning purposes. Use with caution, especially when using the reset feature, as it can discard changes. It's just a simple project I wanted to make, obviusly not a replacement for more complex Git tools or workflows.

## License

This project is under the MIT license.
