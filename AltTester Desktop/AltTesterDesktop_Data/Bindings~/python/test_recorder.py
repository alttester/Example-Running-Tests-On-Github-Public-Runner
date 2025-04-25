# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app
import unittest
from alttester import By, AltKeyCode, AltDriver


class MyTests(unittest.TestCase):

    quiz_tooltip_view_path = (
        "/RuntimePanelSettings/UI(Clone)-container/Quiz.TooltipView"
    )
    unity_engine_ui_elements_label_path = "/RuntimePanelSettings/UI(Clone)-container/Quiz.TooltipView/UnityEngine.UIElements.Label"

    @classmethod
    def setUp(self):
        self.alt_driver = AltDriver(
            host="127.0.0.1", port=13000, app_name="__default__"
        )
        # You might want to load the scene here
        # self.alt_driver.load_scene("Boot", True)

    @classmethod
    def tearDown(self):
        self.alt_driver.stop()

    def test(self):
        quiz_tooltip_view = self.alt_driver.wait_for_object(
            By.PATH, self.quiz_tooltip_view_path, timeout=20
        )
        unity_engine_ui_elements_label = self.alt_driver.wait_for_object(
            By.PATH, self.unity_engine_ui_elements_label_path, timeout=20
        )
        unity_engine_ui_elements_label.wait_for_visual_element_property(
            "text", "TOOLTIP_PLACEHOLDER", timeout=20, get_property_as_string=True
        )
