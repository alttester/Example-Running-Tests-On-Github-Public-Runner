# # For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app
# # import unittest
# # from alttester import By, AltKeyCode, AltDriver


# # class TestGiuli2(unittest.TestCase):

# #     @classmethod
# #     def setUp(self):
# #         self.alt_driver = AltDriver(host="192.168.2.110", port=13000, app_name="__default__")

# #     # You might want to load the scene here
# #     #   self.altdriver.load_scene("Scene 1 AltDriverTestScene", True)

# #     @classmethod
# #     def tearDown(self):
# #         self.alt_driver.stop()

# # def test(self):
# # PlasteredWall = self.altdriver.wait_for_object(
# #     By.PATH, "/IndustrialWarehouse03(Clone)/Decorations/PlasteredWall02 (1)"
# # )
# # PlasteredWall.wait_for_component_property(
# #     "UnityEngine.MeshFilter",
# #     "name",
# #     "PlasteredWall02 (1)",
# #     "UnityEngine.CoreModule",
# #     1,
# #     get_property_as_string=True,
# # )

# # Text = self.altdriver.wait_for_object(By.PATH, "/Canvas/UIButton/Text")
# # Text.wait_for_component_property(
# #     "UnityEngine.UI.Text",
# #     "cachedTextGenerator.characters",
# #     "[{'cursorPos': {}, 'charWidth': 12.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 7.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 4.0}, {'cursorPos': {}, 'charWidth': 7.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 7.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 3.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 4.0}, {'cursorPos': {}, 'charWidth': 3.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 12.0}, {'cursorPos': {}, 'charWidth': 8.0}, {'cursorPos': {}, 'charWidth': 0.0}]",
# #     "UnityEngine.UI",
# #     1,
# #     get_property_as_string=True,
# # )

# # Image = self.altdriver.wait_for_object(
# #     By.PATH, "/UICamera/Game/WholeUI/Life/Image (2)"
# # )
# # Image.wait_for_component_property(
# #     "UnityEngine.RectTransform",
# #     "parent",
# #     "[[],[],[]]",
# #     "UnityEngine.CoreModule",
# #     1,
# #     get_property_as_string=True,
# # )

# # ScoreText = self.altdriver.wait_for_object(
# #     By.PATH, "/UICamera/Game/WholeUI/ScoreZone/ScoreLabel/ScoreText"
# # )
# # ScoreText.wait_for_component_property(
# #     "UnityEngine.UI.Text",
# #     "font.fontNames",
# #     "['Luckiest Guy']",
# #     "UnityEngine.UI",
# #     1,
# #     get_property_as_string=True,
# # )

# # SETUP = self.alt_driver.wait_for_object(By.PATH,"/===== SETUP =====")
# # SETUP.wait_for_component_property("UnityEngine.Transform", "position.x", "0.0", "UnityEngine.CoreModule",1,get_property_as_string=True)

# # def test(self):
# #     Text = self.alt_driver.wait_for_object(By.PATH,"/gameOverMenu/Panel/retry_button/Text")
# #     Text.set_text("!@#$%^&*()_+")

# # def test_cylinder_interaction(self):
# #     self.alt_driver.load_scene("Scene 1 AltDriverTestScene", True)  # Load scene for the test
# #     Cylinder = self.alt_driver.wait_for_object(By.PATH, "/Cylinder")  # Wait for Cylinder object
# #     Cylinder.click()  # Click on Cylinder object
# #     # Verify the expected outcome of the Cylinder interaction, e.g., position change
# #     position = Cylinder.get_component_property("UnityEngine.Transform", "position", "UnityEngine.CoreModule", get_property_as_string=True)
# #     self.assertEqual(position, "expectedPosition")  # Replace "expectedPosition" with actual expected position value


# # For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app
# import unittest
# from alttester import By, AltKeyCode, AltDriver


# # class MyTests(unittest.TestCase):

