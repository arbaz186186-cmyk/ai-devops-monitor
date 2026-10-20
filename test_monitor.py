import unittest
from monitor import check_logs


class TestMonitor(unittest.TestCase):

    def test_error_count(self):
        logs = "INFO: Server started\nERROR: Database failed"
        errors, warnings = check_logs(logs)

        self.assertEqual(errors, 1)
        self.assertEqual(warnings, 0)

    def test_warning_count(self):
        logs = "WARNING: Memory high\nWARNING: CPU high"
        errors, warnings = check_logs(logs)

        self.assertEqual(errors, 0)
        self.assertEqual(warnings, 2)

    def test_no_errors_or_warnings(self):
        logs = "INFO: Server started successfully"
        errors, warnings = check_logs(logs)

        self.assertEqual(errors, 0)
        self.assertEqual(warnings, 0)


if __name__ == "__main__":
    unittest.main()
