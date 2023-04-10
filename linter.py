"""SublimeLinter plugin that provides an interface to rflint

https://pypi.org/project/robotframework-lint/."""

import logging
from SublimeLinter.lint import PythonLinter


logger = logging.getLogger('SublimeLinter.plugins.robot')


class Robotlint(PythonLinter):  # pylint: disable=R0903
    """Python Linter sub-class for rflint."""

    # Example return => W: 1, 0: Line has trailing whitespace (TrailingWhitespace)
    regex = r'^(?P<warn>\w): (?P<line>\d+), (?P<col>\d+): (?P<message>.*) \((?P<code>.*)\)$'
    multiline = False

    # http://www.sublimelinter.com/en/stable/linter_attributes.html#tempfile-suffix-1
    tempfile_suffix = '-' # rflint doesn't accept from stdin

    # --error RULENAME, -e RULENAME
    #                     Assign a severity of ERROR to the given RULENAME
    # --ignore RULENAME, -i RULENAME
    #                     Ignore the given RULENAME
    # --warning RULENAME, -w RULENAME
    #                     Assign a severity of WARNING for the given RULENAME
    # --rulefile RULEFILE, -R RULEFILE
    #                     import additional rules from the given RULEFILE
    # --argumentfile ARGUMENTFILE, -A ARGUMENTFILE
    #                     read arguments from the given file

    defaults = {
        'selector': 'source.robot',
        # args
        '--error:': '',
        '--ignore:': '',
        '--warning:': '',
        '--rulefile:': '',
        '--argumentfile:': ''

    }

    def cmd(self):
        """Default command."""
        # --no-filenames        suppress the printing of filenames
        return (
            'rflint',
            "--no-filenames",
            '${args}',
            '${file_on_disk}'
        )


    def on_stderr(self, stderr):
        """Display error message when there is an error."""
        if stderr:
            self.notify_failure()
            logger.error(stderr)
