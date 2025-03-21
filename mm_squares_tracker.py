import requests
from datetime import datetime

def get_march_madness_scores():
    date = input("What date would you like to check? (Please enter YYYYMMDD Ex: 20250321) ")
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?dates={}&groups=100&limit=500".format(date)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        games = data.get("events", [])
        square_winner = 0

        if not games:
            print("No games found for today.")
            return
        
        for game in games:
            teams = game["competitions"][0]["competitors"]
            team1 = teams[0]["team"]["displayName"]
            team2 = teams[1]["team"]["displayName"]
            score1 = teams[0]["score"]
            score2 = teams[1]["score"]
            winner = team1 if teams[0].get("winner", False) else team2
#            headline = game["competitions"][0]["headlines"][0]["shortLinkText"]
            winning_score = score1 if score2<score1 else score2
            losing_score = score2 if score1>score2 else score1
            if str(winning_score).endswith("1") and str(losing_score).endswith("5"):
                square_winner += 1
            print(f"{winning_score} - {losing_score}")
            print(f"{team1} ({score1}) vs {team2} ({score2})")
            print(f"Winner: {winner}")
#            print(f"Headline: {headline}\n")
            print("\n")
        print("\n")
        print("************")
        print(f"Number of Square Wins for today {square_winner}\n")
        print("************")

      
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    get_march_madness_scores()

