<p align="center">
Meta package that installs group of ergonomic xontribs in xonsh shell.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## Default xontribs

By default ergopack contains xontribs that do not change the prompt or commands processing. 
The xontribs that do more significant changes are in PyPi "extras".

```bash
xpip install -U xontrib-ergopack
```

* [back2dir](https://github.com/anki-code/xontrib-back2dir) - Return to the most recently used directory when starting xonsh shell.
* [argcomplete](https://github.com/anki-code/xontrib-argcomplete) - Tab completion of python and xonsh scripts.
* [output_search](https://github.com/tokenizer/xontrib-output-search) -  Get words from the previous command output for the next command.
* [pipeliner](https://github.com/anki-code/xontrib-pipeliner) - Let your pipe lines flow thru the Python code.
* [sh](https://github.com/anki-code/xontrib-sh) - Paste and run commands from bash, zsh, fish, tcsh in xonsh shell.
* [autoxsh](https://github.com/Granitosaurus/xonsh-autoxsh) - Automatically execution of `.autoxsh` xonsh script after entering into the directory. Not activated by default.
* [history_encrypt](https://github.com/anki-code/xontrib-history-encrypt) - History backend that can encrypt the xonsh shell commands history. Not activated by default.
* [xontrib-clp](https://github.com/anki-code/xontrib-clp) - Copy output to clipboard. Cross-platform. 
* [xontrib-cmd-durations](https://github.com/jnoortheen/xontrib-cmd-durations) - Show long running commands durations in prompt with option to send notification when terminal is not focused. 

## Onepath xontribs

```bash
xpip install -U 'xontrib-ergopack[onepath]'
```

* [onepath](https://github.com/anki-code/xontrib-onepath) - Associate files with app and run it without preceding commands.
* All default xontribs.

## Prompt xontribs

```bash
xpip install -U 'xontrib-ergopack[prompt]'
```

* [prompt_bar](https://github.com/anki-code/xontrib-prompt-bar) - The bar prompt for xonsh shell with customizable sections. 
* [prompt_starship](https://github.com/anki-code/xontrib-prompt-starship) - Starship cross-shell prompt in xonsh shell. 
* All default xontribs.

## Dev xontribs

```bash
xpip install -U 'xontrib-ergopack[dev]'
```

* [hist_format](https://github.com/anki-code/xontrib-hist-format) - Format xonsh history to post it to Github or another page.
* [readable-traceback](https://github.com/vaaaaanquish/xontrib-readable-traceback) - Make traceback readable and colorized.
* [hunter](https://github.com/ionelmc/python-hunter) - A flexible code tracing toolkit. [How to use with xonsh](https://github.com/xonsh/xonsh/issues/4125#issuecomment-787462951). 
* All default xontribs.

## All xontribs

```bash
xpip install -U 'xontrib-ergopack[onepath,prompt,dev]'
```

## Usage

Load default xontribs:
```bash
xontrib load ergopack
```

## Links

* [xonsh-cheatsheet](https://github.com/anki-code/xonsh-cheatsheet) - Cheat sheet for xonsh shell with copy-pastable examples. The best doc for the new users. 
* [xontrib-rc-awesome](https://github.com/anki-code/xontrib-rc-awesome) - Awesome snippets of code for xonshrc in xonsh shell. 
* Ergopack is compatible with [dotfiles plugin](https://github.com/xxh/xxh-plugin-prerun-dotfiles#preinstall-pypi-packages) 
for [xxh](https://github.com/xxh/xxh) - bring your favorite shell wherever you go through the ssh. 
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
* [Get more xontribs for xonsh on Github](https://github.com/topics/xontrib)
