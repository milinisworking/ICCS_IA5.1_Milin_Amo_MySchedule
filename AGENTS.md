# Instructions for this repository

> This file tells the coding agent how to work on this project. It does not replace the requirements or plan.

- Read README.md, PLAN.md and the checks in EVIDENCE.md before implementing.
- Keep changes within requirements R1–R3 in README.md.
- Use Python 3.13 or later and only the Python standard library.
- Keep event validation and overlap checking in `schedule_manager.py`, separate from the command-line interface in `main.py`, so the rules are easier to test. `schedule_manager.py` should not use `input()` or `print()`.
- Keep the interface simple and explain errors clearly to the user. A wrong input should show an error message, not crash the program.
- Use small changes and avoid adding features that are not needed for the three requirements.
- Run tests with: `py -3.13 -m unittest -v`
- Do not change an expected result merely to make a test pass. Raise any disagreement for review.
- Leave requirements, expected results, review decisions and the final judgment for me to write.
