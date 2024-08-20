from fixtures import *
import os, datetime
from random import choice
from modules import locators
from shutil import rmtree

# setup logs dirs
logs_dir = "logs"
screenshot_dir = "logs/screenshot/"
video_dir = "logs/videos/"
def check_and_create_dir(path: str) -> None:
    rmtree(path, ignore_errors=True)
    if not os.path.exists(path):
        os.mkdir(path)
check_and_create_dir(logs_dir)
check_and_create_dir(screenshot_dir)
check_and_create_dir(video_dir)

def get_timestamp() -> str:
    """
    Function to get te timestamp
    """
    return datetime.datetime.now().strftime("%d-%m-%y-%H-%M-%S")

def add_to_logs(logs, file_name="common_logs", display=True):
    
    """
    Function to dump all the logs in a file and on the console
    """

    with open(os.path.join("logs", file_name+".txt"), "a") as file:
        for x in logs.splitlines():
            if display: print(x)
            file.write(x+"\n")

def click_or_validate_element(session,
                              locator, 
                              method="xpath", 
                              wait=32000, 
                              take_screenshot=True,
                              click=True,
                              fill="",
                              select_sub_element=None,
                              check=False):

    """
    This function will do operations on web element.
    session : session object you want to interact with
    locator : this is the element id/xpath or value from locators.py
    method : how you want to find the locator xpath
    wait : want to wait before clicking the element
    wait_method : how you want to wait until visible until clock etc...
    take_screenshot : do you want to take screenshot before clicking
    click : do you want to click on the locator or not
    fill : what value you want to fill on the locator
    select_sub_element: If a locator was a group of element then use the option to click on a specific number of element from the group pass random if you want to select random
    check: If you want to check the select button
    """

    add_to_logs(f"Clicking on {locator} as {method}")
    if method == "xpath" and not select_sub_element:
        element = session.find_element(By.XPATH, locator)
    elif select_sub_element:
        element = session.find_elements(By.XPATH, locator)
    else:
        add_to_logs("No locator is passed.")

    if select_sub_element == "random":
        element = element[choice(range(0, element.count()))]
    elif select_sub_element:
        element = element[select_sub_element]

    # if take_screenshot: session.screenshot(full_page=True, path=os.path.join(screenshot_dir, f"{get_timestamp()}.png"))
    if wait: time.sleep(wait)
    if click: element.click()
    if fill: element.send_keys(fill)

    return True
