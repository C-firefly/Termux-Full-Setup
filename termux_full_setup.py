#!/data/data/com.termux/files/usr/bin/python

# ============================================================
# Termux Full Setup
# ============================================================
#
# Safe / Repeatable / Idempotent Termux setup
#
# Features:
#   - Mandatory packages
#   - zip / unzip
#   - Development languages
#   - Network tools
#   - ZSH
#   - Oh My Zsh
#   - Plugins
#   - Powerlevel10k
#   - Safe .zshrc handling
#   - KeyboardInterrupt handling
#   - Safe "All" re-run
#
# ============================================================

import os
import sys
import time
import json
import shutil
import subprocess
from pathlib import Path


# ============================================================
# RICH
# ============================================================

try:
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    print("[•] Installing Rich...")

    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "rich",
            ],
            check=True,
        )

        from rich.console import Console
        from rich.panel import Panel

    except Exception as e:
        print(f"[!] Could not install Rich: {e}")
        print("[!] Continuing without Rich.")

        class Console:
            def print(self, *args, **kwargs):
                print(*args)

        class Panel:
            @staticmethod
            def fit(text):
                return text


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

stp = "\033[0m"


# ============================================================
# BASIC PATHS
# ============================================================

HOME = str(Path.home())

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ============================================================
# PROJECT PATHS
# ============================================================

MY_BIN = os.path.join(
    HOME,
    ".my_bin"
)

USER_DIR = os.path.join(
    MY_BIN,
    "User"
)

