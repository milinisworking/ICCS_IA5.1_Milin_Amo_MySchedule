# Implementation plan

> This file records my project-specific steps reviewed before coding. Refers to R1–R3 in README.md.

## Steps

1. Create `main.py` for the command-line menu and user input, and a separate `schedule_manager.py` for the `Event` and `Schedule` classes and the scheduling rules.
2. Implement `Schedule.add_event()` in `schedule_manager.py` and connect it to menu option 1 in `main.py` (R1).
3. Implement `Schedule.events_on()` to return the events for one date sorted by start time, and connect it to menu option 2 (R2).
4. Add validation in `add_event()` (R3): parse the date and times with `datetime.strptime` so dates like 2026-02-30 are rejected, reject end time <= start time, and reject events that overlap another event on the same date. Use the rule `new.start < other.end and other.start < new.end` so events that only touch end-to-start are allowed. Errors are raised as `ScheduleError` and `main.py` prints the message.
5. Create `test_schedule_manager.py` with `unittest` tests for C1 and C2 from EVIDENCE.md plus sorting, invalid date, overlap and the touching boundary. Run with `py -3.13 -m unittest -v`.
6. Try a realistic university day: add a lecture, lab, lunch and gym on 2026-10-26, view the day, then try adding a conflicting club meeting.

## Later changes, if any

None
