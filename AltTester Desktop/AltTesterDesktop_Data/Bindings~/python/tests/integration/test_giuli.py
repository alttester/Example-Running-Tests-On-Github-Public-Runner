# # For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app
# import unittest
# from alttester import By, AltKeyCode, AltDriver


# class MyTests(unittest.TestCase):

#     @classmethod
#     def setUp(self):
#         self.altdriver = AltDriver(host="127.0.0.1", port=13000, app_name="__default__")

#     # You might want to load the scene here
#     #   self.altdriver.load_scene("Scene 1 AltDriverTestScene", True)

#     @classmethod
#     def tearDown(self):
#         self.altdriver.stop()

#     def test(self):
#         Capsule = self.altdriver.wait_for_object(By.PATH, "/Capsule")
#         Capsule.wait_for_component_property(
#             "UnityEngine.Rigidbody",
#             "gameObject.scene.name",
#             "Scene 1 AltDriverTestScene",
#             "UnityEngine.PhysicsModule",
#             1,
#             get_property_as_string=True,
#         )

#         Capsule.wait_for_component_property(
#             "UnityEngine.Rigidbody",
#             "gameObject.scene.isLoaded",
#             "True",
#             "UnityEngine.PhysicsModule",
#             1,
#             get_property_as_string=True,
#         )

#         Capsule.wait_for_component_property(
#             "UnityEngine.Rigidbody",
#             "gameObject.scene.handle",
#             "-254",
#             "UnityEngine.PhysicsModule",
#             1,
#             get_property_as_string=True,
#         )

#         Capsule.wait_for_component_property(
#             "UnityEngine.Rigidbody",
#             "transform",
#             "[]",
#             "UnityEngine.PhysicsModule",
#             1,
#             get_property_as_string=True,
#         )

#         Capsule.wait_for_component_property(
#             "UnityEngine.Rigidbody",
#             "transform",
#             "[]",
#             "UnityEngine.PhysicsModule",
#             1,
#             get_property_as_string=True,
#         )

#         Text = self.altdriver.wait_for_object(By.PATH, "/Canvas/UIButton/Text")
#         Text.wait_for_component_property(
#             "UnityEngine.UI.Text",
#             "font.material.shader.name",
#             "GUI/Text Shader",
#             "UnityEngine.UI",
#             1,
#             get_property_as_string=True,
#         )

#         Text.wait_for_component_property(
#             "UnityEngine.UI.Text",
#             "material.mainTexture",
#             "None",
#             "UnityEngine.UI",
#             1,
#             get_property_as_string=True,
#         )
