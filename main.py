import subprocess

def run_git_command(cmd_list):
    result = subprocess.run(['git'] + cmd_list, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error:", result.stderr)

def list_commits():
    # Get last 5 commits with hashes and messages
    result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
    commits = result.stdout.strip().split('\n')
    for i, commit in enumerate(commits, 1):
        print(f"{i}) {commit}")
    return commits

def reset_hard():
    commits = list_commits()
    choice = input("Enter the number of the commit to reset to: ")
    try:
        idx = int(choice) - 1
        commit_hash = commits[idx].split()[0]
        commit_msg = ' '.join(commits[idx].split()[1:])
        confirm = input(
            f"You chose commit {commit_hash} — \"{commit_msg}\"\n"
            f"Are you sure you want to reset your current branch to this commit? This will discard all changes after it! (yes/no): "
        )
        if confirm.lower() == 'yes':
            run_git_command(['reset', '--hard', commit_hash])
            print("Reset successful!")
        else:
            print("Reset cancelled.")
    except (IndexError, ValueError):
        print("Invalid choice.")

def main():
    while True:
        print("\nWhat do you want to do?")
        print("1) Create a new branch")
        print("2) Commit changes")
        print("3) Push to remote")
        print("4) Pull from remote")
        print("5) Show status")
        print("6) Stash changes")
        print("7) Reset hard to previous commit")
        print("8) Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            branch = input("Enter new branch name: ")
            run_git_command(['checkout', '-b', branch])
        elif choice == '2':
            msg = input("Enter commit message: ")
            run_git_command(['add', '.'])
            run_git_command(['commit', '-m', msg])
        elif choice == '3':
            run_git_command(['push'])
        elif choice == '4':
            run_git_command(['pull'])
        elif choice == '5':
            run_git_command(['status'])
        elif choice == '6':
            run_git_command(['stash'])
            print("Changes stashed!")
        elif choice == '7':
            reset_hard()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main()
