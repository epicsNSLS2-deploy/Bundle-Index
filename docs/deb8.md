# Debian 8 Bundles

Below is a list of all bundles available for Debian 8, including included modules and versions, locations, and build configurations and settings.

### ADCore R3-8

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-8/Debian8`
Build Date|2019-10-22
OS Class|debian_8

Modules and Versions Included:

Module Name|Module Version
-------|----------
Versions used in this deployment|
[folder name]|[git tag]
base|R7.0.3
asyn|R4-37
autosave|R5-10
busy|R1-7
calc|R3-7-3
iocStats|3.1.16
seq|R6-1
sscan|R2-11-3
stream|2.8.9
modbus|R3-0
std|R3-6
xspress3|1-11-187-g39832f6
quadEM|R9-2
ADCore|R3-8
ADSupport|R1-9
ADUVC|R1-3
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-1
ADProsilica|R2-5
ADSimDetector|R2-10
ADPilatus|R2-7
ADMerlin|R4-1-1-ga0c19c9
ADEiger|R2-6
ADPointGrey|R2-8
ADURL|R2-2-10-gb522aba


### ADCore R3-9

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-9/Debian8`
Build Config Path|`/ad-nfs/epics/production/R3-9/Debian8/build-config`
Bundle Name|`NSLS2_AD_R3-9_Bin_debian_8_2020-02-25`
installSynApps Version|R2-4-6-g6bed0aa
Python 3 Version|3.4.2
OS Class|debian_8
Build Date|2020-02-25 10:20:22.370119

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout 6bed0aac9cf411495714f876a5af8ad7fc8b537a
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-9/Debian8/build-config -p
```
Make sure to have Python 3.4.2 installed, and be running on a debian_8 machine

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
xspress3|1-11-208-g2783e44
quadEM|R9-2-1
ADSupport|R1-9
ADCore|R3-9
ADUVC|R1-3
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-3
ADProsilica|R2-5
ADSimDetector|R2-10
ADPilatus|R2-9
ADMerlin|R4-1-4-gab6ec75
ADEiger|R2-6
ADPointGrey|R2-9
ADURL|R2-2-19-g35a26df


### ADCore R3-7

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-7/Debian8`
Build Date|2019-08-29
OS Class|debian_8

Modules and Versions Included:

Module Name|Module Version
-------|----------
Versions used in this deployment|
[folder name]|[git tag]
base|R7.0.3
asyn|R4-36
autosave|R5-10
busy|R1-7
calc|R3-7-3
iocStats|3.1.16
seq|R6-1
sscan|R2-11-3
stream|2.8.9
modbus|R3-0
std|R3-6
xspress3|1-11-176-g750cd39
quadEM|R9-2
ADCore|R3-7
ADSupport|R1-9
ADUVC|R1-2
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-0
ADProsilica|R2-5
ADSimDetector|R2-9
ADPilatus|R2-7
ADMerlin|R4-1-1-ga0c19c9
ADEiger|R2-6
ADPointGrey|R2-8
ADURL|R2-2-10-gb522aba
ADPSL|R2-1-3-ge5443ec






### ADCore R3-10

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-10/Debian8`
Build Config Path|`/ad-nfs/epics/production/R3-10/Debian8/build-config`
Bundle Name|`NSLS2_AD_R3-10_Prod_debian_8_2020-09-25`
installSynApps Version|R2-6-29-gb5f2019
Python 3 Version|3.4.2
OS Class|debian_8
Build Date|2020-09-25 17:38:10.758196

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout b5f201951ec052100579eb9c4733d2f153317733
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-10/Debian8/build-config -p
```
Make sure to have Python 3.4.2 installed, and be running on a debian_8 machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
EPICS_BASE|R7.0.4.1-rc1
IPAC|2.15
SNCSEQ|2.2.8
AUTOSAVE|R5-10-1
SSCAN|R2-11-3
CALC|R3-7-3
ASYN|R4-41
CAPUTRECORDER|R3-1
DAC128V|R2-9
STREAM|2.8.9
DEVIOCSTATS|3.1.16
DELAYGEN|R1-2-1
IPUNIDIG|R2-11
BUSY|R1-7-2
MODBUS|R3-1-6-g8929ff1
STD|R3-6-1
CAMAC|R2-7-2
ADSUPPORT|R1-9
ADCORE|R3-10
QUADEM|R9-3
ADANDOR3|R2-2-11-gb5a0d98
ADUVC|R1-4
ADGENICAM|R1-5
ADPROSILICA|R2-5
ADSIMDETECTOR|R2-10-18-gd24fa04
ADPILATUS|R2-9
ADMERLIN|R4-1-4-gab6ec75
ADPOINTGREY|R2-9
ADURL|R2-2-23-g031794e


