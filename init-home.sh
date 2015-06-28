echo "Create symlinks to configuration files:"
ln -sfv ~/dotfiles/_xprofile ~/.xprofile
ln -sfv ~/dotfiles/_bashrc ~/.bashrc
ln -sfv ~/dotfiles/_bash_aliases ~/.bash_aliases
ln -sfv ~/dotfiles/_i3_config ~/.i3/config
ln -sfv ~/dotfiles/_vimrc ~/.vimrc

echo
echo "Create symlinks to some useful scripts:"
ln -sfv ~/scripts/display-adjust.sh ~/bin/display-adjust
ln -sfv ~/scripts/asciidoc2pdf.py ~/bin/a2pdf

