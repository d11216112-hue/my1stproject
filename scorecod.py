#練習2：敏捷迭代
def calculate_scorecod(age, experience_years, certifications):
    score = 0

    # 年齡評分
    if age < 25:
        score += 10
    elif 25 <= age < 35:
        score += 20
    elif 35 <= age < 50:
        score += 15
    else:
        score += 5

    # 經驗年數評分
    if experience_years < 2:
        score += 5
    elif 2 <= experience_years < 5:
        score += 15
    elif 5 <= experience_years < 10:
        score += 25
    else:
        score += 30

    # 證書數量評分
    score += certifications * 10

    return score
# 測試範例
if __name__ == "__main__":
    age = 30
    experience_years = 4
    certifications = 3
    total_score = calculate_scorecod(age, experience_years, certifications)
    print(f"總分數為: {total_score}")
    # 預期輸出: 總分數為: 65
    # 計算過程:
    # 年齡評分: 20 (25-35歲)
    # 經驗年數評分: 15 (2-5年)
    # 證書數量評分: 30 (3張證書，每張10分)
    # 總分數: 20 + 15 + 30 = 65
    
                            


