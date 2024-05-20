from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def log(message):
    print(f"[LOG] {message}")

try:
    log("Setting up ChromeDriver...")
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    # 모바일 장치 설정 
    mobile_emulation = {
        "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
        "userAgent": (
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) "
                        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                        "Version/12.0 Mobile/15A372 Safari/604.1"
                    )
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    # options.add_argument('--headless')  # 필요 시 헤드리스 모드 활성화

    log("Starting ChromeDriver...")
    driver = webdriver.Chrome(service=service, options=options)

    log("Opening Vue.js application...")
    # 주소
    driver.get('http://localhost:8081/')

    log("Waiting for page to load...")
    time.sleep(2)

    # 입력 필드에 텍스트 입력
    log("Finding input field and entering text...")
    inputs = driver.find_elements(By.XPATH, '//input')
    if not inputs:
        log("No input fields found.")
    for input_field in inputs:
        placeholder = input_field.get_attribute('placeholder')
        log(f"Typing input with placeholder: {placeholder}")
        input_field.send_keys('Hello Selenium!')
        log(f"Entered text into input with placeholder: {placeholder}")

    # 모든 버튼 클릭
    log("Clicking all buttons...")
    buttons = driver.find_elements(By.XPATH, '//button')
    if not buttons:
        log("No buttons found.")
    for button in buttons:
        button_text = button.text
        log(f"Clicking button with text: {button_text}")
        button.click()
        time.sleep(1)  # 각 버튼 클릭 후 잠시 대기

    # 결과 메시지 확인
    log("Waiting for result message...")
    try:
        result_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//p'))
        )
        actual_message = result_message_element.text
        log(f"Actual result message: '{actual_message}'")
        assert actual_message == 'Hello Selenium!', "The displayed message is incorrect"
    except Exception as e:
        log(f"An error occurred while waiting for the result message: {e}")
        raise

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
