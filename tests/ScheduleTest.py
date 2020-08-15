"""
    Frances O'Leary, 8/14/2020

    This is a test of using schedule to schedule tasks to occur.
    This one should print "I'm working. . ." every 10
    minutes.
"""
import schedule
import time

def job():
    print "I'm working. . ."
    
schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
