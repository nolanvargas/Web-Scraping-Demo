from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import boto3
import time
from datetime import datetime

st = time.time()

LEADERBOARD_COUNT = 10

# Create time stamp
def t(time):
    x = time - st
    return str(float("{:.2}".format(x))) + "s"

# Logger
def log(text):
    now= time.time()
    f.write(f"{t(now)} {text}\n")


f = open("updates_log.txt", "a")
dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
log(f"----------Starting script at {dt_string}----------")

driver = webdriver.Chrome()
log("Launching chrome web driver")
driver.get("https://apexlegendsstatus.com/live-ranked-leaderboards/Battle_Royale/PA")
log("Waiting...")
driver.implicitly_wait(15)
tags = []
rps = []

for i in range(LEADERBOARD_COUNT):
    y = i+1
    try:
        tag = driver.find_element(by=By.XPATH, value=f"/html/body/main/div[1]/div[2]/div/div/div/div[2]/div/table/tbody/tr[{y}]/td[3]/div/div[2]/span/a").text
        rp = driver.find_element(by=By.XPATH, value=f"/html/body/main/div[1]/div[2]/div/div/div/div[2]/div/table/tbody/tr[{y}]/td/span").text
    except NoSuchElementException:
        log("Error: No such element exists")
        log("Terminating script")
        driver.quit()
        quit()

    log(f"Adding {tag} to list at {len(tags)} with {rp} rp")
    rps.append(rp)
    tags.append(tag)

log("Closing chrome web driver")
driver.quit()

# Create DynamoDb instance
log("Initializing DynamoDB")
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='#',
    aws_secret_access_key='#',
    region_name="us-west-2"
    )


# Delete contents of table 
for i in range(LEADERBOARD_COUNT):
    y = i+1
    a = dynamodb.Table('apex_leaderboard').delete_item(Key={'ranking': y})
    log(f"Deleted item with status code {a['ResponseMetadata']['HTTPStatusCode']} and {a['ResponseMetadata']['RetryAttempts']} retry attempts")

# Write to table
for i in range(LEADERBOARD_COUNT):
    y = i+1
    a = dynamodb.Table('apex_leaderboard').put_item(Item={'ranking' : y, 'tag': tags[i], 'rp': rps[i]})
    log(f"Added item with status code {a['ResponseMetadata']['HTTPStatusCode']} and {a['ResponseMetadata']['RetryAttempts']} retry attempts")

dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
log(f"----------Finished script at {dt_string}----------\n\n\n")
f.close()
