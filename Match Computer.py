import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("ftc-robotics-383722-73666d8c73eb.json", scope)
client = gspread.authorize(creds)

opr = {636: 0, 1002: 0, 1350: 0, 3658: 0, 5026: 0, 5159: 0, 5773: 0, 6220: 0, 6417: 0, 6584: 0, 6645: 0, 7149: 0, 7172: 0,
              7244: 0, 7767: 0, 9864: 0, 9974: 0, 10127: 0, 10355: 0, 10391: 0, 11574: 0, 14010: 0, 14204: 0, 14436: 0, 14496: 0,
              14779: 0, 15972: 0, 16008: 0, 16290: 0, 16377: 0, 16458: 0, 17628: 0, 18185: 0, 18270: 0, 18432: 0, 18438: 0, 18840: 0,
              19207: 0, 19332: 0, 19444: 0, 19458: 0, 20914: 0, 21036: 0, 21159: 0, 21397: 0, 21618: 0, 22683: 0, 22940: 0}

auto_opr = {636: 0, 1002: 0, 1350: 0, 3658: 0, 5026: 0, 5159: 0, 5773: 0, 6220: 0, 6417: 0, 6584: 0, 6645: 0, 7149: 0, 7172: 0,
              7244: 0, 7767: 0, 9864: 0, 9974: 0, 10127: 0, 10355: 0, 10391: 0, 11574: 0, 14010: 0, 14204: 0, 14436: 0, 14496: 0,
              14779: 0, 15972: 0, 16008: 0, 16290: 0, 16377: 0, 16458: 0, 17628: 0, 18185: 0, 18270: 0, 18432: 0, 18438: 0, 18840: 0,
              19207: 0, 19332: 0, 19444: 0, 19458: 0, 20914: 0, 21036: 0, 21159: 0, 21397: 0, 21618: 0, 22683: 0, 22940: 0}

total_auto = {636: 0, 1002: 0, 1350: 0, 3658: 0, 5026: 0, 5159: 0, 5773: 0, 6220: 0, 6417: 0, 6584: 0, 6645: 0, 7149: 0, 7172: 0,
              7244: 0, 7767: 0, 9864: 0, 9974: 0, 10127: 0, 10355: 0, 10391: 0, 11574: 0, 14010: 0, 14204: 0, 14436: 0, 14496: 0,
              14779: 0, 15972: 0, 16008: 0, 16290: 0, 16377: 0, 16458: 0, 17628: 0, 18185: 0, 18270: 0, 18432: 0, 18438: 0, 18840: 0,
              19207: 0, 19332: 0, 19444: 0, 19458: 0, 20914: 0, 21036: 0, 21159: 0, 21397: 0, 21618: 0, 22683: 0, 22940: 0}

total_teleop = {636: 0, 1002: 0, 1350: 0, 3658: 0, 5026: 0, 5159: 0, 5773: 0, 6220: 0, 6417: 0, 6584: 0, 6645: 0, 7149: 0, 7172: 0,
              7244: 0, 7767: 0, 9864: 0, 9974: 0, 10127: 0, 10355: 0, 10391: 0, 11574: 0, 14010: 0, 14204: 0, 14436: 0, 14496: 0,
              14779: 0, 15972: 0, 16008: 0, 16290: 0, 16377: 0, 16458: 0, 17628: 0, 18185: 0, 18270: 0, 18432: 0, 18438: 0, 18840: 0,
              19207: 0, 19332: 0, 19444: 0, 19458: 0, 20914: 0, 21036: 0, 21159: 0, 21397: 0, 21618: 0, 22683: 0, 22940: 0}

total_endgame = {636: 0, 1002: 0, 1350: 0, 3658: 0, 5026: 0, 5159: 0, 5773: 0, 6220: 0, 6417: 0, 6584: 0, 6645: 0, 7149: 0, 7172: 0,
              7244: 0, 7767: 0, 9864: 0, 9974: 0, 10127: 0, 10355: 0, 10391: 0, 11574: 0, 14010: 0, 14204: 0, 14436: 0, 14496: 0,
              14779: 0, 15972: 0, 16008: 0, 16290: 0, 16377: 0, 16458: 0, 17628: 0, 18185: 0, 18270: 0, 18432: 0, 18438: 0, 18840: 0,
              19207: 0, 19332: 0, 19444: 0, 19458: 0, 20914: 0, 21036: 0, 21159: 0, 21397: 0, 21618: 0, 22683: 0, 22940: 0}

