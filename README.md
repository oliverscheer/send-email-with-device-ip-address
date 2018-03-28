# send-email-with-device-ip-address

Where is my Raspberry Pi? Let your Pi send you an email with its IP-address. A few simple lines of Python Code can make your developer life much easier.

A very common challenge for Pi Developer is the challenge, that the Pi does not have a display build in. You can buy very good, and cheap Touchdisplays for the Pi to get rid of that problem. But if you’re using your Pi as “hiddden” device or on board of a car like my Sunfounder Pi Car, you cannot attach easily a display or HDMI cable, without disambling the whole car.

![Sunfounder Raspberry Pi Car](/images/picar.jpeg)

Even if you manage to attach a monitor to this car, it is really annoying and uncomfortable to run after your driving car carrying the monitor all the time.

![Email from my car](/images/email.png)

## Prerequisities

The following project is writen in Python 3. So you will need Python 3 on your machine. The easiest way to install it is, executing the following lines in a command shell.

``` bash
sudo apt-get install python-dev
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
``` 

If you don't want to use your personal email account & password on the device, you should create a new mailbox for that, I suggest GMail, but it is up to you. The only requirement is, that it is accessible via smtp.

## Installation 

You only need the file ```main.py``` locally on your Raspberry Pi device. I copied it in to the folder `/home/pi/apps/send-email-with-device-ip-address/`

You can add your credentials directly to access the mail server there, or create a file called 'secrets.py' and add your personal settings to connect to a mail server. I used that way and gitignored this file to keep my credentials away from your eyes.

``` Python
sender_address = "yourname@gmail.com"
sender_password = "your password"
sender_server = 'smtp.gmail.com'
sender_port = 587
recipient_address = "yourrecipient@outlookc.com"
``` 

## Test it!

Before you add this file to the boot sequence or cronjob, please test the file by executing the following line in the command shell:

``` shell
python /home/pi/apps/send-email-with-device-ip-address/main.py
``` 

And it should display you something like that: 

![Output of Python App on Pi](/images/output.png)

Sending the email takes up to two minutes. I currently haven't exactly figured out, why it takes so long.

## Running it on every start of device

Currently I only use this tool on Raspberry Pi's based on Raspbian. So this is the steps you need to install it as startup app. 

To execute the script on every reboot, you need to add the python app to the `rc.local` file. 

``` shell
sudo nano /etc/rc.local 
``` 
Add the following line to it. The command `sleep 30` is necessary to avoid an error on start, because it takes a while to get an valid IP-address on startup. Use The '&' for running in background.

``` shell
(sleep 30; python /home/pi/apps/send-email-with-device-ip-address/main.py)&
```

Test it, but simply rebooting your system with 

```
sudo reboot
```

You should receive an email within two minutes. 

## Running it every hour

In some scenarios it is useful to get an update of the current ip address every hour. Under some conditions ip addressses can change. 

``` shell
sudo nano /etc/crontab
```

Add the following line to get updates every hour:
```
0 * * * * root python /home/pi/apps/send-email-with-device-ip-address/main.py &


```

To test this feature, you need to wait until the next full hour. 

# Summary

This small tutorial should help you getting an ip address from an headless device. You can use the ip address to access the device like a Raspberry Pi with Putty or other ssh tools.

Feedback is always welcome, please feel free to comment.

