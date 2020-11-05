<p align="center">
Meta package that installs group of ergonomic xontribs in xonsh shell.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## xontribs: default

```bash
xpip install -U xontrib-ergopack
```

* [argcomplete](https://github.com/anki-code/xontrib-argcomplete) - Tab completion of python and xonsh scripts.
* [back2dir](https://github.com/anki-code/xontrib-back2dir) - Return to the most recently used directory when starting xonsh shell.
* [onepath](https://github.com/anki-code/xontrib-onepath) - Associate files with app and run it without preceding commands.
* [output_search](https://github.com/tokenizer/xontrib-output-search) -  Get words from the previous command output for the next command.
* [pipeliner](https://github.com/anki-code/xontrib-pipeliner) - Let your pipe lines flow thru the Python code.
* [sh](https://github.com/anki-code/xontrib-sh) - Paste and run commands from bash, zsh, fish, tcsh in xonsh shell.

## xontribs: prompt

```bash
xpip install -U xontrib-ergopack[prompt]
```

* All default xontribs.
* [prompt_bar](https://github.com/anki-code/xontrib-prompt-bar) - The bar prompt for xonsh shell with customizable sections. 

## xontribs: dev

```bash
xpip install -U xontrib-ergopack[dev]
```

* All default xontribs.
* [hist_format](https://github.com/anki-code/xontrib-hist-format) - Format xonsh history to post it to Github or another page.

## xontribs all

```bash
xpip install -U xontrib-ergopack[prompt,dev]
```

* Install all ergonomic xontribs.

## Usage

Load default xontribs:
```bash
xontrib load ergopack
```

## Credits

* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
* Ergopack is compatible with [dotfiles plugin](https://github.com/xxh/xxh-plugin-prerun-dotfiles#preinstall-pypi-packages) 
for [xxh](https://github.com/xxh/xxh) - bring your favorite shell wherever you go through the ssh. 