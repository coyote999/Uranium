import unittest
from UM.Settings.Setting import Setting
from UM.Settings.SettingsCategory import SettingsCategory
from UM.Settings.MachineSettings import MachineSettings
class SettingTest(unittest.TestCase):
    def setUp(self):
        # Called before the first testfunction is executed
        self._setting = Setting('TestSetting',10,'int')
        self._machine_settings = MachineSettings()
        category = SettingsCategory('TestCategory')
        #category.addSetting(self._setting)
        self._machine_settings.addSettingsCategory(category)
        self._machine_settings.loadSettingsFromFile("tests/Settings/SettingData.json")
        

    def tearDown(self):
        # Called after the last testfunction was executed
        pass

    def test_GetSettingByKey(self):
        self.assertEqual(self._machine_settings.getSettingByKey('TestSetting').getType(), self._setting.getType())
        self.assertEqual(self._machine_settings.getSettingByKey('TestSetting').getDefaultValue(), self._setting.getDefaultValue())
        pass

    def test_Category(self):
        pass

    def test_ValidatorTest(self):
        pass

if __name__ == "__main__":
    unittest.main()
