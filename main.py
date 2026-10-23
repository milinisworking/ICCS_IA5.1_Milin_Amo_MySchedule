"""Command-line interface for MySchedule."""

from __future__ import annotations

from schedule_manager import Schedule, ScheduleError


def main() -> None:
    """Run the CLI menu loop."""
    schedule = Schedule()

    while True:
        print("\nMySchedule")
        print("1. Add event")
        print("2. View events for a date")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Event title: ").strip()
            event_date = input("Date (YYYY-MM-DD): ").strip()
            start_time = input("Start time (HH:MM): ").strip()
            end_time = input("End time (HH:MM): ").strip()

            try:
                schedule.add_event(title, event_date, start_time, end_time)
                print("Event added.")
            except ScheduleError as exc:
                print(f"Error: {exc}")

        elif choice == "2":
            event_date = input("Date to view (YYYY-MM-DD): ").strip()
            try:
                events = schedule.events_on(event_date)
                if not events:
                    print("No events found.")
                else:
                    for event in events:
                        print(event)
            except ScheduleError as exc:
                print(f"Error: {exc}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
