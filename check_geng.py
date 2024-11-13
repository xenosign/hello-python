from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from collections import defaultdict
import time

def check_geng_lineups():
    # Chrome 웹드라이버 초기화
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        base_url = "https://lol.inven.co.kr/dataninfo/match/teamList.php"
        page = 1
        
        while True:
            url = f"{base_url}?iskin=lol&category2=192&pg={page}"
            print(f"\n페이지 {page} 처리 중...")
            driver.get(url)
            time.sleep(2)
            
            try:
                matches = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listFrame")))
                if not matches:
                    break
                
                for match in matches:
                    if "Gen.G" in match.text:
                        stage = match.find_element(By.CLASS_NAME, "stage").text
                        date = match.find_element(By.CLASS_NAME, "date").text
                        
                        try:
                            detail_button = wait.until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, f"#{match.get_attribute('id')} .detail"))
                            )
                            driver.execute_script("arguments[0].click();", detail_button)
                            time.sleep(1)
                            
                            detail_table = wait.until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, f"#{match.get_attribute('id')} .detailTable"))
                            )
                            
                            # Gen.G 선수들 찾기
                            geng_players = set()
                            players = detail_table.find_elements(By.CSS_SELECTOR, ".player")
                            
                            for player in players:
                                player_name = player.find_element(By.CLASS_NAME, "playername").text
                                if "GEN" in player_name:
                                    name = player_name.replace("GEN ", "")
                                    geng_players.add(name)
                            
                            # Peyz나 Chovy가 없는 경우 체크
                            if "Peyz" not in geng_players or "Chovy" not in geng_players:
                                print(f"\n[선수 누락 발견]")
                                print(f"날짜: {date}")
                                print(f"스테이지: {stage}")
                                print(f"출전 선수: {', '.join(sorted(geng_players))}")
                            
                            detail_button.click()
                            
                        except (TimeoutException, NoSuchElementException) as e:
                            print(f"매치 상세 정보 처리 중 오류 발생: {e}")
                            continue
                
                next_pages = driver.find_elements(By.CSS_SELECTOR, "span.nexttext.active")
                if not next_pages:
                    break
                
                page += 1
                
            except TimeoutException:
                print(f"페이지 {page} 로딩 시간 초과")
                break
                
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Gen.G 선수 누락 경기 확인 중...")
    check_geng_lineups()