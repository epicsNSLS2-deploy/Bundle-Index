# Debian 8 Bundles

Below is a list of all bundles available for Debian 8, including included modules and versions, locations, and build configurations and settings.


### ADCore R3-8

Bundle information:

Variable | Value
------|----------------
Location|`/ad-nfs/epics/production/R3-8/Debian8`
Build Python Version|3.4.2
Bundle Name|`NSLS2_AD_R3-8_Bin_debian_8_2019-10-22`
Build Date|2019-10-22

Versions used in this deployment:

[folder name] | [git tag]
------|------------------
base | R7.0.3
asyn | R4-37
autosave | R5-10
busy | R1-7
calc | R3-7-3
iocStats | 3.1.16
seq | R6-1
sscan | R2-11-3
stream | 2.8.9
modbus | R3-0
std | R3-6
xspress3 | 1-11-187-g39832f6
quadEM | R9-2
ADCore | R3-8
ADSupport | R1-9
ADUVC | R1-3
ADAndor3 | R2-2-11-gb5a0d98
ADGenICam | R1-1
ADProsilica | R2-5
ADSimDetector | R2-10
ADPilatus | R2-7
ADMerlin | R4-1-1-ga0c19c9
ADEiger | R2-6
ADPointGrey | R2-8
ADURL | R2-2-10-gb522aba



### ADCore R3-9

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production//./R3-9/Debian8`
Build Config Path|`/ad-nfs/epics/production//./R3-9/Debian8/build-config`
Bundle Name|`NSLS2_AD_R3-9_Bin_debian_8_2020-02-25`
installSynApps Version|R2-4-6-g6bed0aa
Python 3 Version|3.4.2
OS Class|debian_8
Build Date|2020-02-25 10:20:22.370119

To regenerate sources used to build the bundle, use the following commands:
```
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout 6bed0aac9cf411495714f876a5af8ad7fc8b537a
python3 -u installCLI.py -c /ad-nfs/epics/production//./R3-9/Debian8/build-config -p
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

