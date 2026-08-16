# ==============================
# BASIC PATH
# ==============================

[ -d "$HOME/.my_bin" ] && export PATH="$HOME/.my_bin:$PATH"
[ -d "$HOME/.local/bin" ] && export PATH="$HOME/.local/bin:$PATH"

export PATH="$HOME/bin:/usr/local/bin:$PATH"


# ==============================
# LOCALE
# ==============================

export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8


# ==============================
# OH MY ZSH
# ==============================

export ZSH="$HOME/.oh-my-zsh"


# ==============================
# THEME
# ==============================

if [ -d "$ZSH/custom/themes/powerlevel10k" ]; then
	ZSH_THEME="powerlevel10k/powerlevel10k"
else
	ZSH_THEME="robbyrussell"
fi


# ==============================
# PLUGINS
# ==============================

plugins=(
	git
	zsh-autosuggestions
	zsh-syntax-highlighting
)


# ==============================
# OH MY ZSH LOAD
# ==============================

if [ -f "$ZSH/oh-my-zsh.sh" ]; then
	source "$ZSH/oh-my-zsh.sh"
fi


# ==============================
# CUSTOM ALIASES
# ==============================

# Added to the folder $ZSH_CUSTOM/aliases/
# Add as abc.zsh, git.zsh , system.zsh,  docker.zsh 
# Load only if file exists (no error)

if [ -d "$ZSH_CUSTOM/aliases" ]; then
	for file in "$ZSH_CUSTOM"/aliases/*.zsh; do
		[ -f "$file" ] && source "$file"
	done
fi


# ==============================
# HISTORY
# ==============================

HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history
HIST_STAMPS="dd.mm.yyyy"


# ==============================
# OH MY ZSH UPDATE
# ==============================

zstyle ':omz:update' mode reminder
# For no auto update (maximum stability)
# zstyle ':omz:update' mode disabled

# For auto update (not recommended for low device)
# zstyle ':omz:update' mode auto


# ==============================
# PERFORMANCE TWEAKS (LOW RAM FRIENDLY)
# ==============================
# Disable command correction (faster startup)
#DISABLE_CORRECTION="true"

# Faster git status (very useful on slow device)
DISABLE_UNTRACKED_FILES_DIRTY="true"

setopt AUTO_PUSHD
setopt AUTO_CD
setopt PUSHD_IGNORE_DUPS
setopt PUSHD_SILENT

export PUSHD_MAX=15


# ==============================
# OPTIONAL
# ==============================
# ==============================
# HIGH-END / ADVANCED FEATURES (COMMENTED)
# Uncomment only if device is powerful
# ==============================


# Case sensitive completion (advanced users)
# CASE_SENSITIVE="true"

# Better completion waiting dots (visual feature)
# COMPLETION_WAITING_DOTS="true"

# Custom editor (if using vim/nvim)
# export EDITOR='vim'

# Custom MANPATH (advanced users)
# export MANPATH="/usr/local/man:$MANPATH"