# #     @classmethod
# #     def setUp(self):
# #         self.alt_driver = AltDriver(host="192.168.2.110", port=13000, app_name="tc")

# #     # You might want to load the scene here
# #     #   self.alt_driver.load_scene("Main", True)

# #     @classmethod
# #     def tearDown(self):
# #         self.alt_driver.stop()

# #     def test(self):
# #         StartButton = self.alt_driver.wait_for_object(By.PATH, "/Canvas/StartButton")
# #         StartButton.tap()
# #         Text = self.alt_driver.wait_for_object(
# #             By.PATH, "/UICamera/Loadout/StoreButton/Text"
# #         )
# #         Text1 = self.alt_driver.wait_for_object(
# #             By.PATH, "/UICamera/Loadout/MissionButton/Text"
# #         )
# #         self.alt_driver.swipe(
# #             Text.get_screen_position(), Text1.get_screen_position(), 0, 8263245
# #         )


# # For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app
# import unittest
# from alttester import By, AltKeyCode, AltDriver


# class MyTests(unittest.TestCase):

#     @classmethod
#     def setUp(self):
#         self.alt_driver = AltDriver(host="192.168.2.110", port=13000, app_name="tc")

#     # You might want to load the scene here
#     #   self.alt_driver.load_scene("Main", True)

#     @classmethod
#     def tearDown(self):
#         self.alt_driver.stop()

#     def test(self):
#         StartButton = self.alt_driver.wait_for_object(By.PATH, "/Canvas/StartButton")
#         self.alt_driver.hold_button(StartButton.get_screen_position(), 1, 471436)


# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app
import unittest
from alttester import By, AltKeyCode, AltDriver


class MyTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.alt_driver = AltDriver(host="127.0.0.1", port=13000, app_name="tc")

    # You might want to load the scene here
    #   self.alt_driver.load_scene("Main", True)

    @classmethod
    def tearDown(self):
        self.alt_driver.stop()


    def test(self):
        text_path = "/UICamera/Loadout/SettingButton/Text"
        handle_path = "/UICamera/Loadout/SettingPopup/Background/MasterSFXSlider/Handle Slide Area/Handle"
        fill_path = (
            "/UICamera/Loadout/SettingPopup/Background/MasterSFXSlider/Fill Area/Fill"
        )
        about_path = "/UICamera/Loadout/SettingPopup/Background/About"
        back_button_path = "/UICamera/Loadout/SettingPopup/AboutPopup/Image/BackButton"
        fill_path1 = "/UICamera/Loadout/SettingPopup/Background/MasterSlider/Fill Area/Fill"
        fill_path2 = "/UICamera/Loadout/SettingPopup/Background/MusicSlider/Fill Area/Fill"
        self.alt_driver.load_scene("Main", True)
        text = self.alt_driver.wait_for_object(By.PATH, self.text_path, timeout=20)
        text.click()
        handle = self.alt_driver.wait_for_object(By.PATH, self.handle_path, timeout=20)
        fill = self.alt_driver.wait_for_object(By.PATH, self.fill_path, timeout=20)
        self.alt_driver.swipe(
            handle.get_screen_position(), fill.get_screen_position(), 1.834595
        )
        about = self.alt_driver.wait_for_object(By.PATH, self.about_path, timeout=20)
        self.alt_driver.hold_button(about.get_screen_position(), 0.8398438)
        BackButton = self.alt_driver.wait_for_object(
            By.PATH, self.back_button_path, timeout=20
        )
        BackButton.tap()
        fill1 = self.alt_driver.wait_for_object(By.PATH, self.fill_path1, timeout=20)
        fill2 = self.alt_driver.wait_for_object(By.PATH, self.fill_path2, timeout=20)
        fill2.wait_for_component_property(
            "UnityEngine.UI.Image",
            "sprite.textureRect.position.x",
            "648.0",
            "UnityEngine.UI",
            1,
            get_property_as_string=True,
            max_depth=1,
        )
