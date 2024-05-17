from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 로그 함수 추가
def log(message):
    print(f"[LOG] {message}")

try:
    # ChromeDriver를 자동으로 다운로드하고 설치
    log("Setting up ChromeDriver...")
    service = Service(ChromeDriverManager().install())

    # Chrome 옵션 설정
    options = webdriver.ChromeOptions()

    # ChromeDriver 실행
    log("Starting ChromeDriver...")
    driver = webdriver.Chrome(service=service, options=options)

    # Vue.js 애플리케이션 실행 (http://localhost:8080으로 가정)
    log("Opening Vue.js application...")
    driver.get('http://localhost:8080')

    # 페이지가 로드될 시간을 기다림
    log("Waiting for page to load...")
    time.sleep(2)

    # 입력 필드에 텍스트 입력
    log("Finding input field and entering text...")
    input_field = driver.find_element(By.XPATH, '//input[@placeholder="Enter something"]')
    input_field.send_keys('Hello Selenium!')

    # 버튼 클릭
    log("Clicking the button...")
    display_button = driver.find_element(By.XPATH, '//button[text()="Display Message"]')
    display_button.click()

    # 결과 메시지 확인
    log("Waiting for result message...")
    time.sleep(1)
    result_message = driver.find_element(By.XPATH, '//p')
    assert result_message.text == 'Hello Selenium!'

    log("Test completed successfully!")

except Exception as e:
    log(f"An error occurred: {e}")

finally:
    # 브라우저 종료
    log("Closing browser...")
    driver.quit()
