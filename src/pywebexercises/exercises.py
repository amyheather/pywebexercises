"""Web exercises.

Credit:
    > This is based on R webexercises package by Dale Barr and Lisa DeBruine
    (https://github.com/PsyTeachR/webexercises).

Licence:
    This project is licensed under the CC BY-SA 4.0 licence.
"""
import random
import string
from IPython.core.display import HTML


def mcq(opts):
    """
    Create a multiple-choice question (MCQ) with a drop down.

    Arguments:
        opts (dict)
            Dictionary where keys are answers and values are 0 if wrong
            answer and 1 if right answer.
    """
    # Check for a correct answer.
    if 1 not in opts.values():
        raise ValueError('MCQ has no correct answer')

    # Convert 1 to "answer"
    opts = {key: ("answer" if value == 1 else value)
            for key, value in opts.items()}

    # Convert to HTML
    options_html = ''.join(
        [f"<option value='{value}'>{key}</option>"
         for key, value in opts.items()])
    html = ("<select class='webex-select'><option value='blank'>" +
            f"</option>{options_html}</select>")

    # Print as raw HTML
    return HTML(html)


def longmcq(opts):
    """
    Create a multiple-choice question (MCQ) with radio buttons.

    Arguments:
        opts (dict)
            Dictionary where keys are answers and values are 0 if wrong
            answer and 1 if right answer.
    """
    # Check for a correct answer.
    if 1 not in opts.values():
        raise ValueError('MCQ has no correct answer')

    # Convert 1 to "answer"
    opts = {key: ("answer" if value == 1 else value)
            for key, value in opts.items()}

    # Generate a random name for the radio group
    qname = "radio_" + "".join(random.choices(string.ascii_uppercase, k=10))

    # Create radio button options
    options = [
        (f'<label><input type="radio" autocomplete="off" name="{qname}" ' +
         f'value="{value}"></input> <span>{key}</span></label>')
        for key, value in opts.items()
    ]

    # Generate HTML output
    html = (f"<div class='webex-radiogroup' id='{qname}'>" +
            "".join(options) + "</div>\n")

    # Print as raw HTML
    return HTML(html)


def torf(answer):
    """
    Creates a true-or-false question.

    Arguments:
        answer (boolean)
            Either set to True or False.
    """
    # Verify that user has provided either True or False
    if not isinstance(answer, bool):
        raise ValueError('Must set to True or False.')

    # Create options list of True or False, marking answer
    opts = {True: 0, False: 0}
    opts[answer] = 1

    # Return MCQ rendering of the true or false options
    return mcq(opts)
