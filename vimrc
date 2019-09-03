
set ttimeoutlen=50 "removes lag while switching between different modes"
set nu
set rnu
set nocompatible
set signcolumn=yes
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'nightsense/cosmic_latte'
"Plugin 'Valloric/YouCompleteMe'
Plugin 'ervandew/supertab'
let g:SuperTabMappingForward = '<S-tab>' "maps autocomplete to shift-tab
let g:SuperTabMappingBackward = '<S-tab>'
let g:SuperTabMappingTabLiteral = '<tab>' "to set tab back to its original setting

Plugin 'jiangmiao/auto-pairs'
Plugin 'scrooloose/nerdcommenter'
let g:ycm_global_ycm_extra_conf = '$HOME/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'

Plugin 'Chiel92/vim-autoformat'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'w0rp/ale'
Plugin 'scrooloose/nerdtree'
Plugin 'itchyny/lightline.vim'
set laststatus=2
Plugin 'yegappan/mru'
Plugin 'tpope/vim-eunuch'
Plugin 'tpope/vim-surround'
Plugin 'mattn/emmet-vim'
Plugin 'wesQ3/vim-windowswap'
Plugin 'francoiscabrol/ranger.vim'
Plugin 'SirVer/ultisnips'
call vundle#end()
filetype plugin indent on

set cindent


set backspace=indent,eol,start

let g:netrw_browse_split=4

"Mappings
map –  <Plug>NERDCommenterToggle
vmap –   <Plug>NERDCommenterToggle<CR>gv
"tnoremap <Esc> <C-\><C-n>:q!<CR>

tnoremap <C-l> <C-w>l
tnoremap <C-k> <C-w>k
tnoremap <C-j> <C-w>j
tnoremap <C-h> <C-w>h

nnoremap <C-l> <C-w>l
nnoremap <C-k> <C-w>k
nnoremap <C-j> <C-w>j
nnoremap <C-h> <C-w>h
noremap <C-n> :NERDTreeToggle<CR>
map <C-i> :Autoformat<CR> 
map m :MRUToggle<CR> 
noremap ® <C-w>H "Option - r
noremap ‰ <C-w>J "Option Shift r
set bg=dark
colo cosmic_latte

filetype plugin indent on
set guifont=Monaco:h18

syntax on
