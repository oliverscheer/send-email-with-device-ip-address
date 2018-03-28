# send-email-with-device-ip-address

For headless devices it is hard to be discovered. This small script is fixing the issue, that you don't see the ip-address of your device. 

## To Do's

Create a file called 'secrets.py' and add your personal settings to connect to a mail server. 

``` Python

sender_address = "yourname@gmail.com"
sender_password = "your password"
sender_server = 'smtp.gmail.com'
sender_port = 587
recipient_address = "yourrecipient@outlookc.com"

``` 

check if crontab is installed on your device. 
if not, check that tutorial https://www.raspberrypi.org/documentation/linux/usage/cron.md


## Running it on every start of device

Currently I only this tool on Raspberry Pi's based on Raspbian. So this is the steps you need to install it as startup app. 

``` bash
chmod 755 run.sh
```

Use crontab to schedule script every hour and on reboot

0 * * * * 

Use The '&' for running in background

0 * * * * python /home/pi/apps/send-email-with-device-ip-address/main.py & 

To execute the script on every reboot:

``` shell
sudo nano /etc/rc.local 
``` 
And add the following line to it. The command sleep 30 is necessary to avoid an , because it takes a while to get an valid Ip-address on startup:

``` shell
(sleep 15; python /home/pi/apps/send-email-with-device-ip-address/main.py)&
```

## Feedback is always welcome

If you like to send me comments, feel free to comment.