from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from c1_2_quality.__main__ import validate  # noqa: E402


class QualityTests(unittest.TestCase):
    def test_manifest_is_consistent(self) -> None:
        self.assertEqual(validate(ROOT), [])


if __name__ == "__main__":
    unittest.main()
