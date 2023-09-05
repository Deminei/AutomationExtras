import os
import subprocess

def create_project(project_name):
    # Step 1: Create the project folder
    os.makedirs(project_name, exist_ok=True)

    # Step 2: Create the index.html file
    with open(os.path.join(project_name, 'index.html'), 'w') as f:
        f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>New Project</title>\n</head>\n<body>\n\n</body>\n</html>')

    # Step 3: Create the style.css file
    with open(os.path.join(project_name, 'style.css'), 'w') as f:
        f.write('/* Add your styles here */')

    # Step 4: Create the script.js file
    with open(os.path.join(project_name, 'script.js'), 'w') as f:
        f.write('// Add your scripts here')

    # Step 5: Open the project folder in VS Code
    subprocess.run(['code', project_name])

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    create_project(project_name)

