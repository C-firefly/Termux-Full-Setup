 #!/data/data/com.termux/files/usr/bin/bash

# ============================================================
# Termux Full Setup Launcher
# ============================================================

set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/termux_full_setup.py"

# ------------------------------------------------------------
# Colors
# ------------------------------------------------------------

RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
RESET='\033[0m'

# ------------------------------------------------------------
# Keyboard Interrupt
# ------------------------------------------------------------

cleanup() {
    echo
    echo -e "${YELLOW}[!] Setup interrupted by user.${RESET}"
    echo -e "${CYAN}[•] Nothing was intentionally removed.${RESET}"
    exit 130
}

trap cleanup INT TERM

# ------------------------------------------------------------
# Clear
# ------------------------------------------------------------

clear

echo
echo "=============================================="
echo "        TERMUX FULL SETUP"
echo "=============================================="
echo

# ------------------------------------------------------------
# Check Termux
# ------------------------------------------------------------

if [ ! -d "/data/data/com.termux/files/usr" ]; then
    echo -e "${RED}[✗] This script must run inside Termux.${RESET}"
    exit 1
fi

# ------------------------------------------------------------
# Storage Permission
# ------------------------------------------------------------

echo -e "${CYAN}[•] Requesting storage permission...${RESET}"

if ! termux-setup-storage; then
    echo -e "${YELLOW}[!] Storage permission command returned an error.${RESET}"
    echo -e "${YELLOW}[!] Continuing anyway...${RESET}"
fi

echo

# ------------------------------------------------------------
# Update repositories
# ------------------------------------------------------------

echo -e "${CYAN}[•] Updating Termux packages...${RESET}"

if ! pkg update -y; then
    echo -e "${RED}[✗] pkg update failed.${RESET}"
    exit 1
fi

if ! pkg upgrade -y; then
    echo -e "${RED}[✗] pkg upgrade failed.${RESET}"
    exit 1
fi

# ------------------------------------------------------------
# Python
# ------------------------------------------------------------

echo -e "${CYAN}[•] Installing Python...${RESET}"

if ! pkg install python -y; then
    echo -e "${RED}[✗] Python installation failed.${RESET}"
    exit 1
fi

# ------------------------------------------------------------
# Check Python script
# ------------------------------------------------------------

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo
    echo -e "${RED}[✗] Python setup script not found:${RESET}"
    echo "    $PYTHON_SCRIPT"
    exit 1
fi

echo
echo -e "${GREEN}[✓] Starting Termux Full Setup...${RESET}"
echo

# ------------------------------------------------------------
# Run Python
# ------------------------------------------------------------

python "$PYTHON_SCRIPT"
EXIT_CODE=$?

echo

if [ "$EXIT_CODE" -eq 130 ]; then
    echo -e "${YELLOW}[!] Setup interrupted.${RESET}"
    exit 130
fi

if [ "$EXIT_CODE" -ne 0 ]; then
    echo -e "${RED}[✗] Setup finished with errors.${RESET}"
    exit "$EXIT_CODE"
fi

echo -e "${GREEN}[✓] Setup finished successfully.${RESET}"

exit 0