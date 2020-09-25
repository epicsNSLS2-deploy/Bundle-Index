# Debian 10 Bundles

Below is a list of all bundles available for Debian 10, including included modules and versions, locations, and build configurations and settings.

### ADCore R3-8

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-8/Debian10`
Build Config Path|`/ad-nfs/epics/production/R3-8/Debian10/build-config`
Bundle Name|`NSLS2_AD_R3-8_Bin_debian_10_2019-12-27`
installSynApps Version|R2-3-35-geb1c1bf
Python 3 Version|3.7.3
OS Class|debian_10
Build Date|2019-12-27 21:40:43.409149

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout eb1c1bf23ffeafba9a61610bdc678b4ee85e8dc2
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-8/Debian10/build-config -p
```
Make sure to have Python 3.7.3 installed, and be running on a debian_10 machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
base|R7.0.3.1
seq|2.2.6
ipac|2.15
asyn|R4-37
autosave|R5-10
busy|R1-7-2
sscan|R2-11-3
calc|R3-7-3
std|R3-6-1
iocStats|3.1.16
stream|2.8.10
ipUnidig|R2-11
modbus|R3-0-RC1
motor|R7-1
xspress3|1-11-205-g011c692
ADSupport|R1-9
ADCore|R3-8
ADUVC|R1-3
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-1
ADProsilica|R2-5
ADSimDetector|R2-10
ADPilatus|R2-7
ADMerlin|R4-1-2-g1e54359
ADPointGrey|R2-8
ADURL|R2-2-10-gb522aba


### ADCore R3-9

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-9/Debian10`
Build Config Path|`/ad-nfs/epics/production/R3-9/Debian10/build-config`
Bundle Name|`NSLS2_AD_R3-9_Bin_debian_10_2020-02-25`
installSynApps Version|R2-4-6-g6bed0aa
Python 3 Version|3.7.3
OS Class|debian_10
Build Date|2020-02-25 10:34:07.323097

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout 6bed0aac9cf411495714f876a5af8ad7fc8b537a
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-9/Debian10/build-config -p
```
Make sure to have Python 3.7.3 installed, and be running on a debian_10 machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
base|R7.0.3.1
seq|2.2.6
ipac|2.15
asyn|R4-39
autosave|R5-10
busy|R1-7-2
sscan|R2-11-3
calc|R3-7-3
std|R3-6-1
iocStats|3.1.16
stream|2.8.10
ipUnidig|R2-11
modbus|R3-0-RC1
motor|R7-1
xspress3|1-11-208-g2783e44
ADSupport|R1-9
ADCore|R3-9
ADUVC|R1-3
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-3
ADProsilica|R2-5
ADSimDetector|R2-10
ADPilatus|R2-9
ADMerlin|R4-1-4-gab6ec75
ADVimba|R1-1-6-ge3ebad8
ADPointGrey|R2-9
ADURL|R2-2-19-g35a26df


### ADCore R3-10

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-10/Debian10`
Build Config Path|`/ad-nfs/epics/production/R3-10/Debian10/build-config`
Bundle Name|`NSLS2_AD_R3-10_Prod_debian_10_2020-09-25`
installSynApps Version|R2-6-29-gb5f2019
Python 3 Version|3.7.3
OS Class|debian_10
Build Date|2020-09-25 17:46:49.849831

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout b5f201951ec052100579eb9c4733d2f153317733
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-10/Debian10/build-config -p
```
Make sure to have Python 3.7.3 installed, and be running on a debian_10 machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
EPICS_BASE|R7.0.4.1-rc1
SNCSEQ|2.2.8
IPAC|2.15
SSCAN|R2-11-3
AUTOSAVE|R5-10-1
CALC|R3-7-3
ASYN|R4-41
BUSY|R1-7-2
STD|R3-6-1
CAPUTRECORDER|R3-1
DAC128V|R2-9
STREAM|2.8.10
DEVIOCSTATS|3.1.16
IPUNIDIG|R2-11
MCA|R7-8
MODBUS|R3-1-6-g8929ff1
MOTOR|R7-2-1
CAMAC|R2-7-2
ADSUPPORT|R1-9
DELAYGEN|R1-2-1
ADCORE|R3-10
QUADEM|R9-3
XSPRESS3|2-3-10-g999592b
ADANDOR3|R2-2-11-gb5a0d98
ADUVC|R1-4
ADGENICAM|R1-5
ADPROSILICA|R2-5
ADSIMDETECTOR|R2-10-18-gd24fa04
ADPILATUS|R2-9
ADMERLIN|R4-1-4-gab6ec75
ADVIMBA|R1-2-1-g84936bc
ADPOINTGREY|R2-9
ADURL|R2-2-23-g031794e


