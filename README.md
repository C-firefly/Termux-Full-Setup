🚀 Termux Full Setup System

A complete automated setup script for Termux that prepares a fresh Termux environment with essential packages, development tools, ZSH, Oh My Zsh, plugins, themes, utilities, and personal configuration.

The project is designed to make a fresh Termux installation ready for daily use with a single setup workflow.

---

📌 Features

- ✅ Automatic Termux storage permission
- ✅ System package update & upgrade
- ✅ Essential packages installation
- ✅ Python installation
- ✅ Git, Curl, Wget
- ✅ Nano, Vim, Neovim
- ✅ Tree, Zip, Unzip, Htop, Eza
- ✅ ZSH installation
- ✅ Oh My Zsh installation
- ✅ ZSH Autosuggestions
- ✅ ZSH Syntax Highlighting
- ✅ Powerlevel10k theme
- ✅ Custom ".zshrc" support
- ✅ Development languages
- ✅ Network tools
- ✅ User information storage
- ✅ Modular installation system
- ✅ Interactive installation menu

---

📂 Project Structure

Recommended project structure:

Termux-Full-Setup/
│
├── setup.sh
├── termux_full_setup.py
│
├── User/
│   └── .zshrc
│
├── README.md
│
└── LICENSE

After installation, the script creates:

~/.my_bin/
│
└── User/
    └── user_info.json


---

⚙️ Requirements

Before starting, make sure you have:

- Android device
- Termux
- Internet connection
- Enough free storage
- Permission to access Termux storage

«It is recommended to use the latest available Termux release from a trusted source.»

---

📥 Installation

1. Clone the project

If the project is hosted on GitHub:

git clone https://github.com/C-Firefly/Termux-Full-Setup.git

Enter the project directory:

cd Termux-Full-Setup

---

2. Give execute permission

chmod +x setup.sh

---

3. Run the setup

./setup.sh

Or:

bash setup.sh

---

⚡ Quick Installation

If you already have the project files in your Termux home directory:

chmod +x setup.sh && ./setup.sh

The bootstrap script will:

Termux Storage
      ↓
Package Update
      ↓
Package Upgrade
      ↓
Python Installation
      ↓
termux_full_setup.py
      ↓
Full Setup

---

🧰 Bootstrap Script

The "setup.sh" file is responsible for preparing the basic environment before running Python.

Example:

#!/data/data/com.termux/files/usr/bin/bash

termux-setup-storage
clear

pkg update -y
pkg upgrade -y

pkg install python -y
clear

python termux_full_setup.py

exit

The Python script handles the actual setup process.

---

🐍 Python Setup Script

Run manually with:

python termux_full_setup.py

Python is responsible for:

- Installation menu
- User configuration
- Package installation
- ZSH configuration
- Plugin installation
- Theme installation
- Network tools
- Development tools
- Custom configuration

---

👤 User Information

During setup, the script asks for:

Name        :
Title       :
Device Name :

Example:

Name        : Bruce Lee
Title       : Developer
Device Name : Galaxy S25 Ultra

The information is stored in:

~/.my_bin/User/user_info.json

Example:

{
    "name": "Bruce Lee",
    "title": "Developer",
    "device_name": "Galaxy S25 Ultra"
}

This information can later be used by banners, scripts, aliases, or other Termux tools.

---

🐚 ZSH Setup

The ZSH installation follows this order:

ZSH
 ↓
Oh My Zsh
 ↓
Plugins
 ↓
Powerlevel10k
 ↓
Custom .zshrc

This order is important.

Install ZSH

pkg install zsh -y

Install Oh My Zsh

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

---

🔌 ZSH Plugins

The setup installs:

ZSH Autosuggestions

