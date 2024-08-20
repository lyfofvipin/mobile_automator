from fixtures import *
import os, yaml
from modules.common import video_dir

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

@pytest.fixture(scope="session")
def app_session():

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config_data(request):

    config_file = "config.yaml"
    if os.environ.get("MOB_AUTO_CONFIG"):
        config_file = os.environ.get("MOB_AUTO_CONFIG")
    print(f"MOB_AUTO_CONFIG set to {config_file}")
    with open(config_file, 'r') as file:
        data = yaml.safe_load(file)

    data["username"] = request.config.getoption("--username")
    data["password"] = request.config.getoption("--password")
    return data
