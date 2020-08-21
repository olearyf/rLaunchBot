# 🚀 [@rLaunchBot](https://twitter.com/rLaunchBot)

**Note: rLaunchBot is a work in progress!**

![](https://github.com/olearyf/rLaunchBot/blob/master/images/rLaunchBotProfile.JPG)

# 🛰 About

[@rLaunchBot](https://twitter.com/rLaunchBot) is a Twitter Bot made with Python that usings the [NASA APOD](https://apod.nasa.gov/apod/astropix.html) and [LaunchLibrary](https://launchlibrary.net/docs/1.3/api.html) APIs. It is currently a work in progress, and if you discover any bugs or have any suggestions feel free to DM them to the account! As of right now the bot tweets NASA's APOD everyday at 1 PM EST with the provided explanation as a thread of tweets under the image. In addition to this, everyday at 3 AM EST, the bot gets a list of 5 upcoming rocket launches, tweets any launches that may be happening today, and up to 5 upcoming launches. Right now it is run by 2 scripts I have running on a [Raspberry Pi](https://www.raspberrypi.org/).

## 🐣 Example Launch Tweet

![](https://github.com/olearyf/rLaunchBot/blob/master/images/current_launch.JPG)

## 🐣 Example APOD Tweet

![](https://github.com/olearyf/rLaunchBot/blob/master/images/APOD_thread.JPG)

## 🐣 Example Upcoming Launches Tweet

![](https://github.com/olearyf/rLaunchBot/blob/master/images/upcoming_launches.JPG)

# 🌌 Known Issues/Things I'm Currently Working On

- better parsing and formatting for the explanation for the APOD; right now it just cuts it into chunks that fit into the tweet, whereas ideally it would divide it into whole sentences that fit
- adding in a wiki link to go along with the topic of the APOD
- more information for launches, such as responsible agencies, videos, informational links, ~~photos scraped from a google search~~(Launch Library supplies URLs!), etc
- adding in the ability to reply to a launch with 'Remind me!' and have the bot DM you 1 hour before the launch occurs
- descriptions for launches that have them
- tweet random rocket facts
- consolidate into one master script - for now it's easier to have modular scripts I can tinker with!
