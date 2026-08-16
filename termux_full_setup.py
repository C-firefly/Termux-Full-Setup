# ============================================================
# Termux Full Setup
# ============================================================
#
# A complete automated setup script for Termux that prepares
# a fresh Termux environment with essential packages,
# development tools, ZSH, Oh My Zsh, plugins, themes,
# utilities, aliases and personal configuration.
#
# This code is created by C-Firefly
#
# GitHub: https://c-firefly.github.io
# ============================================================


import os
import time
import json
import shutil
import subprocess
from pathlib import Path


# ============================================================
# RICH
# ============================================================

try:
	import rich
except ImportError:
	print("[•] Installing Rich...")
	subprocess.run(
		["python", "-m", "pip", "install", "rich"],
		check=False
	)

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table


console = Console()


# ============================================================
# COLORS
# ============================================================

a = "\033[1;30m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

stp = "\033[1;0m"
itl = "\033[1;3m"
unl = "\033[1;4m"
lgt = "\033[1;1m"


# ============================================================
# BASIC PATHS
# ============================================================

HOME = str(Path.home())

# Directory where this Python script exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# PROJECT PATHS
# ============================================================

Z_Profile = os.path.join(HOME, ".zprofile")

MY_BIN = os.path.join(
	HOME,
	".my_bin"
)

User_Dir = os.path.join(
	MY_BIN,
	"User"
)

User_File = os.path.join(
	User_Dir,
	"user_info.json"
)


# ============================================================
# ZSH PATHS
# ============================================================

ZSH_DIR = os.path.join(
	HOME,
	".oh-my-zsh"
)

ZSH_CUSTOM = os.path.join(
	ZSH_DIR,
	"custom"
)

ZSH_PLUGIN_DIR = os.path.join(
	ZSH_CUSTOM,
	"plugins"
)

ZSH_THEME_DIR = os.path.join(
	ZSH_CUSTOM,
	"themes"
)

ALIAS_DIR = os.path.join(
	ZSH_CUSTOM,
	"aliases"
)

Aliash = os.path.join(
	ALIAS_DIR,
	"from_setup.zsh"
)


# ============================================================
# CUSTOM ZSHRC
# ============================================================

Custom_Zshrc = os.path.join(
	BASE_DIR,
	".zshrc"
)

Target_Zshrc = os.path.join(
	HOME,
	".zshrc"
)

Backup_Zshrc = os.path.join(
	HOME,
	".zshrc.backup"
)


# ============================================================
# UTILITY
# ============================================================

def clear():
	"""
	Clear terminal screen.
	"""
	os.system("clear")


def pause(seconds=1):
	"""
	Small delay.
	"""
	time.sleep(seconds)


def print_success(message):
	print(f"{g}[✓] {message}{stp}")


def print_error(message):
	print(f"{r}[✗] {message}{stp}")


def print_info(message):
	print(f"{c}[•] {message}{stp}")


# ============================================================
# COMMAND RUNNER
# ============================================================

def run_cmd(cmd, clear_after=True):
	"""
	Run shell command and return exit code.
	"""

	print()
	print(f"{y}[+] Running:{stp} {cmd}")

	result = subprocess.run(
		cmd,
		shell=True
	)

	if result.returncode == 0:
		print_success("Command completed successfully.")
	else:
		print_error(
			f"Command failed! Exit code: {result.returncode}"
		)

	if clear_after:
		pause(2)
		clear()

	return result.returncode


# ============================================================
# CREATE PROJECT DIRECTORIES
# ============================================================

def create_folders():

	print_info("Creating required directories...")

	os.makedirs(
		MY_BIN,
		exist_ok=True
	)

	os.makedirs(
		User_Dir,
		exist_ok=True
	)

	# ZSH custom directories (No need, these will automatically create)
	#os.makedirs(
	#	ZSH_CUSTOM,
	#	exist_ok=True
	#)

	#os.makedirs(
	#	ZSH_PLUGIN_DIR,
	#	exist_ok=True
	#)

	#os.makedirs(
	#	ZSH_THEME_DIR,
	#	exist_ok=True
	#)

	#os.makedirs(
	#	ALIAS_DIR,
	#	exist_ok=True
	#)

	# Create user_info.json if missing
	if not os.path.exists(User_File):

		with open(
			User_File,
			"w",
			encoding="utf-8"
		) as f:

			json.dump(
				{},
				f,
				indent=4,
				ensure_ascii=False
			)

	print_success("Required directories created.")


