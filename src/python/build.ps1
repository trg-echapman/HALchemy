param (
    [switch]$InstallPackage
)

"Creating local virtual environment"
python -m venv .venv

"Activating local virtual environment"
.\.venv\Scripts\activate.ps1

"Installing build module"
pip install build

"Setting up 'setup.cfg' configuration file"
python configure.py

"Building HALchemy module package"
python -m build

if ($InstallPackage) {
    "Installing HALchemy to local virtual environment"
    pip install .
}
else {
    "Deactivating local virtual environment"
    deactivate .\.gitignore
}
