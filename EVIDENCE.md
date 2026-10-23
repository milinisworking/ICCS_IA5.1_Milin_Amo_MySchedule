# Checks and decisions

> This file records what I checked, what actually happened, and why I accepted or changed the work.

## Concrete checks

| Check / requirement          | Given                  | When                                                                            | Expected result                                                         | Actual result / pass or fail |
| ---------------------------- | ---------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------- |
| C1 / R1, R2 — normal case    | The schedule is empty. | I add "Database Lecture" on 2026-10-26 from 09:00 to 10:30 and view 2026-10-26. | The event is added and shown as `09:00-10:30  Database Lecture`.        | Not run yet                  |
| C2 / R3 — invalid time range | Any schedule.          | I try to add an event on 2026-10-26 from 14:00 to 13:00.                        | Rejected with a message that the end time must be after the start time. | Not run yet                  |

## Two review decisions

- Plan decision: Not yet.
- Code decision: Not yet.

## Automated tests

Not done yet.

## Realistic use and final judgment

Not done yet.
