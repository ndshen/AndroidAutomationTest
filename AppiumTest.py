import subprocess
import time
import unittest
import logging
import yaml
import re
from appium.webdriver.common.touch_action import TouchAction

from Values import strings
from Values import numbers
from logging_config import create_logger
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

create_logger("MyTestCase")
logger = logging.getLogger(__name__)
config_file = "test_config.yml"


class MyTestCase(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        logger.info("Starting to setup MyTestCase")
        with open(config_file, 'r') as f:
            try:
                config = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                logging.error(str(exc))
                exit(1)

        self.dc = {"app": config["app"]["location"] + config["app"]["name"],
                   "deviceName": config["device"]["name"], "platformName": config["device"]["platform"],
                   "appPackage": config["app"]["package"], "appWaitActivity": config["app"]["waitActivity"],
                   "uiautomator2ServerLaunchTimeout": config["appium"]["uiautomator2ServerLaunchTimeout"]}
        # self.dc["fullReset"] = True
        logger.info("Testing {} on {}".format(config["app"]["name"], config["device"]["name"]))

        # Check if app is already installed
        p = subprocess.Popen("adb shell pm list packages", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = p.communicate()
        if config["app"]["package"] in out.decode("utf-8"):
            # app is already installed, clear user data
            logger.debug("App is already installed, clearing User Data")
            _ = subprocess.Popen("adb shell pm clear {}".format(config["app"]["package"]), shell=True)

        self.driver = webdriver.Remote(config["appium"]["url"], self.dc)
        self.driver.implicitly_wait(numbers.DRIVER_WAIT_TIME)
        print(self.driver.get_window_size())

    # def test_scan(self):
    #     logger = logging.getLogger("ScanTest")
    #     logger.info("Start Scan Test")
    #
    #     self.driver.find_element_by_id(strings.START_USE_BTN_ID).click()
    #     logger.info("'Start Using' Btn clicked")
    #     self.driver.find_element_by_id(strings.FREE_VERSION_BTN_ID).click()
    #     logger.info("Selected free version")
    #     self.driver.find_element_by_id(strings.CONTINUE_FREE_BTN_ID).click()
    #     logger.info("Selected free version again")
    #     self.driver.find_element_by_id(strings.SCAN_BTN_ID).click()
    #     logger.info("Scan Btn clicked")
    #     self.driver.find_element_by_id(strings.PERMISSION_ALLOWED_BTN_ID).click()
    #     logger.info("'Allow Permission' Btn clicked")
    #
    #     # My method to know a scan process has ended is to wait for scan progress element disappear
    #     waitedTime = 0
    #     while True:
    #         try:
    #             time.sleep(5)
    #             waitedTime += 5
    #             self.driver.find_element_by_id(strings.SCAN_PROGRESS_ID)
    #             logger.debug("Waiting for scan progress element to disappear...{}s".format(waitedTime))
    #             self.assertLess(waitedTime, numbers.MAXIMUM_SCAN_TIME)
    #         except NoSuchElementException:
    #             logger.info("Finish Scan Progress")
    #             break
    #
    #     try:
    #         status_element = self.driver.find_element_by_id(strings.STATUS_ELEMENT_ID)
    #         logger.info("Status: " + status_element.text)
    #         self.assertEqual(status_element.text == "掃描完成")
    #     except NoSuchElementException:
    #         logger.debug("Can't find status element.")
    #         # header_title = self.driver.find_element_by_id("com.avast.android.mobilesecurity:id/ui_feed_header_title")
    #         subtitle_element = self.driver.find_element_by_id(strings.STATUS_SUBTITLE_ELEMENT_ID)
    #         logger.info("Status Subtitle: " + subtitle_element.text)
    #         self.assertTrue("已掃描" in subtitle_element.text)

    def test_appVersion_info(self):
        logger = logging.getLogger("AppVersionTest")
        logger.info("Start AppVersionInfo Test")

        self.driver.find_element_by_id(strings.START_USE_BTN_ID).click()
        logger.info("'Start Using' Btn clicked")
        self.driver.find_element_by_id(strings.FREE_VERSION_BTN_ID).click()
        logger.info("Selected free version")
        self.driver.find_element_by_id(strings.CONTINUE_FREE_BTN_ID).click()
        logger.info("Selected free version again")
        self.driver.find_element_by_xpath(strings.MENU_BAR_XPATH).click()
        logger.info("Clicked Menu Bar")

        self.driver.swipe(start_x=405, start_y=1642, end_x=405, end_y=470, duration=500)
        logger.info("Menu scrolled to bottom1")
        # touch = TouchAction(driver=self.driver)
        # touch.press(x=405, y=1642).move_to(x=409, y=470).release().perform()
        # logger.info("Menu scrolled to bottom")


        time.sleep(10)
        self.driver.find_element_by_id(strings.SETTINGS_BTN_ID)
        logger.info("Clicked Settings")
        self.driver.find_element_by_xpath(strings.ABOUT_BTN_XPATH)
        logger.info("Clicked About")
        version_info_textview = self.driver.find_element_by_id(strings.VERSION_INFO_TEXTVIEW_ID)
        logger.info("Version Info: " + version_info_textview.text)
        self.assertTrue(re.match("版本.+", version_info_textview.text) is not None)

    def tearDown(self):
        self.driver.quit()
        logger.info("End of test. Webdriver shut down. \n\n\n")


if __name__ == '__main__':
    unittest.main()
