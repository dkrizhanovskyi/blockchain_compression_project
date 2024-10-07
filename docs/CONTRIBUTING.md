# Contributing to Blockchain Compression Project

We appreciate your interest in contributing to the **Blockchain Compression Project**. By contributing, you can help us improve blockchain data storage efficiency, enhance cryptographic security, and further optimize this project. Please follow the guidelines below to ensure a smooth process for everyone involved.

---

### Table of Contents
1. [How to Contribute](#how-to-contribute)
2. [Setting up the Development Environment](#setting-up-the-development-environment)
3. [Code Style and Guidelines](#code-style-and-guidelines)
4. [Running Tests](#running-tests)
5. [Submitting a Pull Request](#submitting-a-pull-request)
6. [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
7. [License](#license)

---

## How to Contribute

There are several ways to contribute to the project:
- **Reporting Bugs**: Found a bug or an issue? Open an issue in the GitHub repository, and provide detailed steps to reproduce the problem.
- **Proposing Features**: Have an idea to improve the project? Open a feature request issue, and describe how it could enhance the project.
- **Contributing Code**: Help us by implementing new features, fixing bugs, or improving the documentation.

Please ensure your contributions align with the goals of the project (i.e., enhancing blockchain data compression, storage efficiency, and cryptographic integrity).

---

## Setting up the Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dkrizhanovskyi/blockchain_compression_project.git
   cd blockchain_compression_project
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   Install the required packages by running:
   ```bash
   pip install -e .
   ```

4. **Install development dependencies**:
   If you're planning to run tests or make changes to the code, install additional dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run tests** to make sure everything is set up correctly:
   ```bash
   pytest
   ```

---

## Code Style and Guidelines

### Code Style:
- Follow **PEP 8** style guidelines for Python code.
- Write clear, concise, and meaningful comments and docstrings.
- Ensure your code is clean and easy to read. Use consistent naming conventions.
- Avoid duplicating code (follow the DRY principle).

### Architectural Considerations:
- Follow the **SOLID** principles for architecture and design:
  - **Single Responsibility**: Ensure each module or class has a single responsibility.
  - **Open/Closed**: Make your code open for extension, but closed for modification.
  - **Liskov Substitution**: Ensure that derived classes can be substituted for their base classes without issues.
  - **Interface Segregation**: Don't force users to depend on interfaces they don't use.
  - **Dependency Inversion**: Depend on abstractions, not concrete implementations.
  
### Cryptographic Integrity:
- If you work on cryptographic components (e.g., Merkle Trees, ZK-SNARKs), ensure that any changes or additions maintain the cryptographic security of the system.
- Avoid using custom cryptographic algorithms unless necessary. Always prefer well-tested, standard algorithms.
  
### Documentation:
- All functions and classes must include docstrings.
- Keep the **README.md** and **docs/** updated as new features are added.
- Ensure that any cryptographic changes are documented with clear explanations of how they affect data security.

---

## Running Tests

Before submitting changes, make sure that all tests pass successfully. We use **pytest** as the testing framework.

1. Run the full test suite with:
   ```bash
   pytest
   ```

2. Make sure to write new tests for any new functionality or bug fixes:
   - Place your test files in the `tests/` directory.
   - Name your test functions with the `test_` prefix.
   - Ensure that all critical components (e.g., compression, cryptographic verification, state management) are thoroughly tested.

3. Code coverage:
   - Ensure the code you contribute is well-tested to maintain or improve the current level of test coverage.
   - You can check code coverage by running:
     ```bash
     pytest --cov=src
     ```

---

## Submitting a Pull Request

When you're ready to submit your changes, please follow these steps:

1. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/my-feature
   ```

2. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of my changes"
   ```

3. **Push the branch to GitHub**:
   ```bash
   git push origin feature/my-feature
   ```

4. **Submit a pull request**:
   - Go to the GitHub repository and create a new pull request from your branch.
   - In your pull request description, explain what the change does and how it has been tested.

5. **Review**:
   - A project maintainer will review your pull request.
   - If changes are requested, please address them promptly and update your pull request.
   
---

## Bug Reports and Feature Requests

If you encounter a bug or would like to propose a new feature, please submit an issue on the GitHub repository:

- **Bugs**: Include a clear and concise description of the problem, including steps to reproduce it.
- **Feature Requests**: Provide a detailed explanation of the feature you'd like to see, and describe its potential benefits to the project.

When reporting bugs or requesting features, please make sure that your issue:
- Includes as much detail as possible (stack traces, logs, error messages).
- References any related issues if applicable.
  
---

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