# ============================================================
# USER INFORMATION
# ============================================================

def set_username():

	print()
	print("=" * 40)
	print("       USER INFORMATION SETUP")
	print("=" * 40)
	print()

	name = input("Name        : ").strip()
	title = input("Title       : ").strip()
	device_name = input("Device Name : ").strip()

	user_info = {
		"name": name,
		"title": title,
		"device_name": device_name
	}

	with open(
		User_File,
		"w",
		encoding="utf-8"
	) as f:

		json.dump(
			user_info,
			f,
			indent=4,
			ensure_ascii=False
		)

	print()
	print_success("User information saved.")
	print(f"{c}File:{stp} {User_File}")

	pause(1)


# ============================================================
# MANDATORY PACKAGES
# ============================================================

def mandatory_install():

	console.print(
		Panel.fit(
			"[bold green]Installing Mandatory Packages[/bold green]"
		)
	)

	run_cmd(
		"pkg update -y && pkg upgrade -y"
	)

	run_cmd(
		"pkg install "
		"git "
		"curl "
		"wget "
		"zsh "
		"nano "
		"vim "
		"neovim "
		"tree "
		"unzip "
		"zip "
		"htop "
		"eza "
		"-y"
	)

	print_success("Mandatory packages completed.")


# ============================================================
# ZSH INSTALLATION
# ============================================================

def install_zsh():

	console.print(
		Panel.fit(
			"[bold green]Installing ZSH + Oh My Zsh[/bold green]"
		)
	)

	# --------------------------------------------------------
	# 1. Install ZSH
	# --------------------------------------------------------

	print_info("Installing ZSH...")

	run_cmd(
		"pkg install zsh -y"
	)

	# --------------------------------------------------------
	# 2. Set ZSH as default shell
	# --------------------------------------------------------

	print_info("Setting ZSH as default shell...")

	run_cmd(
		"chsh -s zsh"
	)

	# --------------------------------------------------------
	# 3. Install Oh My Zsh
	# --------------------------------------------------------

	print_info("Installing Oh My Zsh...")

	ohmyzsh_command = (
		'RUNZSH=no CHSH=no KEEP_ZSHRC=yes '
		'sh -c "$(curl -fsSL '
		'https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh'
		')"'
	)

	run_cmd(
		ohmyzsh_command
	)

	print_success(
		"ZSH + Oh My Zsh installation completed."
	)


# ============================================================
# ZSH PLUGINS
# ============================================================

def install_plugin():

	console.print(
		Panel.fit(
			"[bold green]Installing ZSH Plugins[/bold green]"
		)
	)

	# --------------------------------------------------------
	# Autosuggestions
	# --------------------------------------------------------

	autosuggestions_dir = os.path.join(
		ZSH_PLUGIN_DIR,
		"zsh-autosuggestions"
	)

	if os.path.isdir(autosuggestions_dir):

		print_success(
			"zsh-autosuggestions already installed."
		)

	else:

		run_cmd(
			"git clone "
			"https://github.com/zsh-users/zsh-autosuggestions "
			"${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/"
			"zsh-autosuggestions"
		)

	# --------------------------------------------------------
	# Syntax Highlighting
	# --------------------------------------------------------

	syntax_dir = os.path.join(
		ZSH_PLUGIN_DIR,
		"zsh-syntax-highlighting"
	)

	if os.path.isdir(syntax_dir):

		print_success(
			"zsh-syntax-highlighting already installed."
		)

	else:

		run_cmd(
			"git clone "
			"https://github.com/zsh-users/zsh-syntax-highlighting.git "
			"${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/"
			"zsh-syntax-highlighting"
		)

	print_success("ZSH plugin setup completed.")


