# AndroidAutomationTest
 
## Description
In this project, I developed 2 simple test case for [**Avast Mobile Security**](https://play.google.com/store/apps/details?id=com.avast.android.mobilesecurity) on Android. The main purpose of this project is to learn Appium and Android Automation Testing.

## Prerequisites
### Environment Setup   
#### 1. Install Python3
Here is the link for the latest python version to install: https://www.python.org/downloads/
#### 2. Install Appium
I installed the Appium Desktop v1.17.1-1 from [here](https://github.com/appium/appium-desktop/releases). 
#### 3. Install Java and Android Studio(with SDK)
Remember to add **adb** to path after installing SDK, and enable the developer mode in your Android device.

### Dependencies
You can checkout the dependencies in this project at *requirements.txt*
```
Appium-Python-Client==0.36
PyYAML==5.3.1
selenium==3.141.0
urllib3==1.24.1
```
To install the packages, simply run the following command:
```bash
pip install -r requirements.txt
```

## Configuration
Before running the test, remember to modify **test_config.yml** and set to your own settings.
```yaml
app:
  name: name of the Avast Mobile Security apk file
  location: the absolute path of the apk file
  package: "com.avast.android.mobilesecurity"
  waitActivity: "com.avast.android.mobilesecurity.app.main.MainActivity"

device:
  name: Android device. #Type 'adb devices' in cmd to find out 
  platform: "Android"

appium:
  url: "http://[appium server url]/wd/hub"
```