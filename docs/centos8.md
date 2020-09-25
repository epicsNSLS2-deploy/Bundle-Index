# CentOS 8 Bundles

Below is a list of all bundles available for CentOS 8, including included modules and versions, locations, and build configurations and settings.

### ADCore R3-8

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-8/CentOS8`
Build Config Path|`/ad-nfs/epics/production/R3-8/CentOS8/build-config`
Bundle Name|`NSLS2_AD_R3-8_Bin_centos_8_2019-12-27`
installSynApps Version|R2-3-35-geb1c1bf
Python 3 Version|3.6.8
OS Class|centos_8
Build Date|2019-12-27 21:53:04.469329

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout eb1c1bf23ffeafba9a61610bdc678b4ee85e8dc2
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-8/CentOS8/build-config -p
```
Make sure to have Python 3.6.8 installed, and be running on a centos_8 machine

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
stream|2.8.9
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
Location|`/ad-nfs/epics/production/R3-9/CentOS8`
Build Config Path|`/ad-nfs/epics/production/R3-9/CentOS8/build-config`
Bundle Name|`NSLS2_AD_R3-9_Bin_centos_8_2020-02-25`
installSynApps Version|R2-4-6-g6bed0aa
Python 3 Version|3.6.8
OS Class|centos_8
Build Date|2020-02-25 10:47:01.882049

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout 6bed0aac9cf411495714f876a5af8ad7fc8b537a
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-9/CentOS8/build-config -p
```
Make sure to have Python 3.6.8 installed, and be running on a centos_8 machine

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
stream|2.8.9
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
ADPointGrey|R2-9
ADURL|R2-2-19-g35a26df




