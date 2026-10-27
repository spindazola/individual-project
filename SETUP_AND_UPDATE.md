# Setup and Update Commands

## Updating an existing local repository with the full pack

From Terminal:

```bash
cd ~/Developer/university/"Year 3"/individual-project

# Make a safety checkpoint first
git status
git add .
git commit -m "Checkpoint before full IP pack" || true
git branch backup-before-full-pack-2026-10-27 || true

# Overlay the downloaded full pack
unzip -o ~/Downloads/individual-project-full-2026-10-27.zip -d .

# Activate the project environment
source .venv/bin/activate
pip install -r requirements.txt

# Verify code/tests
python -m pytest

# Inspect and commit the new project structure
git status
git add .
git commit -m "Add full IP research pack, sources and meeting updates"

# Open in VS Code
code .
```

If `code` is not installed as a shell command, open VS Code manually and choose this repository folder.

## New machine / clean setup

```bash
mkdir -p ~/Developer/university/"Year 3"/individual-project
cd ~/Developer/university/"Year 3"/individual-project
unzip ~/Downloads/individual-project-full-2026-10-27.zip -d .
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name individual-project --display-name "Python (Individual Project)"
git init
git add .
git commit -m "Initial individual project repository"
code .
```
