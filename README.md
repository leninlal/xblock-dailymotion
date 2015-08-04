# xblock-dailymotion
xblock for embedding dailymotion videos in edx-platform

## Install the XBlock
```
# Move to the folder where you want to download the XBlock
cd /edx/app/edxapp
# install XBlock
sudo -u edxapp /edx/bin/pip.edxapp install git+https://github.com/leninlal/xblock-dailymotion.git

```

## Reboot lms and studio
```
sudo /edx/bin/supervisorctl -c /edx/etc/supervisord.conf restart edxapp:

```

## Activate the XBlock in your course
Go to ```Settings -> Advanced Settings``` and set advanced_modules to ```["dailymotion"]```.
