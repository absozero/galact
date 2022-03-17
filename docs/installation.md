# Installation

Installing this bot can be done with either pip, pipx, pipenv, poetry, or any other pypi-compatible dependency management solution.
## Easy installation
For the stable branch:
```bash
pip install git+https://github.com/absozero/galact.git
```
And for the unstable branch:
```bash
pip install git+https://github.com/absozero/galact.git@Testing
```
- Make sure to have python and pip installed, and both added to the system PATH, whether on a UNIX-based on NT(windows)-based system.


## The longer but safer way
 You can choose to create a [virtual environment](https://docs.python.org/3/library/venv.html), which isolates the interpreter and its packages and commands so packages and their versions don't go and interfere with other packages and cause a mess. This is smart since it isolates the package and it is almost completely future-proof

- This is almost 100% necessary if you are using linux with the built in python3 interpreter, since installing packages directly without could mess up system packages.

### Virtual environment
You can create a virtual environment with `venv` if you want to use the built in pip
```bash
(win) C:/ python -m venv venv
(lin) ~$ python3 -m venv venv
```

Then, on windows, you would run:
```
cmd C/> (venv path)\Scripts\Activate.bat
PS ~ (venv path)\Scripts\Activate.ps1
```

On linux, with bash/zsh, run:
```bash
 source (venv path)/bin/activate
```

For most other shells the venv can run on, please check the [venv documentation](https://docs.python.org/3/library/venv.html)

### Other tools

The other tools mentioned, such as pipenv, pipx, poetry, create a virtual environment automatically.

**Pipx is recommended because its default job is to install and use CLI packages and add them to the PATH. This means that galact will still be globally accessible without accessing from inside the virtual environment, so if you boot a shell and type in galact, it will work.**
- Pipx syntax is extremely similar to pip syntax

To install any of these tools, inluding `pipx`, use pip from a regular shell that is not in a virtual environment.

```bash
pip install (tool)
```
### Installing into virtual environment
Now, once the virtual environment or tool is set up or installed, install galact.

With pip use:
- For the stable branch:
```bash
pip install git+https://github.com/absozero/galact.git
```
- For the unstable branch:
```bash
pip install git+https://github.com/absozero/galact.git@Testing
```

For something like pipx use:
(Remember, pipx should be run outside of any python virtual environment)
For the stable branch:
```bash
pipx install git+https://github.com/absozero/galact.git
```
And for the unstable branch:
```bash
pipx install git+https://github.com/absozero/galact.git
```