git clone https://github.com/zsh-users/zsh-autosuggestions \
${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

ZSH Syntax Highlighting

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

---

🎨 Powerlevel10k

Install:

git clone --depth=1 https://github.com/romkatv/powerlevel10k \
~/.oh-my-zsh/custom/themes/powerlevel10k

After installation, the custom ".zshrc" can configure the theme.

---

📝 Custom ".zshrc"

The project can replace the generated ".zshrc" with a custom configuration.

Recommended workflow:

Install ZSH
     ↓
Install Oh My Zsh
     ↓
Install Plugins
     ↓
Install Powerlevel10k
     ↓
Backup existing .zshrc
     ↓
Copy custom .zshrc

Example:

shutil.copy2(
    custom_zshrc,
    os.path.join(HOME, ".zshrc")
)

A backup should be created before replacing the existing configuration.

Example:

~/.zshrc.backup

---

📦 Mandatory Packages

The setup installs essential packages such as:

pkg install git curl wget zsh nano vim neovim tree unzip zip htop eza -y

These provide:

Package| Purpose
Git| Version control
Curl| HTTP/network requests
Wget| File downloading
ZSH| Advanced shell
Nano| Simple text editor
Vim| Advanced terminal editor
Neovim| Modern Vim
Tree| Directory visualization
Zip| Archive creation
Unzip| Archive extraction
Htop| System monitoring
Eza| Modern "ls" replacement

---

💻 Development Environment

The project can install common development tools.

Node.js

pkg install nodejs -y

C/C++

pkg install clang -y

Go

pkg install golang -y

---

🌐 Network Tools

Optional network tools include:

pkg install nmap -y

pkg install php -y

pkg install cloudflared -y

Python packages:

pip install requests

pip install flask

---

🖥️ Aliases

The project can create:

~/.oh-my-zsh/custom/aliases/from_setup.zsh

Example aliases:

alias ls='eza --icons --group-directories-first'
alias ll='eza -l --icons'
alias la='eza -la --icons'
alias tree='eza -T --icons'
alias update='pkg update && pkg upgrade -y'

These aliases make common Termux operations faster.

---

🔄 Workflow

The complete setup workflow is:

                    START
                      │
                      ▼
             Storage Permission
                      │
                      ▼
              Update Termux
                      │
                      ▼
             Upgrade Packages
                      │
                      ▼
              Install Python
                      │
                      ▼
            Run Python Installer
                      │
                      ▼
              Create Folders
                      │
                      ▼
            Collect User Info
                      │
                      ▼
          ┌─────────────────────┐
          │   Installation Menu │
          └─────────────────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Python       ZSH          Tools
                      │
                      ▼
                 Oh My Zsh
                      │
                      ▼
                   Plugins
                      │
                      ▼
                 Powerlevel10k
                      │
                      ▼
                Custom .zshrc
                      │
                      ▼
                Other Tools
                      │
                      ▼
                 COMPLETED

---

🧭 Installation Menu

The recommended menu structure is:

========================================
       Welcome to Termux Setup...
========================================

What do you want to setup?

✓ Mandatory (Auto Installed)

1. Git, wget, curl
2. Python
3. Languages
4. Network Tools
5. ZSH + Plugins + Theme
6. Tools
All

Example:

Enter your choice:

5

will install the ZSH environment.

Multiple selections:

2,3,5,6

Everything:

All

---

🔐 Backup & Safety

Before replacing configuration files, the setup should create backups.

For example:

cp ~/.zshrc ~/.zshrc.backup

The Python implementation can use:

shutil.copy2(
    target_zshrc,
    backup_zshrc
)

Never overwrite an existing configuration without a backup unless the user explicitly chooses to do so.

---

🔄 Reloading ZSH

The setup script does not need to execute:

source ~/.zshrc

inside Python.

After the setup is finished, either restart Termux or run:

source ~/.zshrc

This loads the new configuration.

---

✅ Advantages

🚀 Fast Setup

A fresh Termux environment can be prepared with one workflow.

🧩 Modular

Different components can be installed independently.

🎨 Customizable

Users can provide their own:

- ".zshrc"
- aliases
- theme
- banner
- scripts

💾 Persistent Configuration

User information is saved locally:

~/.my_bin/User/user_info.json

🛠 Developer Friendly

Provides common tools for:

- Python
- Node.js
- C/C++
- Go
- Git
- Networking

🐚 Better Shell Experience

ZSH + Oh My Zsh + Autosuggestions + Syntax Highlighting + Powerlevel10k provide a much better interactive terminal experience.

---

⚠️ Guidelines

1. Run on a Fresh Termux Installation

For the best result, run the setup on a relatively clean Termux environment.

2. Keep Internet Connected

Several components are downloaded from the internet.

3. Do Not Interrupt Package Installation

Avoid closing Termux while:

pkg update
pkg upgrade
pkg install

is running.

4. Backup Configuration

Always backup:

~/.zshrc

before replacing it.

5. Check Installation Errors

Do not assume a command succeeded only because the script continued.

The installer should ideally check the return code of commands.

6. Avoid Duplicate Git Clones

Before cloning plugins or themes, check whether the directory already exists.

Example:

if [ ! -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ]; then
    git clone ...
fi

7. Keep Secrets Out of Git

Never commit:

API keys
BOT tokens
Passwords
Private credentials
Personal secrets

to the repository.

Use environment variables or local configuration files instead.

---

🐞 Troubleshooting

Python command not found

Install Python:

pkg install python -y

Check:

python --version

---

Git command not found

pkg install git -y

---

ZSH command not found

pkg install zsh -y

Check:

zsh --version

---

Permission denied

Make the shell script executable:

chmod +x setup.sh

Then:

./setup.sh

---

Storage permission problem

Run:

termux-setup-storage

Then allow storage permission from Android.

---

".zshrc" not loading

Try:

source ~/.zshrc

Or completely restart Termux.

---

🧹 Uninstallation

This project mainly installs packages and configuration files. It does not provide a complete automatic uninstall by default.

To remove the project's generated data:

rm -rf ~/.my_bin

To remove the custom aliases:

rm -f ~/.oh-my-zsh/custom/aliases/from_setup.zsh

«Be careful when using "rm -rf". Always verify the path before executing it.»

---

📌 Recommended Development Practices

When adding new installation modules:

1. Create a separate function.
2. Keep installation commands isolated.
3. Check whether the package already exists.
4. Handle errors.
5. Avoid unnecessary duplicate installation.
6. Keep user configuration separate from system installation.
7. Backup configuration files before replacing them.
8. Keep sensitive information outside the repository.
9. Keep the main menu simple.
10. Test each module independently.

Example:

def install_example():
    console.print("[bold green]Installing Example...[/bold green]")
    run_cmd("pkg install example -y")

Then add it to the menu and main workflow.

---

🧪 Testing

Before releasing a new version, test:

[ ] Fresh Termux installation
[ ] Storage permission
[ ] Package update
[ ] Python installation
[ ] Mandatory packages
[ ] User information
[ ] ZSH installation
[ ] Oh My Zsh
[ ] Autosuggestions
[ ] Syntax highlighting
[ ] Powerlevel10k
[ ] Custom .zshrc
[ ] Development tools
[ ] Network tools
[ ] Alias installation
[ ] Existing .zshrc backup
[ ] Re-running the installer

---

🔁 Re-running the Installer

The installer should ideally be safe to run multiple times.

Before installing:

Does package exist?
        │
       YES
        │
     Skip
        │
       NO
        │
      Install

Likewise for Git repositories:

Directory exists?
        │
   ┌────┴────┐
  YES        NO
   │          │
 Skip       Clone

This prevents duplicate installations and errors.

---

📜 License

Choose an appropriate open-source license for your project.

For example:

MIT License

Add a "LICENSE" file to the repository if you choose MIT or another open-source license.

---

👨‍💻 Author

Termux Full Setup

A personal automated Termux environment setup project.

---

⭐ Support

If this project is useful to you:

⭐ Star the repository
🍴 Fork the project
🐛 Report bugs
💡 Suggest improvements

---

🚀 Final Setup

After everything finishes:

source ~/.zshrc

Or simply restart Termux.

Then verify:

zsh --version

python --version

git --version

eza --version

If everything is installed correctly, your Termux environment is ready.

---

🎉 Termux Ready!

╔══════════════════════════════════════╗
║                                      ║
║       🚀 TERMUX SETUP COMPLETE       ║
║                                      ║
║   ZSH          ✓                     ║
║   Plugins      ✓                     ║
║   Theme        ✓                     ║
║   Python       ✓                     ║
║   Git          ✓                     ║
║   Tools        ✓                     ║
║   Configuration ✓                    ║
║                                      ║
╚══════════════════════════════════════╝