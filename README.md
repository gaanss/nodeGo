# 🚀 NodeGo Automation Tool

![NodeGo Interface](https://github.com/gaanss/nodeGo/blob/main/int.png)

## ✨ Features

- 📝 **Account Registration** - automatic registration with proxy support and captcha solving
- ✅ **Task Completion** - automatically complete available tasks for rewards
- 🔄 **Automatic Session Recovery** - re-login when access tokens expire
- 🌐 **Proxy Support** - full HTTP proxy support to bypass limitations
- 📊 **Data Storage** - all accounts and tasks are stored in a PostgreSQL database
- 🔒 **Code Protection** - code is obfuscated using PyArmor for intellectual property protection

## 🛠️ Required Settings

### Prerequisites
- Python 3.11
- PostgreSQL database (instructions for setting up a free DB on Neon below)
- Accounts file (accounts.txt)
- Proxy file (proxy.txt)
- CAPSolver API key for solving captchas

### ⚙️ Configure settings.yaml file

```yaml
database:
  host: your-host.neon.tech
  port: 5432
  name: nodego
  user: postgres
  password: your-password

proxy:
  type: http
  file: proxy.txt

files:
  accounts: accounts.txt

registration:
  threads: 3
  delays:
    min: 2
    max: 5
  username_prefix: user_

capsolver:
  api_key: YOUR_CAPSOLVER_API_KEY
  site_key: 0x4AAAAAAA4zgfgCoYChIZf4
  site_url: https://nodego.ai
```

## 🚀 Installation and Launch

1. Clone the repository:
```bash
git clone https://github.com/gaanss/nodeGo.git
cd nodego
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure settings.yaml, accounts.txt, and proxy.txt files

5. Run the program:
```bash
python main.py
```

## 🔒 Code Protection

This project is protected to secure the intellectual property and prevent unauthorized copying or reverse engineering. The distributed version contains obfuscated code that functions identically to the original but is protected against analysis and modification.

### Why code obfuscation?
- Prevents unauthorized use of proprietary technology
- Mitigates risks of code theft and replication

For contributors who need access to the original source code, please contact the repository owner.

## 🗄️ Free PostgreSQL Database on Neon

[Neon](https://neon.tech) offers a free PostgreSQL database tier with excellent performance.

### Step 1: Register on Neon
1. Go to [neon.tech](https://neon.tech) and click "Sign Up"
2. Create an account (using GitHub, Google, or Email)

### Step 2: Create a Project
1. Click "New Project"
2. Enter a project name (e.g., "NodeGo")
3. Select the region closest to you
4. Click "Create Project"

### Step 3: Set Up the Database
1. After creating the project, you'll see connection details
2. Copy the connection details (host, port, username, password)
3. Create a new database named "nodego" through the Neon interface or SQL console:
   ```sql
   CREATE DATABASE nodego;
   ```

### Step 4: Configure Connection
1. Update the `database` section in settings.yaml with the connection details from Neon
2. Make sure you're using the correct host URL, which has the format `[project-id].neon.tech`

## 📁 Project Structure

```
nodego/
├── main.py           # Main program file (obfuscated)
├── settings.yaml     # Settings file
├── requirements.txt  # Project dependencies
├── accounts.txt      # Accounts file
├── proxy.txt         # Proxy file
├── logs/             # Logs directory
└── modules/          # Program modules (obfuscated)
    ├── api_client.py      # API client for interaction with NodeGo
    ├── captcha_solver.py  # Module for solving captchas
    ├── database.py        # Database interaction
    ├── proxy_manager.py   # Proxy management
    ├── registration.py    # Account registration
    └── tasks.py           # Task management
```

## 📝 File Formats

### accounts.txt
```
email1@example.com:password1
email2@example.com:password2
```

### proxy.txt
```
username:password@ip:port
```

## 📄 License

MIT License

## 🙏 Acknowledgments

Developed with ❤️ for the NodeGo community. 
