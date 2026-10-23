# Checks and decisions

> This file records what I checked, what actually happened, and why I accepted or changed the work.

## Concrete checks

C1 and C2 were written before implementation. C3–C6 were added later so all of R1–R3 are covered.

| Check / requirement           | Given                                                                       | When                                                                            | Expected result                                                         | Actual result / pass or fail                                                             |
| ----------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| C1 / R1, R2 — normal case     | The schedule is empty.                                                      | I add "Database Lecture" on 2026-10-26 from 09:00 to 10:30 and view 2026-10-26. | The event is added and shown as `09:00-10:30  Database Lecture`.        | Printed "Event added." and viewing the date showed `09:00-10:30  Database Lecture`. Pass |
| C2 / R3 — invalid time range  | Any schedule.                                                               | I try to add an event on 2026-10-26 from 14:00 to 13:00.                        | Rejected with a message that the end time must be after the start time. | `Error: End time must be after the start time.` and the event was not added. Pass        |
| C3 / R2 — order               | Lecture 09:00, Lunch 12:00 and Lab 10:30 added in that order on 2026-10-26. | View 2026-10-26.                                                                | Shown as Lecture, Lab, Lunch.                                           | Shown in start-time order even though Lab was added last. Pass                           |
| C4 / R3 — invalid date        | Any schedule.                                                               | Add an event on 2026-02-30.                                                     | Rejected, says the date is invalid.                                     | `Error: Invalid date: '2026-02-30'. Use YYYY-MM-DD.` Pass                                |
| C5 / R3 — overlap             | Lunch 12:00–13:00 on 2026-10-26.                                            | Add "Club meeting" 11:30–12:30 on the same date.                                | Rejected because it overlaps.                                           | `Error: This event overlaps another event on the same date.` Pass                        |
| C6 / R3 — boundary (touching) | Lecture 09:00–10:30 on 2026-10-26.                                          | Add "Lab" 10:30–12:00 on the same date.                                         | Allowed, because they only touch.                                       | Added, and both are shown. Pass                                                          |

## Two review decisions

- Plan decision: I chose a command-line program instead of a graphical calendar because it is easier to finish and test within the assignment time. I also decided that events that only touch (one ends 10:30, next starts 10:30) are allowed, because back-to-back classes are normal for students.
- Code decision: In `schedule_manager.py`, Copilot's `Event` dataclass had no `__str__`, so printing an event showed the raw dataclass text (`Event(title='Database Lecture', date=datetime.date(...)...)`) instead of `09:00-10:30  Database Lecture` like I expected in C1. I added `Event.__str__` and `.strip()` in `parse_date()`/`parse_time()`, because a stray space like " 09:00" was rejected as an invalid time. I kept Copilot's empty-title check in `Event.__post_init__` since it already covers that case.

## Automated tests

- Test file and behaviour checked: `test_schedule_manager.py` — add and view an event (C1), end time before start rejected (C2), events sorted by start time (C3), invalid date 2026-02-30 rejected (C4), overlapping event rejected (C5), touching events 09:00–10:30 and 10:30–11:00 both allowed (C6).
- Command I ran: `py -3.13 -m unittest -v`
- Final result: Ran 6 tests, OK (all passed).
- Correction and rerun, if needed: None needed. I checked each assertion matched my expected results before running.

## Realistic use and final judgment

- Task I tried: Planned my Monday 2026-10-26 with `py -3.13 main.py`: added Database Lecture 09:00–10:30, Lunch 12:00–13:00, Computer Systems Lab 10:30–12:00 and Gym 17:00–18:30. Then tried a Club meeting 11:30–12:30, a Meeting 14:00–13:00 and Group work on 2026-02-30, and viewed the day.
- Outcome: All 4 real events printed "Event added.". The club meeting was rejected for overlapping, and the other two got clear errors instead of crashing. Viewing the day showed Lecture, Lab, Lunch, Gym in time order even though I added the lab after lunch. Useful for quickly seeing one day and stopping double-booking.
- Judgment: Done. R1–R3 all work in the manual checks C1–C6 and all 6 automated tests pass.
- Remaining limitation or unfinished work: Events are not saved, so everything is lost when I quit. Also the overlap error doesn't say which event it clashes with, so on a busy day I have to view the date to find it.
