# Bundle-Index

A website with a list of available bundles, their contents, and their location.  

https://epicsnsls2-deploy.github.io/Bundle-Index

### Adding Bundle Info

To add additional bundle information to the website, please use the included python script (Requires python3).
Simply run the script with the path to the target bundle as the parameter. For example:
```
./grab_bundle_markdown.py /ad-nfs/epics/production/R3-8/CentOS7/
```
Would print the following:
```
### ADCore R3-8

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-8/CentOS7`
Build Config Path|`/ad-nfs/epics/production/R3-8/CentOS7/build-config`
Bundle Name|`NSLS2_AD_R3-8_Bin_centos_7_2019-11-27`
installSynApps Version|R2-2-76-g0d17e9b
Python 3 Version|3.6.8
OS Class|centos_7
Build Date|2019-11-27 16:04:41.015045

To regenerate sources used to build the bundle, use the following commands:
``
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout -q R2-2-76-g0d17e9b
python3 -u installCLI.py -c `/ad-nfs/epics/production/R3-8/CentOS7/build-config` -p
``
Make sure to have Python 3.6.8 installed, and be running on a centos_7 machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
base|R7.0.3
seq|2.2.6
autosave|R5-10
asyn|R4-37
sscan|R2-11-3
std|R3-6
iocStats|3.1.16
calc|R3-7-3
stream|2.8.9
busy|R1-7
modbus|R3-0
motor|R7-1
ADSupport|R1-9
ADCore|R3-8
quadEM|R9-2
ADUVC|R1-3
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-1
ADProsilica|R2-5
ADSimDetector|R2-10
ADPilatus|R2-7
ADMerlin|R4-1-1-ga0c19c9
ADPointGrey|R2-8
ADVimba|R1-0
ADURL|R2-2-10-gb522aba
```

This should then be copied to the file `docs/centos7.md`, or whichever `.md` file matches your OS distribution. Then, you may test the site with:
```
python3 -m mkdocs build
python3 -m mkdocs serve
```
and opening the supplied `localhost` url in a web browser. Once you are satisfied with the changes, use the `mkdocs built in deploy mechanism:
```
python3 -m mkdocs gh-deploy
```
You will be prompted to enter a username and password for the `Bundle-Index` github repository.
