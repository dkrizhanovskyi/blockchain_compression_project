# setup.py

"""
Module: Setup Configuration for Blockchain Compression Project
Purpose:
    The `setup.py` file serves as the configuration script for the blockchain compression project, 
    enabling the project to be packaged and distributed as a Python package. This file uses `setuptools` 
    to manage the installation process, dependencies, and entry points, making the project easier 
    to install and run on different systems.

    Key Features:
    - Defines project metadata such as name, version, author information, and URL.
    - Specifies the directory structure for source files, allowing the project to be modular.
    - Includes optional development dependencies, such as testing tools like `pytest`.
    - Sets up an entry point for command-line execution, allowing users to run the project as a console script.
    - Ensures compatibility with Python 3.6 and later versions.

    Packaging Considerations:
    The configuration allows users to install the project with standard Python package tools, such as `pip`. 
    It also supports optional extras for development environments and testing.
"""
from setuptools import setup, find_packages  # Import necessary functions from setuptools for packaging.

# Call the `setup` function to define the package configuration.
setup(
    name="blockchain_compression_project",  # The name of the package as it will appear in PyPI or other repositories.
    version="0.1",  # Initial version of the project. Increment this with new releases.

    # Use `find_packages` to automatically discover all sub-packages inside the `src` directory.
    # This ensures that modules such as compression, pruning, etc., are included in the package.
    packages=find_packages(where="src"),  
    
    # Define the root directory for package modules. The source code is located under `src/`.
    package_dir={"": "src"},  
    
    # Define the package dependencies. This list is currently empty because the project 
    # relies on standard Python libraries such as `lzma`, `hashlib`, etc.
    install_requires=[
        # Add required packages here if external libraries are introduced in the future.
    ],

    # Optional dependencies for development purposes, such as testing frameworks like `pytest`.
    extras_require={
        "dev": [
            "pytest",  # Install pytest for running unit tests in the development environment.
        ]
    },

    # Specify the entry point for the command-line interface (CLI) when the project is installed.
    # This allows the user to run the project by typing `blockchain-compress` in the terminal.
    entry_points={
        "console_scripts": [
            "blockchain-compress=main:main",  # Maps the script name to the main function in `main.py`.
        ]
    },

    # Metadata fields that describe the project, useful for public repositories like PyPI.
    description="A project for compressing blockchain data and reducing storage size",  # Short description of the project.

    # Long description loaded from the README file to provide detailed documentation on PyPI.
    long_description=open("docs/README.md").read(),
    long_description_content_type="text/markdown",  # Specify that the README file is in Markdown format.

    # URL to the project's GitHub repository for reference.
    url="https://github.com/dkrizhanovskyi/blockchain_compression_project",

    # Author information for the project.
    author="Daniil Krizhanovskyi",  
    author_email="daniil.krizhanovsyki@hotmail.com",  # Contact email for the author.

    # Classifiers provide metadata about the project, such as the supported programming languages,
    # licensing, and operating systems.
    classifiers=[
        "Programming Language :: Python :: 3",  # This project uses Python 3.
        "License :: OSI Approved :: MIT License",  # The project is licensed under the MIT License.
        "Operating System :: OS Independent",  # The project is OS-independent and can run on any platform.
    ],

    # Define the minimum required Python version for compatibility. The project requires Python 3.6 or higher.
    python_requires='>=3.6',
)
"""
Architectural and Packaging Considerations:

1. **Modular Design**:
   The `setup.py` configuration leverages the `find_packages` function to ensure that all submodules 
   and packages within the `src` directory are included when the project is installed. This promotes 
   a clean separation of concerns, ensuring that each module (e.g., compression, state delta, Merkle tree) 
   is packaged and distributed effectively.

2. **Development and Testing**:
   The `extras_require` field provides a way to install development-specific dependencies, such as `pytest`. 
   This allows developers to run tests and check the integrity of the project without cluttering the main 
   installation with unnecessary dependencies.

3. **Command-line Interface (CLI)**:
   The `entry_points` field enables a simple command-line interface for users to run the project 
   without needing to manually invoke Python scripts. This makes the project more user-friendly, 
   especially when distributed to non-developers.

4. **Scalability**:
   As the project grows, external dependencies can easily be added to the `install_requires` list. 
   This flexibility ensures that future versions can incorporate additional features while maintaining 
   an efficient packaging structure.

5. **Cross-platform Compatibility**:
   The `setup.py` is designed to ensure that the project is OS-independent, allowing it to be installed 
   and run on any operating system that supports Python 3.6 or later. This promotes broad adoption 
   and use in various environments.
"""
