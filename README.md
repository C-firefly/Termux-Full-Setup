🚀 Termux Full Setup

A complete automated setup script for Termux that transforms a fresh Termux installation into a ready-to-use development environment.

This project automatically installs essential packages, development languages, network tools, ZSH, Oh My Zsh, plugins, Powerlevel10k, custom aliases, and personal configuration.

«Created by C-Firefly»

---

✨ Features

📦 Essential Packages

Automatically installs:

- Git
- Curl
- Wget
- ZSH
- Nano
- Vim
- Neovim
- Tree
- Zip / Unzip
- Htop
- Eza

🐚 ZSH Environment

Automatically configures:

- ZSH
- Oh My Zsh
- Powerlevel10k
- ZSH Autosuggestions
- ZSH Syntax Highlighting

💻 Programming Languages

Optional installation of:

- Node.js
- C / C++ (Clang)
- Go

🌐 Network & Web Tools

Optional installation of:

- Nmap
- PHP
- Cloudflared
- Python Requests
- Flask

⚡ Custom Aliases

Includes useful aliases for Eza and Termux package management:

ls
ll
la
tree
update

Example:

alias ls='eza --icons --group-directories-first'
alias ll='eza -l --icons'
alias la='eza -la --icons'
alias tree='eza -T --icons'
alias update='pkg update && pkg upgrade -y'

👤 User Configuration

The setup can save basic user information:

{
    "name": "Your Name",
    "title": "Your Title",
    "device_name": "Your Device"
}

---

📋 Requirements

- Android device
- Termux
- Internet connection
- Python 3
- "pip"

It is recommended to use the latest version of Termux available from a trusted source.

---

📥 Installation

Clone the repository:

git clone https://github.com/C-firefly/Termux-Full-Setup.git

Enter the project directory:

cd Termux-Full-Setup

Run the setup script:

python setup.py

Replace "setup.py" with the actual Python filename if different.

---

🛠️ Setup Process

The script follows this general workflow:

Start
  │
  ├── Create required directories
  │
  ├── Save user information
  │
  ├── Install mandatory packages
  │
  ├── Select optional components
  │
  ├── Install development languages
  │
  ├── Install network tools
  │
  └── Configure ZSH
        │
        ├── ZSH
        ├── Oh My Zsh
        ├── Plugins
        ├── Powerlevel10k
        ├── Aliases
        └── Custom .zshrc

---

🎯 Menu Options

When the script starts, you can select:

1. Git, Wget, Curl (Auto)
2. Languages
3. Network Tools
4. Setup ZSH (Theme, Autosuggestion, Autocomplete, Highlighting)

All

You can also select multiple options:

2,3,4

Or install everything:

All

---

🎨 ZSH Configuration

The project uses:

Oh My Zsh

Provides the main ZSH framework and configuration system.

Powerlevel10k

Provides a fast and customizable ZSH prompt.

zsh-autosuggestions

Shows suggestions based on previously used commands.

zsh-syntax-highlighting

Highlights commands while typing and helps identify invalid commands.

---

⚡ Custom ".zshrc"

The project includes a custom ".zshrc" configuration.

It provides:

- Oh My Zsh integration
- Powerlevel10k support
- Plugin loading
- Custom aliases
- History configuration
- Useful ZSH options
- PATH configuration
- Locale configuration

The existing ".zshrc" is backed up before the custom configuration is installed.

Backup location:

~/.zshrc.backup

---

🔄 Updating

Oh My Zsh update mode can be configured from ".zshrc".

For reminder mode:

zstyle ':omz:update' mode reminder

For automatic updates:

zstyle ':omz:update' mode auto

For disabling automatic update checks:

zstyle ':omz:update' mode disabled

---

📁 Project Structure

A typical project structure:

Termux-Full-Setup/
│
├── setup.py
├── .zshrc
├── README.md
└── ...

After installation, configuration files are placed inside:

~/.oh-my-zsh/
~/.my_bin/
~/.zshrc

User information is stored in:

~/.my_bin/User/user_info.json

---

⚠️ Important Notes

This script modifies your Termux environment and may:

- Install or upgrade packages
- Change the default shell to ZSH
- Install Oh My Zsh
- Replace your existing ".zshrc"
- Create configuration files
- Modify your shell PATH

If you already have a customized ".zshrc", make sure you keep a backup.

The script automatically attempts to create:

~/.zshrc.backup

before installing the custom configuration.

---

🔧 Troubleshooting

ZSH is installed but theme is not working

Try:

source ~/.zshrc

Or restart Termux.

Check the current shell:

echo $SHELL

Check Powerlevel10k:

ls ~/.oh-my-zsh/custom/themes/powerlevel10k

---

Check installed plugins

ls ~/.oh-my-zsh/custom/plugins

You should see:

zsh-autosuggestions
zsh-syntax-highlighting

---

Reload ZSH configuration

source ~/.zshrc

---

🧑‍💻 Author

C-Firefly

GitHub:

https://github.com/C-firefly

---

⭐ Support

If this project helped you set up your Termux environment, consider giving the repository a ⭐ on GitHub.

Feel free to fork the project and customize it for your own Termux setup.

---

📜 License

This project is provided for personal and educational use.

You are free to modify and improve the project according to your needs.