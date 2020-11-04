<p align="center">
Meta package that installs group of ergonomic xontribs in xonsh shell.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## Xontribs

* [argcomplete](https://github.com/anki-code/xontrib-argcomplete) - Tab completion of python and xonsh scripts.
* [back2dir](https://github.com/anki-code/xontrib-back2dir) - Return to the most recently used directory when starting xonsh shell.
* [onepath](https://github.com/anki-code/xontrib-onepath) - Associate files with app and run it without preceding commands.
* [output_search](https://github.com/tokenizer/xontrib-output-search) -  Get words from the previous command output for the next command.
* [pipeliner](https://github.com/anki-code/xontrib-pipeliner) - Let your pipe lines flow thru the Python code.
* [prompt_bar](https://github.com/anki-code/xontrib-prompt-bar) - The bar prompt for xonsh shell with customizable sections. 
* [sh](https://github.com/anki-code/xontrib-sh) - Paste and run commands from bash, zsh, fish, tcsh in xonsh shell.

## Developers extra

* [xontrib-hist-format](https://github.com/anki-code/xontrib-hist-format) - Format xonsh history to post it to Github or another page.

## Installation

To install use pip:

```bash
xpip install xontrib-ergopack
# or for developers extra: xpip install xontrib-ergopack[dev]
# or: xpip install -U git+https://github.com/anki-code/xontrib-ergopack
```

## Usage
To load all xontribs from the pack just load the pack xontrib:
```bash
xontrib load ergopack
```

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).