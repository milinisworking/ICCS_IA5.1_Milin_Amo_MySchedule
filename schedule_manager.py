"""Core scheduling logic for MySchedule."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time


class ScheduleError(ValueError):
    """Raised when schedule data is invalid."""


def parse_date(value: str) -> date:
    """Parse a date string in YYYY-MM-DD format."""
    if not isinstance(value, str):
        raise ScheduleError("Date must be provided as a string in YYYY-MM-DD format.")

    try:
        return datetime.strptime(value.strip(), "%Y-%m-%d").date()
    except ValueError as exc:
        raise ScheduleError(f"Invalid date: {value!r}. Use YYYY-MM-DD.") from exc


def parse_time(value: str) -> time:
    """Parse a time string in HH:MM 24-hour format."""
    if not isinstance(value, str):
        raise ScheduleError("Time must be provided as a string in HH:MM format.")

    try:
        return datetime.strptime(value.strip(), "%H:%M").time()
    except ValueError as exc:
        raise ScheduleError(f"Invalid time: {value!r}. Use HH:MM in 24-hour format.") from exc


@dataclass(frozen=True)
class Event:
    title: str
    date: date
    start: time
    end: time

    def __post_init__(self) -> None:
        if not isinstance(self.title, str) or not self.title.strip():
            raise ScheduleError("Event title cannot be empty.")
        if not isinstance(self.date, date):
            raise ScheduleError("Event date must be a date object.")
        if not isinstance(self.start, time):
            raise ScheduleError("Event start must be a time object.")
        if not isinstance(self.end, time):
            raise ScheduleError("Event end must be a time object.")

    def __str__(self) -> str:
        return f"{self.start.strftime('%H:%M')}-{self.end.strftime('%H:%M')}  {self.title}"


class Schedule:
    """Stores events for a schedule."""

    def __init__(self) -> None:
        self.events: list[Event] = []

    def add_event(
        self,
        title: str,
        event_date: str | date,
        start: str | time,
        end: str | time,
    ) -> Event:
        """Add an event after parsing the date and time values."""
        parsed_date = parse_date(event_date) if isinstance(event_date, str) else event_date
        parsed_start = parse_time(start) if isinstance(start, str) else start
        parsed_end = parse_time(end) if isinstance(end, str) else end

        if not isinstance(parsed_date, date):
            raise ScheduleError("Event date must be a valid date value.")
        if not isinstance(parsed_start, time):
            raise ScheduleError("Event start time must be a valid time value.")
        if not isinstance(parsed_end, time):
            raise ScheduleError("Event end time must be a valid time value.")
        if parsed_end <= parsed_start:
            raise ScheduleError("End time must be after the start time.")

        for existing in self.events:
            if existing.date != parsed_date:
                continue
            if parsed_start < existing.end and existing.start < parsed_end:
                raise ScheduleError("This event overlaps another event on the same date.")

        event = Event(title=title.strip(), date=parsed_date, start=parsed_start, end=parsed_end)
        self.events.append(event)
        return event

    def events_on(self, date_text: str) -> list[Event]:
        """Return all events for a date, sorted by start time."""
        target_date = parse_date(date_text)
        matching_events = [event for event in self.events if event.date == target_date]
        return sorted(matching_events, key=lambda event: (event.start.hour, event.start.minute))