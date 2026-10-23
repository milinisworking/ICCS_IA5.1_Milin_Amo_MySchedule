import unittest

from schedule_manager import Schedule, ScheduleError


class ScheduleManagerTests(unittest.TestCase):
    def test_add_and_view_normal_case(self):
        schedule = Schedule()
        schedule.add_event("Database Lecture", "2026-10-26", "09:00", "10:30")

        events = [str(event) for event in schedule.events_on("2026-10-26")]

        self.assertEqual(events, ["09:00-10:30  Database Lecture"])

    def test_reject_invalid_time_range(self):
        schedule = Schedule()

        with self.assertRaisesRegex(ScheduleError, "End time must be after the start time."):
            schedule.add_event("Bad Event", "2026-10-26", "14:00", "13:00")

    def test_sort_events_by_start_time(self):
        schedule = Schedule()
        schedule.add_event("Database Lecture", "2026-10-26", "09:00", "10:30")
        schedule.add_event("Lab", "2026-10-26", "08:30", "08:45")

        events = [str(event) for event in schedule.events_on("2026-10-26")]

        self.assertEqual(events, ["08:30-08:45  Lab", "09:00-10:30  Database Lecture"])

    def test_reject_invalid_date(self):
        schedule = Schedule()

        with self.assertRaisesRegex(ScheduleError, "Invalid date"):
            schedule.add_event("Bad Date", "2026-02-30", "09:00", "10:00")

    def test_reject_overlapping_events(self):
        schedule = Schedule()
        schedule.add_event("Lecture", "2026-10-26", "09:00", "10:30")

        with self.assertRaisesRegex(ScheduleError, "overlaps another event"):
            schedule.add_event("Overlap", "2026-10-26", "10:00", "10:45")

    def test_allow_touching_events(self):
        schedule = Schedule()
        schedule.add_event("Lecture", "2026-10-26", "09:00", "10:30")
        schedule.add_event("Next Event", "2026-10-26", "10:30", "11:00")

        events = [str(event) for event in schedule.events_on("2026-10-26")]

        self.assertEqual(
            events,
            [
                "09:00-10:30  Lecture",
                "10:30-11:00  Next Event",
            ],
        )


if __name__ == "__main__":
    unittest.main()
