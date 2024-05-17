from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def log(message):
    print(f"[LOG] {message}")

try:
    log("Setting up ChromeDriver...")
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 필요 시 헤드리스 모드 활성화

    log("Starting ChromeDriver...")
    driver = webdriver.Chrome(service=service, options=options)

    log("Opening Vue.js application...")
    driver.get('http://localhost:8080')

    log("Waiting for page to load...")
    time.sleep(2)

    # 입력 필드에 텍스트 입력
    log("Finding input field and entering text...")
    input_field = driver.find_element(By.XPATH, '//input[@placeholder="Enter something"]')
    input_field.send_keys('Hello Selenium!')

    # 버튼 클릭
    log("Clicking the display message button...")
    display_button = driver.find_element(By.XPATH, '//button[text()="Display Message"]')
    display_button.click()

    # 결과 메시지 확인
    log("Waiting for result message...")
    time.sleep(1)
    result_message = driver.find_element(By.XPATH, '//p')
    assert result_message.text == 'Hello Selenium!', "The displayed message is incorrect"

    # 색변경 버튼 클릭 전 초기 색상 확인
    log("Checking initial colors...")
    box_test = driver.find_element(By.CLASS_NAME, 'box-container')
    initial_color_box_test = box_test.value_of_css_property('background-color')
    log(f"Initial BoxTest color: {initial_color_box_test}")

    box = driver.find_element(By.CLASS_NAME, 'box')
    initial_color_box = box.value_of_css_property('background-color')
    log(f"Initial div box color: {initial_color_box}")

    # 색변경 버튼 클릭
    log("Clicking the color change button...")
    color_change_button = driver.find_element(By.ID, 'color-change-button')
    color_change_button.click()

    # 색상 변경 확인
    log("Checking changed colors...")
    time.sleep(1)  # 색상 변경 후 렌더링 대기
    changed_color_box_test = box_test.value_of_css_property('background-color')
    log(f"Changed BoxTest color: {changed_color_box_test}")

    changed_color_box = box.value_of_css_property('background-color')
    log(f"Changed div box color: {changed_color_box}")

    assert initial_color_box_test != changed_color_box_test, "The BoxTest color did not change"
    assert initial_color_box != changed_color_box, "The div box color did not change"

    log("Test completed successfully!")

except Exception as e:
    log(f"An error occurred: {e}")
    log(f"Error details: {type(e).__name__}, {e}")

finally:
    log("Closing browser...")
    driver.quit()