matches_played = {636: 0, 1002: 0, 1350: 0, 3658: 0, 5026: 0, 5159: 0, 5773: 0, 6220: 0, 6417: 0, 6584: 0, 6645: 0, 7149: 0, 7172: 0,
              7244: 0, 7767: 0, 9864: 0, 9974: 0, 10127: 0, 10355: 0, 10391: 0, 11574: 0, 14010: 0, 14204: 0, 14436: 0, 14496: 0,
              14779: 0, 15972: 0, 16008: 0, 16290: 0, 16377: 0, 16458: 0, 17628: 0, 18185: 0, 18270: 0, 18432: 0, 18438: 0, 18840: 0,
              19207: 0, 19332: 0, 19444: 0, 19458: 0, 20914: 0, 21036: 0, 21159: 0, 21397: 0, 21618: 0, 22683: 0, 22940: 0}

def sync():
    global sheet_instance, grand_auto, grand_teleop, grand_endgame
    sheet = client.open("Matches")
    sheet_instance = sheet.get_worksheet(0)
    grand_auto = 0
    grand_teleop = 0
    grand_endgame = 0
    
    for match_data in sheet_instance.get_all_records():
        try:
            matches_played[match_data["Red One"]] += 1
            matches_played[match_data["Red Two"]] += 1
            matches_played[match_data["Blue One"]] += 1
            matches_played[match_data["Blue Two"]] += 1
            
            total_auto[match_data["Red One"]] += int(match_data["Red Auto"])
            total_auto[match_data["Red Two"]] += int(match_data["Red Auto"])
            total_auto[match_data["Blue One"]] += int(match_data["Blue Auto"])
            total_auto[match_data["Blue Two"]] += int(match_data["Blue Auto"])
            
            total_teleop[match_data["Red One"]] += int(match_data["Red TeleOp"])
            total_teleop[match_data["Red Two"]] += int(match_data["Red TeleOp"])
            total_teleop[match_data["Blue One"]] += int(match_data["Blue TeleOp"])
            total_teleop[match_data["Blue Two"]] += int(match_data["Blue TeleOp"])
            
            total_endgame[match_data["Red One"]] += int(match_data["Red Endgame"])
            total_endgame[match_data["Red Two"]] += int(match_data["Red Endgame"])
            total_endgame[match_data["Blue One"]] += int(match_data["Blue Endgame"])
            total_endgame[match_data["Blue Two"]] += int(match_data["Blue Endgame"])
            
            match_number = int(str(match_data["Match Number"])[-1])
        except:
            for i in total_auto:
                grand_auto += total_auto[i] / max(matches_played[i], 1)
            for i in total_teleop:
                grand_teleop += total_teleop[i] / max(matches_played[i], 1)
            for i in total_endgame:
                grand_endgame += total_endgame[i] / max(matches_played[i], 1)
            
            grand_auto /= match_number
            grand_teleop /= match_number
            grand_endgame /= match_number
            
            print("Synced with spreadsheet")
            return
            
def lookup(team_number):
    print("Average Auto: " + str(int(total_auto[team_number]) / int(matches_played[team_number])))
    print("Average TeleOp: " + str(int(total_teleop[team_number]) / int(matches_played[team_number])))
    print("Average Endgame: " + str(int(total_endgame[team_number]) / int(matches_played[team_number])))
    print("Standard Deviation Auto: " + str(round(int(total_auto[team_number]) / int(matches_played[team_number]) - grand_auto)))
    print("Standard Deviation TeleOp: " + str(round(int(total_teleop[team_number]) / int(matches_played[team_number]) - grand_teleop)))
    print("Standard Deviation Endgame: " + str(round(int(total_endgame[team_number]) / int(matches_played[team_number]) - grand_endgame)))
    print("Matches Played: " + str(matches_played[team_number]))

sync()
while True:
    user_input = input("Team Computer: ")
    if user_input == "sync":
        sync()
    else:
        lookup(int(user_input))
