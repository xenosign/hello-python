from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
import time

def analyze_t1_tournament_stats():
    # 각 선수별 통계를 저장할 딕셔너리
    players_stats = defaultdict(lambda: {'kills': 0, 'deaths': 0, 'assists': 0, 'games': 0})
    
    # Chrome 웹드라이버 초기화
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    try:
        # 첫 페이지 접속
        base_url = "https://lol.inven.co.kr/dataninfo/match/teamList.php"
        
        page = 1
        while True:
            # 현재 페이지 URL
            url = f"{base_url}?iskin=lol&category2=192&pg={page}"
            print(f"\n페이지 {page} 처리 중...")
            driver.get(url)
            time.sleep(2)  # 페이지 로딩 대기
            
            # 모든 매치 찾기
            matches = driver.find_elements(By.CLASS_NAME, "listFrame")
            if not matches:  # 매치가 없으면 종료
                break
                
            for match in matches:
                # T1 경기만 분석
                if "T1" in match.text:
                    print("T1 매치 발견, 데이터 수집 중...")
                    # 상세 정보 버튼 클릭
                    detail_button = match.find_element(By.CLASS_NAME, "detail")
                    driver.execute_script("arguments[0].click();", detail_button)
                    time.sleep(1)  # 데이터 로딩 대기
                    
                    # T1 선수들 스탯 수집
                    detail_table = match.find_element(By.CLASS_NAME, "detailTable")
                    players = detail_table.find_elements(By.CSS_SELECTOR, ".player")
                    
                    for player in players:
                        player_name = player.find_element(By.CLASS_NAME, "playername").text
                        if "T1" in player_name:
                            name = player_name.replace("T1 ", "")  # T1 접두어 제거
                            stats = player.find_element(By.CLASS_NAME, "p2").find_elements(By.TAG_NAME, "li")
                            
                            # 스탯 업데이트
                            players_stats[name]['kills'] += int(stats[0].text)
                            players_stats[name]['deaths'] += int(stats[1].text)
                            players_stats[name]['assists'] += int(stats[2].text)
                            players_stats[name]['games'] += 1
                    
                    # 상세 정보 다시 접기
                    detail_button.click()
            
            # 다음 페이지 확인
            next_page = driver.find_elements(By.CSS_SELECTOR, "span.nexttext.active")
            if not next_page:
                break
                
            page += 1
                
    finally:
        driver.quit()
    
    # 결과 계산 및 출력
    print("\nT1 선수별 2024 월드챔피언십 전체 통계:")
    print("=" * 70)
    print(f"{'선수':10} {'전체 K/D/A':20} {'평균 K/D/A':20} {'KDA':8} {'경기 수':8}")
    print("-" * 70)
    
    for player, stats in players_stats.items():
        kills = stats['kills']
        deaths = stats['deaths']
        assists = stats['assists']
        games = stats['games']
        
        if deaths == 0:
            kda = kills + assists  # 죽음이 0일 경우
        else:
            kda = (kills + assists) / deaths
        
        # 경기당 평균 스탯
        avg_k = kills / games
        avg_d = deaths / games
        avg_a = assists / games
        
        total_kda = f"{kills}/{deaths}/{assists}"
        avg_kda = f"{avg_k:.1f}/{avg_d:.1f}/{avg_a:.1f}"
        
        print(f"{player:10} {total_kda:20} {avg_kda:20} {kda:8.2f} {games:8}")

if __name__ == "__main__":
    analyze_t1_tournament_stats()