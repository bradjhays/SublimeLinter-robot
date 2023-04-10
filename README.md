SublimeLinter-robot
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [rflint](https://pypi.org/project/robotframework-lint/).
It will be used with files that have the "robot" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `rflint` (1.1 or later) is installed on your system.
To install `rflint`, do the following:

```
pip install robotframework-lint
```
Please make sure that the path to `rflint` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Installation method 2 (developer)
clone this repo anywhere you want `~/sublimelinter-robot` for example

see Sublime Settings -> browse packages, for the correct path

for Mac
```
$ ln -s ~/sublimelinter-robot ~/Library/Application\ Support/Sublime\ Text/Packages/
```
for Ubuntu
```
$ ln -s ~/sublimelinter-robot ~/.config/sublime-text/
```

then restart sublime to pick up the new package


## Config

Add robot to you SublimeLinter settings -> linters
```
{
    "linters": {
        "robotlint":{
            "disable": false,
            "executable": "rflint",
            "lint_mode": "load_save",
            "selector": "source.robot",
            "ignore": ["LineTooLong"]
        },
        ...
    }
    ...
}
```


## rlint
For Reference... Not all options are currently supported, see `linter.py` for supported in 'defaults'
```
usage: python -m rflint [-h] [--error RULENAME] [--ignore RULENAME] [--warning RULENAME] [--list] [--describe] [--no-filenames] [--format FORMAT]
                        [--version] [--verbose] [--configure CONFIGURE] [--recursive] [--rulefile RULEFILE] [--argumentfile ARGUMENTFILE]
                        ...

A static analyzer for robot framework plain text files.

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  --error RULENAME, -e RULENAME
                        Assign a severity of ERROR to the given RULENAME
  --ignore RULENAME, -i RULENAME
                        Ignore the given RULENAME
  --warning RULENAME, -w RULENAME
                        Assign a severity of WARNING for the given RULENAME
  --list, -l            show a list of known rules and exit
  --describe, -d        describe the given rules
  --no-filenames        suppress the printing of filenames
  --format FORMAT, -f FORMAT
                        Define the output format
  --version             Display version number and exit
  --verbose, -v         Give verbose output
  --configure CONFIGURE, -c CONFIGURE
                        Configure a rule
  --recursive, -r       Recursively scan subfolders in a directory
  --rulefile RULEFILE, -R RULEFILE
                        import additional rules from the given RULEFILE
  --argumentfile ARGUMENTFILE, -A ARGUMENTFILE
                        read arguments from the given file

You can use 'all' in place of RULENAME to refer to all rules. 

For example: '--ignore all --warn DuplicateTestNames' will ignore all
rules except DuplicateTestNames.

FORMAT is a string that performs a substitution on the following 
patterns: {severity}, {linenumber}, {char}, {message}, and {rulename}.

For example: --format 'line: {linenumber}: message: {message}'. 

ARGUMENTFILE is a filename with contents that match the format of 
standard robot framework argument files

If you give a directory as an argument, all files in the directory
with the suffix .txt, .robot, .resource, or .tsv will be processed. 
With the --recursive option, subfolders within the directory will 
also be processed.
```