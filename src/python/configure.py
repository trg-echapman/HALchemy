import subprocess
import os

current_directory = current_dir = os.path.dirname(os.path.abspath(__file__))


# Load the template file
with open(f"{current_directory}\\setup.cfg.tmpl", 'r') as template_file:
    template_content = template_file.read()

# Retrieve the current version from a Git tag
git_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()

# Replace the version field in the template with the retrieved version
modified_content = template_content.replace('{{version}}', git_tag)

# Save the modified content to setup.cfg
with open(f"{current_directory}\\setup.cfg", 'w') as setup_file:
    setup_file.write(modified_content)
