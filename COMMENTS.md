# COMMENTS - SETUP GUIDE
  - This readme focuses on setup in your local environment as  per instructions.
  - Currently, it's a Unix-based machine guide (like macOS or Linux).
  - If you're familiar with this setup, you can skip this section and go to `README.md`

# Prerequisites
  - Before starting, ensure that your local machine has the following installed:

  - Python 3.6+: The Python runtime to execute the script.
  - Git: For cloning the repository.
  - pip: Python's package manager to install dependencies.
  - Virtual Environment (venv): A tool for creating isolated Python environments.

# Verify Python and Git Installation
  - You can verify if Python and Git are installed by running these commands:
  
  In your terminal:

```bash
python3 --version  # Check Python version 
git --version     # Check Git version
```

  **If either is missing, you can install them:**
     - Install Python: Follow instructions at python.org.
     - Install Git: Follow instructions at git-scm.com.

# Setting Up Your Local Development Environment

  1. **Clone the Repository**
    - First, clone the repository to your local machine using Git.

In terminal:
```bash
git clone https://github.com/Sambi85/spark-advisors-code-challenge-2025.git
cd ./spark-advisors-code-challenge-2025
```

2. **Create a Virtual Environment**
    - Inside the project folder, create a virtual environment using Python's venv module.
   
In terminal:
```bash
python3 -m venv venv
```

3. **Activate the Virtual Environment**
  - Once the virtual environment is created, activate it. This isolates your project’s dependencies from your global Python environment.

In terminal:
```bash
source venv/bin/activate
```

4. **Run the Project**
  - After the dependencies are installed, you’re ready to run the project. Checkout my \`COMMENTS.md\` for more details on the project and how to run the script.

5. **Deactivating the Virtual Environment**
  - Once you’re finished working on the project, you can deactivate the virtual environment with:

In terminal:
```bash
deactivate
```