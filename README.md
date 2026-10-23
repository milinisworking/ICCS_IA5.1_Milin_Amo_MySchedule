# MySchedule

> This file explains who the project is for, what it should do, and how to run it.

## Purpose

MySchedule is a small command-line schedule manager for students who want to organize classes, assignment deadlines, appointments and other activities. It helps me see what I have planned for a particular day.

## Requirements

- R1: The user can add an event with a title, date (YYYY-MM-DD), start time and end time (HH:MM, 24-hour).
- R2: The user can view the events for a selected date, shown in start-time order.
- R3: The program must reject invalid dates or times, end times that are not after the start time, and events that overlap another event on the same date. Events that only touch (one ends at 10:30, the next starts at 10:30) are allowed.

## Setup and use

- Prerequisites: Python 3.13 or later. Only the standard library is used, nothing to install.
- Setup: Clone the repo and go into the folder.

  ```
  git clone https://github.com/milinisworking/ICCS_IA5.1_Milin_Amo_MySchedule.git
  cd ICCS_IA5.1_Milin_Amo_MySchedule
  ```

- Run: `py -3.13 main.py` (or `python main.py` if Python 3.13 is your default)
  - Choose `1` to add an event, then type the title, date, start and end time, e.g. `Database Lecture`, `2026-10-26`, `09:00`, `10:30`.
  - Choose `2` and type a date to see that day's events.
  - Choose `3` to quit. Events are only kept while the program is running.
- Run tests: `py -3.13 -m unittest -v`

## Author and acknowledgements

- Name / student ID: Milin Amornruattanadecha / 6480303
- AI tools used: GitHub Copilot for planning, implementation and review.
- External code/resources: None.

See PLAN.md for the implementation plan and EVIDENCE.md for results and decisions.
