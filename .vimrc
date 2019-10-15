
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

Plugin 'lervag/vimtex'

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

" -----------------------------------------------------------------------------
"  VIMTEX OPTIONS
"  ----------------------------------------------------------------------------
if has('unix')
if has('mac')
let g:vimtex_view_method = "skim"
let g:vimtex_view_general_viewer
\ = '/Applications/Skim.app/Contents/SharedSupport/displayline'
let g:vimtex_view_general_options = '-r @line @pdf @tex'
        " This adds a callback hook that updates Skim after compilation
let g:vimtex_compiler_callback_hooks = ['UpdateSkim']
function! UpdateSkim(status)
if !a:status | return | endif
let l:out = b:vimtex.out()
let l:tex = expand('%:p')
let l:cmd = [g:vimtex_view_general_viewer, '-r']
if !empty(system('pgrep Skim'))
call extend(l:cmd, ['-g'])
endif
if has('nvim')
call jobstart(l:cmd + [line('.'), l:out, l:tex])
elseif has('job')
call job_start(l:cmd + [line('.'), l:out, l:tex])
else
call system(join(l:cmd + [line('.'), shellescape(l:out), shellescape(l:tex)], ' '))
endif
endfunction
else
let g:latex_view_general_viewer = "zathura"
let g:vimtex_view_method = "zathura"
endif
elseif has('win32')
endif
let g:tex_flavor = "latex"
let g:vimtex_quickfix_open_on_warning = 0
let g:vimtex_quickfix_mode = 2
if has('nvim')
let g:vimtex_compiler_progname = 'nvr'
endif
" One of the neosnippet plugins will conceal symbols in LaTeX which is
" confusing
let g:tex_conceal = ""
" Can hide specifc warning messages from the quickfix window
" Quickfix with Neovim is broken or something
" https://github.com/lervag/vimtex/issues/773
let g:vimtex_quickfix_latexlog = {
\ 'default' : 1,
\ 'fix_paths' : 0,
\ 'general' : 1,
\ 'references' : 1,
\ 'overfull' : 1,
\ 'underfull' : 1,
\ 'font' : 1,
\ 'packages' : {
\   'default' : 1,
\   'natbib' : 1,
\   'biblatex' : 1,
\   'babel' : 1,
\   'hyperref' : 1,
\   'scrreprt' : 1,
\   'fixltx2e' : 1,
\   'titlesec' : 1,
\ },
\}

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