USER_FILE = os.path.join(
    USER_DIR,
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

ALIAS_FILE = os.path.join(
    ALIAS_DIR,
    "from_setup.zsh"
)

P10K_DIR = os.path.join(
    ZSH_THEME_DIR,
    "powerlevel10k"
)


# ============================================================
# ZSHRC
# ============================================================

CUSTOM_ZSHRC = os.path.join(
    BASE_DIR,
    ".zshrc"
)

TARGET_ZSHRC = os.path.join(
    HOME,
    ".zshrc"
)

BACKUP_ZSHRC = os.path.join(
    HOME,
    ".zshrc.backup"
)

ZSH_SETUP_MARKER = os.path.join(
    HOME,
    ".termux_setup_zsh"
)


# ============================================================
# CONSTANTS
# ============================================================

SETUP_MARKER = "# >>> TERMUX-FULL-SETUP >>>"
SETUP_MARKER_END = "# <<< TERMUX-FULL-SETUP <<<"

ZSH_SETUP_VERSION = "1"


# ============================================================
# GLOBAL INTERRUPT STATE
# ============================================================

INTERRUPTED = False


# ============================================================
# KEYBOARD INTERRUPT
# ============================================================

def handle_interrupt():
    global INTERRUPTED

    INTERRUPTED = True

    print()
    print()
    print(
        f"{y}[!] Setup interrupted by user (Ctrl+C).{stp}"
    )

    print(
        f"{c}[•] No existing configuration was intentionally removed.{stp}"
    )

    print(
        f"{c}[•] You can run the setup again safely.{stp}"
    )

    sys.exit(130)


# ============================================================
# CLEAR
# ============================================================

def clear():
    try:
        os.system("clear")
    except KeyboardInterrupt:
        handle_interrupt()


# ============================================================
# PAUSE
# ============================================================

def pause(seconds=1):
    try:
        time.sleep(seconds)
    except KeyboardInterrupt:
        handle_interrupt()


# ============================================================
# PRINT HELPERS
# ============================================================

def print_success(message):
    print(
        f"{g}[✓] {message}{stp}"
    )


def print_error(message):
    print(
        f"{r}[✗] {message}{stp}"
    )


def print_info(message):
    print(
        f"{c}[•] {message}{stp}"
    )


def print_warning(message):
    print(
        f"{y}[!] {message}{stp}"
    )


# ============================================================
# COMMAND RUNNER
# ============================================================

def run_cmd(
    cmd,
    clear_after=False,
    check=False,
):
    """
    Run shell command safely.

    Returns:
        exit code
    """

    print()
    print(
        f"{y}[+] Running:{stp} {cmd}"
    )

    try:

        result = subprocess.run(
            cmd,
            shell=True,
        )

    except KeyboardInterrupt:
        handle_interrupt()

    except Exception as e:
        print_error(
            f"Command execution error: {e}"
        )
        return 1

    if result.returncode == 0:

        print_success(
            "Command completed successfully."
        )

    else:

        print_error(
            f"Command failed! Exit code: "
            f"{result.returncode}"
        )

        if check:
            return result.returncode

    if clear_after:
        pause(1)
        clear()

    return result.returncode


# ============================================================
# COMMAND EXISTS
# ============================================================

def command_exists(command):
    return shutil.which(command) is not None


# ============================================================
# PACKAGE INSTALLED
# ============================================================

def package_installed(package):
    """
    Check whether a Termux package is installed.
    """

    try:

        result = subprocess.run(
            [
                "dpkg",
                "-s",
                package,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        return result.returncode == 0

    except KeyboardInterrupt:
        handle_interrupt()

    except Exception:
        return False


# ============================================================
# CREATE DIRECTORIES
# ============================================================

def create_folders():

    print_info(
        "Creating required directories..."
    )

    os.makedirs(
        MY_BIN,
        exist_ok=True,
    )

    os.makedirs(
        USER_DIR,
        exist_ok=True,
    )

    if not os.path.exists(USER_FILE):

        with open(
            USER_FILE,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                {},
                f,
                indent=4,
                ensure_ascii=False,
            )

    print_success(
        "Required directories ready."
    )


# ============================================================
# USER INFORMATION
# ============================================================

def set_username():

    print()
    print("=" * 45)
    print("        USER INFORMATION SETUP")
    print("=" * 45)
    print()

    try:

        name = input(
            "Name        : "
        ).strip()

        title = input(
            "Title       : "
        ).strip()

        device_name = input(
            "Device Name : "
        ).strip()

    except KeyboardInterrupt:
        handle_interrupt()

    except EOFError:

        print_warning(
            "Input closed. Keeping existing user information."
        )

        return

    user_info = {
        "name": name,
        "title": title,
        "device_name": device_name,
    }

    try:

        with open(
            USER_FILE,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                user_info,
                f,
                indent=4,
                ensure_ascii=False,
            )

    except Exception as e:

        print_error(
            f"Could not save user information: {e}"
        )

        return

    print()
    print_success(
        "User information saved."
    )

    print(
        f"{c}File:{stp} {USER_FILE}"
    )

    pause(1)


# ============================================================
# MANDATORY PACKAGES
# ============================================================

def mandatory_install():

    console.print(
        Panel.fit(
            "[bold green]"
            "Installing Mandatory Packages"
            "[/bold green]"
        )
    )

    packages = [
        "git",
        "curl",
        "wget",
        "zsh",
        "nano",
        "vim",
        "neovim",
        "tree",
        "unzip",
        "zip",
        "htop",
        "eza",
    ]

    missing = [
        package
        for package in packages
        if not package_installed(package)
    ]

    if not missing:

        print_success(
            "All mandatory packages are already installed."
        )

        return True

    print_info(
        "Missing packages:"
    )

    print(
        " ".join(missing)
    )

    command = (
        "pkg install "
        + " ".join(missing)
        + " -y"
    )

    code = run_cmd(
        command,
        check=True,
    )

    if code != 0:

        print_error(
            "Mandatory package installation failed."
        )

        return False

    print_success(
        "Mandatory packages completed."
    )

    return True


# ============================================================
# ZSH INSTALLED?
# ============================================================

def zsh_installed():

    return (
        command_exists("zsh")
        or package_installed("zsh")
    )


# ============================================================
# OH MY ZSH INSTALLED?
# ============================================================

def oh_my_zsh_installed():

    return os.path.isdir(
        ZSH_DIR
    )


# ============================================================
# PLUGIN INSTALLED
# ============================================================

def plugin_installed(plugin_name):

    plugin_path = os.path.join(
        ZSH_PLUGIN_DIR,
        plugin_name,
    )

    return os.path.isdir(
        plugin_path
    )


# ============================================================
# THEME INSTALLED
# ============================================================

def theme_installed():

    return os.path.isdir(
        P10K_DIR
    )


# ============================================================
# ZSHRC HAS OUR CONFIG
# ============================================================

def zshrc_has_setup():

    if not os.path.isfile(
        TARGET_ZSHRC
    ):
        return False

    try:

        with open(
            TARGET_ZSHRC,
            "r",
            encoding="utf-8",
        ) as f:

            content = f.read()

        return (
            SETUP_MARKER in content
            and
            SETUP_MARKER_END in content
        )

    except Exception:
        return False


# ============================================================
# ZSH COMPLETE CHECK
# ============================================================

def is_zsh_setup_complete():

    required = [
        zsh_installed(),
        oh_my_zsh_installed(),
        plugin_installed(
            "zsh-autosuggestions"
        ),
        plugin_installed(
            "zsh-syntax-highlighting"
        ),
        theme_installed(),
        os.path.isfile(ALIAS_FILE),
        zshrc_has_setup(),
    ]

    marker_exists = os.path.isfile(
        ZSH_SETUP_MARKER
    )

    return (
        all(required)
        and marker_exists
    )


# ============================================================
# INSTALL ZSH + OH MY ZSH
# ============================================================

def install_zsh():

    console.print(
        Panel.fit(
            "[bold green]"
            "Installing ZSH + Oh My Zsh"
            "[/bold green]"
        )
    )

    # --------------------------------------------------------
    # ZSH
    # --------------------------------------------------------

    if zsh_installed():

        print_success(
            "ZSH is already installed. Skipping."
        )

    else:

        print_info(
            "Installing ZSH..."
        )

        code = run_cmd(
            "pkg install zsh -y",
            check=True,
        )

        if code != 0:
            return False

    # --------------------------------------------------------
    # Default shell
    # --------------------------------------------------------

    if command_exists("chsh"):

        print_info(
            "Checking default shell..."
        )

        try:

            shell_path = shutil.which(
                "zsh"
            )

            if shell_path:

                result = subprocess.run(
                    [
                        "chsh",
                        "-s",
                        shell_path,
                    ]
                )

                if result.returncode == 0:

                    print_success(
                        "ZSH set as default shell."
                    )

                else:

                    print_warning(
                        "Could not change default shell."
                    )

        except KeyboardInterrupt:
            handle_interrupt()

        except Exception as e:

            print_warning(
                f"chsh failed: {e}"
            )

    # --------------------------------------------------------
    # Oh My Zsh
    # --------------------------------------------------------

    if oh_my_zsh_installed():

        print_success(
            "Oh My Zsh already installed. Skipping."
        )

    else:

        print_info(
            "Installing Oh My Zsh..."
        )

        ohmyzsh_command = (
            'RUNZSH=no '
            'CHSH=no '
            'KEEP_ZSHRC=yes '
            'sh -c "$(curl -fsSL '
            'https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh'
            ')"'
        )

        code = run_cmd(
            ohmyzsh_command,
            check=True,
        )

        if code != 0:

            print_error(
                "Oh My Zsh installation failed."
            )

            return False

    # --------------------------------------------------------
    # Verify
    # --------------------------------------------------------

    if not oh_my_zsh_installed():

        print_error(
            "Oh My Zsh directory was not found."
        )

        return False

    print_success(
        "ZSH + Oh My Zsh ready."
    )

    return True


# ============================================================
# INSTALL SINGLE PLUGIN
# ============================================================

def install_git_plugin(
    plugin_name,
    repo_url,
):

    target = os.path.join(
        ZSH_PLUGIN_DIR,
        plugin_name,
    )

    if os.path.isdir(target):

        print_success(
            f"{plugin_name} already installed. Skipping."
        )

        return True

    os.makedirs(
        ZSH_PLUGIN_DIR,
        exist_ok=True,
    )

    print_info(
        f"Installing {plugin_name}..."
    )

    code = run_cmd(
        f'git clone "{repo_url}" "{target}"',
        check=True,
    )

    if code != 0:

        print_error(
            f"Could not install {plugin_name}."
        )

        return False

    print_success(
        f"{plugin_name} installed."
    )

    return True


# ============================================================
# ZSH PLUGINS
# ============================================================

def install_plugin():

    console.print(
        Panel.fit(
            "[bold green]"
            "Installing ZSH Plugins"
            "[/bold green]"
        )
    )

    if not oh_my_zsh_installed():

        print_error(
            "Oh My Zsh is not installed."
        )

        return False

    os.makedirs(
        ZSH_PLUGIN_DIR,
        exist_ok=True,
    )

    success = True

    # Autosuggestions
    if not install_git_plugin(
        "zsh-autosuggestions",
        "https://github.com/zsh-users/zsh-autosuggestions.git",
    ):
        success = False

    # Syntax highlighting
    if not install_git_plugin(
        "zsh-syntax-highlighting",
        "https://github.com/zsh-users/zsh-syntax-highlighting.git",
    ):
        success = False

    return success


# ============================================================
# POWERLEVEL10K
# ============================================================

def install_theme():

    console.print(
        Panel.fit(
            "[bold green]"
            "Installing Powerlevel10k Theme"
            "[/bold green]"
        )
    )

    if theme_installed():

        print_success(
            "Powerlevel10k already installed. Skipping."
        )

        return True

    os.makedirs(
        ZSH_THEME_DIR,
        exist_ok=True,
    )

    code = run_cmd(
        f'git clone --depth=1 '
        f'"https://github.com/romkatv/powerlevel10k.git" '
        f'"{P10K_DIR}"',
        check=True,
    )

    if code != 0:

        print_error(
            "Powerlevel10k installation failed."
        )

        return False

    print_success(
        "Powerlevel10k installed."
    )

    return True


# ============================================================
# ALIASES
# ============================================================

def inject_alias():

    print_info(
        "Installing custom aliases..."
    )

    os.makedirs(
        ALIAS_DIR,
        exist_ok=True,
    )

    block = """#___Termux-Setup___

alias ls='eza --icons --group-directories-first'
alias ll='eza -l --icons'
alias la='eza -la --icons'
alias tree='eza -T --icons'

alias update='pkg update && pkg upgrade -y'

"""

    try:

        if os.path.isfile(
            ALIAS_FILE
        ):

            with open(
                ALIAS_FILE,
                "r",
                encoding="utf-8",
            ) as f:

                content = f.read()

        else:

            content = ""

        if "#___Termux-Setup___" in content:

            print_success(
                "Aliases already configured. Skipping."
            )

        else:

            with open(
                ALIAS_FILE,
                "a",
                encoding="utf-8",
            ) as f:

                if content and not content.endswith(
                    "\n"
                ):
                    f.write("\n")

                f.write(block)

            print_success(
                "Aliases added."
            )

    except Exception as e:

        print_error(
            f"Could not install aliases: {e}"
        )

        return False

    print(
        f"{c}Alias file:{stp} {ALIAS_FILE}"
    )

    return True


# ============================================================
# BACKUP ZSHRC
# ============================================================

def backup_zshrc():

    if not os.path.isfile(
        TARGET_ZSHRC
    ):
        return True

    # Don't overwrite previous backup.
    if os.path.isfile(
        BACKUP_ZSHRC
    ):

        print_success(
            "Existing .zshrc backup already exists."
        )

        return True

    try:

        shutil.copy2(
            TARGET_ZSHRC,
            BACKUP_ZSHRC,
        )

        print_success(
            "Existing .zshrc backed up."
        )

        return True

    except Exception as e:

        print_error(
            f"Could not backup .zshrc: {e}"
        )

        return False


# ============================================================
# CREATE ZSH SETUP BLOCK
# ============================================================

def get_zsh_setup_block():

    return f"""
{SETUP_MARKER}

# ------------------------------------------------------------
# Termux Full Setup
# ------------------------------------------------------------

# Oh My Zsh
export ZSH="$HOME/.oh-my-zsh"

# Powerlevel10k
ZSH_THEME="powerlevel10k/powerlevel10k"

# Oh My Zsh plugins
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

# Load Oh My Zsh
if [ -f "$ZSH/oh-my-zsh.sh" ]; then
    source "$ZSH/oh-my-zsh.sh"
fi

# Custom aliases
if [ -f "$ZSH/custom/aliases/from_setup.zsh" ]; then
    source "$ZSH/custom/aliases/from_setup.zsh"
fi

# Load Powerlevel10k configuration if present
if [ -f "$HOME/.p10k.zsh" ]; then
    source "$HOME/.p10k.zsh"
fi

{SETUP_MARKER_END}
"""


# ============================================================
# INSTALL / UPDATE ZSHRC SAFELY
# ============================================================

def install_custom_zshrc():

    print_info(
        "Configuring .zshrc safely..."
    )

    if not os.path.isfile(
        TARGET_ZSHRC
    ):

        try:

            with open(
                TARGET_ZSHRC,
                "w",
                encoding="utf-8",
            ) as f:

                f.write(
                    "# Termux ZSH configuration\n"
                )

            print_success(
                "Created new .zshrc."
            )

        except Exception as e:

            print_error(
                f"Could not create .zshrc: {e}"
            )

            return False

    # --------------------------------------------------------
    # Existing setup?
    # --------------------------------------------------------

    try:

        with open(
            TARGET_ZSHRC,
            "r",
            encoding="utf-8",
        ) as f:

            content = f.read()

    except Exception as e:

        print_error(
            f"Could not read .zshrc: {e}"
        )

        return False

    # --------------------------------------------------------
    # Already configured
    # --------------------------------------------------------

    if (
        SETUP_MARKER in content
        and
        SETUP_MARKER_END in content
    ):

        print_success(
            "Termux setup block already exists in .zshrc."
        )

        return True

    # --------------------------------------------------------
    # Backup before modification
    # --------------------------------------------------------

    if not backup_zshrc():

        return False

    # --------------------------------------------------------
    # Append our configuration
    # --------------------------------------------------------

    try:

        block = get_zsh_setup_block()

        if not content.endswith("\n"):
            content += "\n"

        content += block

        with open(
            TARGET_ZSHRC,
            "w",
            encoding="utf-8",
        ) as f:

            f.write(content)

        print_success(
            "ZSH configuration added without replacing existing config."
        )

        return True

    except Exception as e:

        print_error(
            f"Could not update .zshrc: {e}"
        )

        return False


# ============================================================
# CREATE ZSH COMPLETION MARKER
# ============================================================

def create_zsh_marker():

    try:

        with open(
            ZSH_SETUP_MARKER,
            "w",
            encoding="utf-8",
        ) as f:

            f.write(
                "TERMUX_FULL_SETUP_ZSH=1\n"
                f"VERSION={ZSH_SETUP_VERSION}\n"
            )

        print_success(
            "ZSH setup completion marker created."
        )

        return True

    except Exception as e:

        print_error(
            f"Could not create ZSH marker: {e}"
        )

        return False


# ============================================================
# COMPLETE ZSH SETUP
# ============================================================

def setup_zsh():

    clear()

    console.print(
        Panel.fit(
            "[bold cyan]"
            "ZSH COMPLETE SETUP"
            "[/bold cyan]"
        )
    )

    # --------------------------------------------------------
    # Already complete?
    # --------------------------------------------------------

    if is_zsh_setup_complete():

        print_success(
            "ZSH setup is already complete."
        )

        print_info(
            "Skipping ZSH setup to prevent overwriting."
        )

        return True

    # --------------------------------------------------------
    # ZSH
    # --------------------------------------------------------

    if not install_zsh():

        return False

    clear()

    # --------------------------------------------------------
    # Plugins
    # --------------------------------------------------------

    if not install_plugin():

        print_warning(
            "Some ZSH plugins could not be installed."
        )

    clear()

    # --------------------------------------------------------
    # Theme
    # --------------------------------------------------------

    if not install_theme():

        return False

    clear()

    # --------------------------------------------------------
    # Aliases
    # --------------------------------------------------------

    if not inject_alias():

        return False

    clear()

    # --------------------------------------------------------
    # ZSHRC
    # --------------------------------------------------------

    if not install_custom_zshrc():

        return False

    clear()

    # --------------------------------------------------------
    # Final verification
    # --------------------------------------------------------

    if (
        zsh_installed()
        and oh_my_zsh_installed()
        and plugin_installed(
            "zsh-autosuggestions"
        )
        and plugin_installed(
            "zsh-syntax-highlighting"
        )
        and theme_installed()
        and os.path.isfile(ALIAS_FILE)
        and zshrc_has_setup()
    ):

        create_zsh_marker()

        print()
        print("=" * 50)
        print(
            f"{g}       ZSH SETUP COMPLETED ✓{stp}"
        )
        print("=" * 50)
        print()

        print(
            f"{y}Restart Termux or run:{stp}"
        )

        print(
            f"{c}source ~/.zshrc{stp}"
        )

        pause(2)

        return True

    print_error(
        "ZSH setup verification failed."
    )

    return False


# ============================================================
# PROGRAMMING LANGUAGES
# ============================================================

def install_language():

    console.print(
        Panel.fit(
            "[bold green]"
            "Installing Development Languages"
            "[/bold green]\n\n"
            "Node.js\n"
            "C/C++\n"
            "Go"
        )
    )

    packages = [
        "nodejs",
        "clang",
        "golang",
    ]

    missing = [
        package
        for package in packages
        if not package_installed(package)
    ]

    if not missing:

        print_success(
            "Development languages already installed."
        )

        return True

    code = run_cmd(
        "pkg install "
        + " ".join(missing)
        + " -y",
        check=True,
    )

    if code != 0:
        return False

    print_success(
        "Development language installation completed."
    )

    return True


# ============================================================
# NETWORK TOOLS
# ============================================================

def install_network_tool():

    console.print(
        Panel.fit(
            "[bold green]"
            "Installing Network Tools"
            "[/bold green]\n\n"
            "Nmap\n"
            "PHP\n"
            "Cloudflared\n"
            "Requests\n"
            "Flask"
        )
    )

    packages = [
        "nmap",
        "php",
        "cloudflared",
    ]

    missing = [
        package
        for package in packages
        if not package_installed(package)
    ]

    if missing:

        code = run_cmd(
            "pkg install "
            + " ".join(missing)
            + " -y",
            check=True,
        )

        if code != 0:
            print_warning(
                "Some Termux network packages failed."
            )

    else:

        print_success(
            "Nmap, PHP and Cloudflared already installed."
        )

    # --------------------------------------------------------
    # Python Requests
    # --------------------------------------------------------

    run_cmd(
        "python -m pip install requests",
        check=False,
    )

    # --------------------------------------------------------
    # Flask
    # --------------------------------------------------------

    run_cmd(
        "python -m pip install flask",
        check=False,
    )

    print_success(
        "Network tools installation completed."
    )

    return True


# ============================================================
# MENU
# ============================================================

def menu():

    clear()

    print("=" * 50)
    print("        Welcome to Termux Setup")
    print("=" * 50)

    print()

    print(
        f"{g}✓ Mandatory packages will be installed automatically."
        f"{stp}"
    )

    print()

    print(
        "1. Mandatory Packages"
    )

    print(
        "2. Languages"
    )

    print(
        "3. Network Tools"
    )

    print(
        "4. Setup ZSH + Theme + Plugins"
    )

    print()

    print(
        "All"
    )

    print()

    try:

        choice = input(
            "Enter your choice (e.g: 2,3,4 or All): "
        )

    except KeyboardInterrupt:
        handle_interrupt()

    except EOFError:

        print()
        print_warning(
            "Input closed."
        )

        return "all"

    return choice.lower().strip()


# ============================================================
# SETUP COMPLETE
# ============================================================

def setup_complete():

    clear()

    print()
    print("=" * 55)
    print()
    print(
        f"{g}       🎉 TERMUX SETUP COMPLETED!{stp}"
    )
    print()
    print("=" * 55)

    print()

    print(
        f"{c}Your Termux environment is ready.{stp}"
    )

    print()

    if is_zsh_setup_complete():

        print(
            f"{y}ZSH setup is installed and protected from re-installation."
            f"{stp}"
        )

        print()

        print(
            f"{g}Restart Termux or run:{stp}"
        )

        print(
            f"{c}source ~/.zshrc{stp}"
        )

    else:

        print(
            f"{y}ZSH was not completely configured.{stp}"
        )

    print()


# ============================================================
# MAIN
# ============================================================

def main():

    # --------------------------------------------------------
    # Create directories
    # --------------------------------------------------------

    create_folders()

    # --------------------------------------------------------
    # User information
    # --------------------------------------------------------

    set_username()

    # --------------------------------------------------------
    # Menu
    # --------------------------------------------------------

    choice = menu()

    # --------------------------------------------------------
    # Mandatory packages
    # --------------------------------------------------------

    clear()

    print(
        f"{g}Starting Mandatory Setup...{stp}"
    )

    if not mandatory_install():

        print_error(
            "Mandatory setup failed."
        )

        return 1

    # --------------------------------------------------------
    # ALL
    # --------------------------------------------------------

    if choice == "all":

        # ----------------------------------------------------
        # Languages
        # ----------------------------------------------------

        clear()

        install_language()

        # ----------------------------------------------------
        # Network
        # ----------------------------------------------------

        clear()

        install_network_tool()

        # ----------------------------------------------------
        # ZSH
        # ----------------------------------------------------

        clear()

        if is_zsh_setup_complete():

            print_success(
                "ZSH + Theme + Plugins already configured."
            )

            print_info(
                "Skipping option 4."
            )

        else:

            setup_zsh()

    # --------------------------------------------------------
    # Selected options
    # --------------------------------------------------------

    else:

        selections = [
            item.strip()
            for item in choice.split(",")
        ]

        # ----------------------------------------------------
        # 1
        # ----------------------------------------------------

        if "1" in selections:

            clear()

            print(
                f"{g}"
                "Mandatory packages "
                "are already handled automatically."
                f"{stp}"
            )

            pause(1)

        # ----------------------------------------------------
        # 2
        # ----------------------------------------------------

        if "2" in selections:

            clear()

            install_language()

        # ----------------------------------------------------
        # 3
        # ----------------------------------------------------

        if "3" in selections:

            clear()

            install_network_tool()

        # ----------------------------------------------------
        # 4
        # ----------------------------------------------------

        if "4" in selections:

            clear()

            if is_zsh_setup_complete():

                print_success(
                    "ZSH setup already complete."
                )

                print_info(
                    "Nothing will be overwritten."
                )

                pause(2)

            else:

                setup_zsh()

    # --------------------------------------------------------
    # Final
    # --------------------------------------------------------

    setup_complete()

    return 0


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    try:

        sys.exit(
            main()
        )

    except KeyboardInterrupt:

        handle_interrupt()

    except EOFError:

        print()
        print_warning(
            "Input closed. Exiting safely."
        )

        sys.exit(0)

    except Exception as e:

        print()
        print_error(
            f"Unexpected error: {e}"
        )

        print(
            f"{y}[!] Your existing configuration was not intentionally removed."
            f"{stp}"
        )

        sys.exit(1)