# ============================================================
# POWERLEVEL10K THEME
# ============================================================

def install_theme():

	console.print(
		Panel.fit(
			"[bold green]Installing Powerlevel10k Theme[/bold green]"
		)
	)

	p10k_dir = os.path.join(
		ZSH_THEME_DIR,
		"powerlevel10k"
	)

	if os.path.isdir(p10k_dir):

		print_success(
			"Powerlevel10k already installed."
		)

		return

	run_cmd(
		"git clone --depth=1 "
		"https://github.com/romkatv/powerlevel10k "
		"~/.oh-my-zsh/custom/themes/powerlevel10k"
	)

	print_success(
		"Powerlevel10k installation completed."
	)


# ============================================================
# ALIASES
# ============================================================

def inject_alias():

	print_info("Installing custom aliases...")

	# Make sure directory exists
	os.makedirs(
		ALIAS_DIR,
		exist_ok=True
	)

	# Create file if missing
	if not os.path.exists(Aliash):

		with open(
			Aliash,
			"w",
			encoding="utf-8"
		):
			pass

	block = """#___Termux-Setup___
# Shortcuts for Eza

alias ls='eza --icons --group-directories-first'
alias ll='eza -l --icons'
alias la='eza -la --icons'
alias tree='eza -T --icons'

alias update='pkg update && pkg upgrade -y'

"""

	with open(
		Aliash,
		"r",
		encoding="utf-8"
	) as f:

		content = f.read()

	if "#___Termux-Setup___" not in content:

		with open(
			Aliash,
			"a",
			encoding="utf-8"
		) as f:

			f.write(block)

			print_success(
				"Aliases added."
			)

	else:

		print_success(
			"Aliases already configured."
		)

	print(f"{c}Alias file:{stp} {Aliash}")


# ============================================================
# CUSTOM ZSHRC
# ============================================================

def install_custom_zshrc():

	print_info("Installing custom .zshrc...")

	if not os.path.isfile(Custom_Zshrc):

		print_error(
			"Custom .zshrc not found!"
		)

		print(
			f"{y}Expected:{stp} {Custom_Zshrc}"
		)

		return False

	# Backup existing .zshrc
	if os.path.isfile(Target_Zshrc):

		try:

			shutil.copy2(
				Target_Zshrc,
				Backup_Zshrc
			)

			print_success(
				"Existing .zshrc backed up."
			)

		except Exception as e:

			print_error(
				f"Could not backup .zshrc: {e}"
			)

			return False

	# Install custom .zshrc
	try:

		shutil.copy2(
			Custom_Zshrc,
			Target_Zshrc
		)

		print_success(
			"Custom .zshrc installed."
		)

	except Exception as e:

		print_error(
			f"Could not install .zshrc: {e}"
		)

		return False

	print(f"{c}Installed:{stp} {Target_Zshrc}")

	return True


# ============================================================
# COMPLETE ZSH SETUP
# ============================================================

def setup_zsh():

	clear()

	console.print(
		Panel.fit(
			"[bold cyan]ZSH COMPLETE SETUP[/bold cyan]"
		)
	)

	# IMPORTANT ORDER:
	#
	# ZSH
	# ↓
	# Oh My Zsh
	# ↓
	# Plugins
	# ↓
	# Theme
	# ↓
	# Aliases
	# ↓
	# Custom .zshrc

	install_zsh()

	clear()

	install_plugin()

	clear()

	install_theme()

	clear()

	inject_alias()

	clear()

	install_custom_zshrc()

	clear()

	print()
	print("=" * 45)
	print(f"{g}        ZSH SETUP COMPLETED ✓{stp}")
	print("=" * 45)
	print()

	print(
		f"{y}Restart Termux or run:{stp}"
	)

	print(
		f"{c}source ~/.zshrc{stp}"
	)

	pause(2)


# ============================================================
# PROGRAMMING LANGUAGES
# ============================================================

