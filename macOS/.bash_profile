export LC_ALL=en_US.UTF-8  
export LANG=en_US.UTF-8

export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=2
export LSCOLORS=gxBxhxDxfxhxhxhxhxcxcx

alias ls='ls -GFh'
alias c='clear'
alias g='googler'
alias sm='/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/save.sh'
alias dm='/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/download.sh'
alias o='open'

/users/Ahish/Desktop/Ahish/Scripts/sizeupLauncher/opensizeUp.sh
/users/Ahish/Desktop/Ahish/Scripts/trialRestarter/checkWhenToRun.sh

[ -f /usr/local/etc/profile.d/autojump.sh ] && . /usr/local/etc/profile.d/autojump.sh
[[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && . "/usr/local/etc/profile.d/bash_completion.sh"

export PATH="$PATH:$HOME/Library/Python/2.7/bin"
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /Users/ahish/Library/Python/2.7/lib/python/site-packages/powerline/bindings/bash/powerline.sh

#export HISTSIZE=5000

# HSTR configuration - add this to ~/.bashrc
alias h=hstr                    # hh to be alias for hstr
export HSTR_CONFIG=hicolor       # get more colors
shopt -s histappend              # append new history items to .bash_history
export HISTCONTROL=ignorespace   # leading space hides commands from history
export HISTFILESIZE=10000        # increase history file size (default is 500)
export HISTSIZE=${HISTFILESIZE}  # increase history size (default is 500)
# ensure synchronization between Bash memory and history file
export PROMPT_COMMAND="history -a; history -n; ${PROMPT_COMMAND}"
# if this is interactive shell, then bind hstr to Ctrl-r (for Vi mode check doc)
if [[ $- =~ .*i.* ]]; then bind '"\C-r": "\C-a hstr -- \C-j"'; fi
# if this is interactive shell, then bind 'kill last command' to Ctrl-x k
if [[ $- =~ .*i.* ]]; then bind '"\C-xk": "\C-a hstr -k \C-j"'; fi

cdf() {
    target=`osascript -e 'tell application "Finder" to if (count of Finder windows) > 0 then get POSIX path of (target of front Finder window as text)'`
    if [ "$target" != "" ]; then
        cd "$target"; pwd
    else
        echo 'No Finder window found' >&2
    fi
}

