# CentOS 7 Bundles

Below is a list of all bundles available for CentOS 7, including included modules and versions, locations, and build configurations and settings.

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
```
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout -q R2-2-76-g0d17e9b
python3 -u installCLI.py -c `/ad-nfs/epics/production/R3-8/CentOS7/build-config` -p
```
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



### ADCore R3-9

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-9/CentOS7`
Build Config Path|`/ad-nfs/epics/production/R3-9/CentOS7/build-config`
Bundle Name|`NSLS2_AD_R3-9_Bin_centos_7_2020-02-25`
installSynApps Version|R2-4-6-g6bed0aa
Python 3 Version|3.6.8
OS Class|centos_7
Build Date|2020-02-25 10:40:25.092761

To regenerate sources used to build the bundle, use the following commands:
```
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout 6bed0aac9cf411495714f876a5af8ad7fc8b537a
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-9/CentOS7/build-config -p
```
Make sure to have Python 3.6.8 installed, and be running on a centos_7 machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
base|R7.0.3.1
seq|2.2.6
autosave|R5-10
asyn|R4-39
sscan|R2-11-3
std|R3-6-1
iocStats|3.1.16
calc|R3-7-3
stream|2.8.9
busy|R1-7-2
modbus|R3-0-RC1
motor|R7-1
ADSupport|R1-9
ADCore|R3-9
quadEM|R9-2-1
ADUVC|R1-3
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-3
ADProsilica|R2-5
ADSimDetector|R2-10
ADPilatus|R2-9
ADMerlin|R4-1-4-gab6ec75
ADPointGrey|R2-9
ADVimba|R1-1-6-ge3ebad8
ADURL|R2-2-19-g35a26df

