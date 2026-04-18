import subprocess
import os

def initialize_git_repo():
    """
    Automates the Git workflow:
    Modified State -> Staged State -> Committed State
    """
    try:
        # 1. Initialize the .git directory (The heart of Git) [cite: 73, 74]
        subprocess.run(["git", "init"], check=True)
        print("Initialized empty Git repository.")

        # 2. Add files to the Staging Area (The 'Index') [cite: 69, 71, 79]
        # This moves files from the Working Directory to the Staged State [cite: 63, 70]
        subprocess.run(["git", "add", "."], check=True)
        print("Files added to the staging area.")

        # 3. Create a Commit (The Committed State) [cite: 51, 52]
        # This records the staged version permanently in the Git directory [cite: 54, 76]
        commit_message = "Initial commit: Implementing version control"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Commit successful: '{commit_message}'")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during Git operations: {e}")
    except FileNotFoundError:
        print("Git is not installed or not found in your PATH.")

if _name_ == "_main_":
    initialize_git_repo()