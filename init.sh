$(export PYENV_ROOT="$HOME/.pyenv")

$(export PATH="~/.pyenv/bin:$PATH")

$(eval "$(pyenv init -)")

$(eval "$(pyenv virtualenv-init -)")

$(pyenv versions)

$(pyenv local 3.11.9)

$(pyenv shell 3.11.9)
