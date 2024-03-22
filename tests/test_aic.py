import unittest
from aic import load_character, AICharacter

class TestDownloadAndValidateCharacterLive(unittest.TestCase):
    def test_live_deserialization(self):
        key = "datetime"

        # Call the function with the actual GCS path
        character = load_character(key)

        # Verify the type of the returned object
        # Add additional assertions based on the expected content of your JSON
        self.assertIsInstance(character, AICharacter)
        # Example assertion: check if the version field matches expected value
        self.assertEqual(character.version, "1.0")

if __name__ == '__main__':
    unittest.main()