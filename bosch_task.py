import unittest
from appium import webdriver

class FieldButtonTests(unittest.TestCase):

    @classmethod

    def setUpClass(self): 
    
        desired_caps = {                    
                        'platformName': 'Windows',
                        'deviceName': 'WindowsPC'
                        }
        desired_caps["app"] = ""
        # Start Appium session
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_initialize(self):
        self.driver.find_element_by_name("Save").click()
        self.driver.find_element_by_name("Clear").click()

    def test_field(self):
        input_field_locator = (self.driver.find_element_by_name, 'textfiled')
        # Find the input field and enter text
        input_field = self.driver.find_element(*input_field_locator)
        input_field.send_keys('MyTestInput')

        if input_field.is_enabled():
            print("Test case passed: input_field is enabled after entering input.")
        else:
            print("Test case failed: input_field is not enabled after entering input.")

    def test_buttion(self):
        submit_button_locator = (self.driver.find_element_by_name, 'SubmitButton')

        submit_button = self.driver.find_element(*submit_button_locator)

        if submit_button.is_enabled():
            print("Test case passed: Submit button is enabled after entering input.")
        else:
            print("Test case failed: Submit button is not enabled after entering input.")

if __name__ == '__main__':
    unittest.TestLoader().TestCase(FieldButtonTests).run()
