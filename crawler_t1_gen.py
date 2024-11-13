from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from collections import defaultdict
import time
import re

page = 1
fix_count = 0

def fix_geng_player_data(player_name, champion_name, stage_text):
    global fix_count

    """Gen.G 선수 데이터 수정 - 특정 경기만"""        
    if re.match(r"1승조 2경기.*", stage_text) and player_name == "GEN Chovy":
        fix_count += 1        
        if fix_count == 2:
            print(f'매칭! stage: {stage_text}, player: {player_name}, champion: {champion_name}')
            return "GEN Peyz"
    
    return player_name

def analyze_teams_stats():
    team_stats = {
        'T1': defaultdict(lambda: {'kills': 0, 'deaths': 0, 'assists': 0, 'games': 0}),
        'GEN': defaultdict(lambda: {'kills': 0, 'deaths': 0, 'assists': 0, 'games': 0})
    }
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        base_url = "https://lol.inven.co.kr/dataninfo/match/teamList.php"        
        
        global page
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
                    match_text = match.text
                    if "T1" in match_text or "Gen.G" in match_text:
                        stage = match.find_element(By.CLASS_NAME, "stage").text
                        print(f"매치 발견: {'T1' if 'T1' in match_text else 'Gen.G'} - {stage}")
                        
                        try:
                            detail_button = wait.until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, f"#{match.get_attribute('id')} .detail"))
                            )
                            driver.execute_script("arguments[0].click();", detail_button)
                            time.sleep(1)
                            
                            detail_table = wait.until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, f"#{match.get_attribute('id')} .detailTable"))
                            )
                            
                            players = detail_table.find_elements(By.CSS_SELECTOR, ".player")
                            
                            for player in players:
                                player_name = player.find_element(By.CLASS_NAME, "playername").text
                                
                                try:
                                    # 이미지를 찾아서 챔피언 이름 추출
                                    champion_img = player.find_element(By.CSS_SELECTOR, ".icon img[onmouseover]")
                                    champion = champion_img.get_attribute("onmouseover")
                                    champion_name = champion.split("'")[1]
                                except:
                                    # 챔피언 정보를 찾을 수 없는 경우 기본값 사용
                                    champion_name = "unknown"

                                # 특정 경기에 대해서만 선수 데이터 수정
                                player_name = fix_geng_player_data(player_name, champion_name, stage)
                                
                                if "T1" in player_name:
                                    team = 'T1'
                                    name = player_name.replace("T1 ", "")
                                elif "GEN" in player_name:
                                    team = 'GEN'
                                    name = player_name.replace("GEN ", "")
                                else:
                                    continue
                                    
                                stats = player.find_element(By.CLASS_NAME, "p2").find_elements(By.TAG_NAME, "li")
                                
                                team_stats[team][name]['kills'] += int(stats[0].text)
                                team_stats[team][name]['deaths'] += int(stats[1].text)
                                team_stats[team][name]['assists'] += int(stats[2].text)
                                team_stats[team][name]['games'] += 1
                            
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
    
    print("\n2024 월드챔피언십 T1 vs Gen.G 선수별 통계 비교")
    print("=" * 100)
    
    positions = ['Top', 'Jungle', 'Mid', 'Bot', 'Support']
    position_players = {
        'T1': {'Top': 'Zeus', 'Jungle': 'Oner', 'Mid': 'Faker', 'Bot': 'Gumayusi', 'Support': 'Keria'},
        'GEN': {'Top': 'Kiin', 'Jungle': 'Canyon', 'Mid': 'Chovy', 'Bot': 'Peyz', 'Support': 'Lehends'}
    }
    
    for pos in positions:
        print(f"\n{pos} 라인 비교:")
        print("-" * 100)
        print(f"{'팀':6} {'선수':10} {'전체 K/D/A':20} {'평균 K/D/A':20} {'KDA':8} {'경기 수':8}")
        print("-" * 100)
        
        for team in ['T1', 'GEN']:
            player = position_players[team][pos]
            if player in team_stats[team]:
                stats = team_stats[team][player]
                
                kills = stats['kills']
                deaths = stats['deaths']
                assists = stats['assists']
                games = stats['games']
                
                if deaths == 0:
                    kda = kills + assists
                else:
                    kda = (kills + assists) / deaths
                
                avg_k = kills / games if games > 0 else 0
                avg_d = deaths / games if games > 0 else 0
                avg_a = assists / games if games > 0 else 0
                
                total_kda = f"{kills}/{deaths}/{assists}"
                avg_kda = f"{avg_k:.1f}/{avg_d:.1f}/{avg_a:.1f}"
                
                print(f"{team:6} {player:10} {total_kda:20} {avg_kda:20} {kda:8.2f} {games:8}")
            else:
                print(f"{team:6} {player:10} {'데이터 없음':20}")

if __name__ == "__main__":
    analyze_teams_stats()