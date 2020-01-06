# Debian 9 Bundles

Below is a list of all bundles available for Debian 9, including included modules and versions, locations, and build configurations and settings.



### ADCore R3-8

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-8/Debian9`
Build Config Path|`/ad-nfs/epics/production/R3-8/Debian9/build-config`
Bundle Name|`NSLS2_AD_R3-8_Bin_debian_9_2019-12-27`
installSynApps Version|R2-3-35-geb1c1bf
Python 3 Version|3.5.3
OS Class|debian_9
Build Date|2019-12-27 21:34:15.047388

To regenerate sources used to build the bundle, use the following commands:
```
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout eb1c1bf23ffeafba9a61610bdc678b4ee85e8dc2
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-8/Debian9/build-config -p
```
Make sure to have Python 3.5.3 installed, and be running on a debian_9 machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
base|R7.0.3.1
seq|2.2.6
autosave|R5-10
asyn|R4-37
sscan|R2-11-3
std|R3-6-1
iocStats|3.1.16
calc|R3-7-3
stream|2.8.9
busy|R1-7-2
modbus|R3-0-RC1
motor|R7-1
ADSupport|R1-9
ADCore|R3-8
quadEM|R9-2-1
ADUVC|R1-3
ADAndor3|R2-2-11-gb5a0d98
ADGenICam|R1-1
ADProsilica|R2-5
ADSimDetector|R2-10
ADPilatus|R2-7
ADMerlin|R4-1-2-g1e54359
ADPointGrey|R2-8
ADURL|R2-2-10-gb522aba