def install_language():

	console.print(
		Panel.fit(
			"""[bold green]
Installing Development Languages

1. Node.js
2. C/C++
3. Go
			[/bold green]"""
		)
	)

	run_cmd(
		"pkg install nodejs -y"
	)

	run_cmd(
		"pkg install clang -y"
	)

	run_cmd(
		"pkg install golang -y"
	)

	print_success(
		"Development language installation completed."
	)


# ============================================================
# NETWORK TOOLS
# ============================================================

def install_network_tool():

	console.print(
		Panel.fit(
			"""[bold green]
Installing Network Tools

1. Nmap
2. PHP
3. Cloudflared
4. Requests
5. Flask
			[/bold green]"""
		)
	)

	run_cmd(
		"pkg install nmap -y"
	)

	run_cmd(
		"pkg install php -y"
	)

	run_cmd(
		"pkg install cloudflared -y"
	)

	run_cmd(
		"python -m pip install requests"
	)

	run_cmd(
		"python -m pip install flask"
	)

	print_success(
		"Network tools installation completed."
	)


# ============================================================
# MENU
# ============================================================

def menu():

	clear()

	print("=" * 45)
	print("        Welcome to Termux Setup")
	print("=" * 45)

	print()
	print(
		f"{g}✓ Mandatory packages will be installed automatically.{stp}"
	)

	print()
	print("1. Git, Wget, Curl (Auto)")
	print("2. Languages")
	print("3. Network Tools")
	print("4. Setup ZSH (Theme, Autosuggestions, Autocomplete, Highlighting")
	print()
    print("All")
	print()

	choice = input(
		"Enter your choice (e.g: 2,3,4 or All): "
	).lower().strip()

	return choice


# ============================================================
# COMPLETION MESSAGE
# ============================================================

def setup_complete():

	clear()

	print()
	print("=" * 50)
	print()
	print(
		f"{g}       🎉 TERMUX SETUP COMPLETED!{stp}"
	)
	print()
	print("=" * 50)

	print()
	print(
		f"{c}Your Termux environment is ready.{stp}"
	)

	print()

	print(
		f"{y}If ZSH was installed, restart Termux or run:{stp}"
	)

	print(
		f"{g}source ~/.zshrc{stp}"
	)

	print()


# ============================================================
# MAIN
# ============================================================

def main():

	# --------------------------------------------------------
	# Step 1: Create directories
	# --------------------------------------------------------

	create_folders()

	# --------------------------------------------------------
	# Step 2: User information
	# --------------------------------------------------------

	set_username()

	# --------------------------------------------------------
	# Step 3: Menu
	# --------------------------------------------------------

	choice = menu()

	# --------------------------------------------------------
	# Step 4: Mandatory packages
	# --------------------------------------------------------

	clear()

	print(
		f"{g}Starting Mandatory Setup...{stp}"
	)

	mandatory_install()

	# --------------------------------------------------------
	# Step 5: Selected modules
	# --------------------------------------------------------

	if choice == "all":

		# Languages
		clear()
		install_language()

		# Network tools
		clear()
		install_network_tool()

		# ZSH
		clear()
		setup_zsh()

	else:

		selections = [
			item.strip()
			for item in choice.split(",")
		]

		# ----------------------------------------------------
		# 1. Mandatory
		# ----------------------------------------------------

		if "1" in selections:

			clear()

			print(
				f"{g}Git, Wget and Curl are included "
				f"in Mandatory packages.{stp}"
			)

			pause(1)

		# ----------------------------------------------------
		# 2. Languages
		# ----------------------------------------------------

		if "2" in selections:

			clear()

			install_language()

		# ----------------------------------------------------
		# 3. Network
		# ----------------------------------------------------

		if "3" in selections:

			clear()

			install_network_tool()

		# ----------------------------------------------------
		# 4. ZSH
		# ----------------------------------------------------

		if "4" in selections:

			clear()

			setup_zsh()

	# --------------------------------------------------------
	# Final
	# --------------------------------------------------------

	setup_complete()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
	main()