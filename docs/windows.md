# Windows Bundles

Below is a list of all bundles available for Windows, including included modules and versions, locations, and build configurations and settings.

### ADCore R3-9

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-9/Windows`
Build Config Path|`/ad-nfs/epics/production/R3-9/Windows/build-config`
Bundle Name|`NSLS2_AD_R3-9_Prod_windows-x64-static_2020-07-13`
installSynApps Version|R2-6-16-g5f94b54
Python 3 Version|3.8.3
OS Class|Windows
Build Date|2020-07-13 14:56:31.706234

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout 5f94b54e2bc21d47a214f0b7dc7516a7270425fc
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-9/Windows/build-config -p
```
Make sure to have Python 3.8.3 installed, and be running on a Windows machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
EPICS_BASE|R7.0.4
SNCSEQ|2.2.7
IPAC|2.15
ASYN|R4-39
AUTOSAVE|R5-10-1
BUSY|R1-7-2
SSCAN|R2-11-1
CALC|R3-7-2
DEVIOCSTATS|3.1.16
ADSUPPORT|R1-9
ADCORE|R3-9
ADSPINNAKER|R0.1beta-106-ge0bf1f6
ADANDOR3|R2-2-11-gb5a0d98
ADPERKINELMER|R2-9-6-gbbc467d
ADPROSILICA|R2-5
ADSIMDETECTOR|R2-10
ADPILATUS|R2-9
ADMERLIN|R4-1-4-gab6ec75
ADPOINTGREY|R2-9
ADDEXELA|R2-3
ADURL|R2-2-22-g8ea7846


### ADCore R3-10

Bundle Information:

Variable|Value
------|--------
Location|`/ad-nfs/epics/production/R3-10/Windows`
Build Config Path|`/ad-nfs/epics/production/R3-10/Windows/build-config`
Bundle Name|`NSLS2_AD_R3-10_Prod_windows-x64-static_2020-10-07`
installSynApps Version|R2-6-17-ga6cbeb0
Python 3 Version|3.8.3
OS Class|Windows
Build Date|2020-10-07 14:49:22.828271

To regenerate sources used to build the bundle, use the following commands:
```bash
git clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps
git checkout a6cbeb0cccc42ab5389e0d104f5f3011a2bb7c24
python3 -u installCLI.py -c /ad-nfs/epics/production/R3-10/Windows/build-config -p
```
Make sure to have Python 3.8.3 installed, and be running on a Windows machine

Modules and Versions Included:

Module Name|Module Version
-------|----------
EPICS_BASE|R7.0.4.1-rc1
SNCSEQ|2.2.7
IPAC|2.16
ASYN|R4-41
AUTOSAVE|R5-10-2
BUSY|R1-7-3
SSCAN|R2-11-1
CALC|R3-7-2
DEVIOCSTATS|3.1.16
ADSUPPORT|R1-9
ADCORE|R3-10
ADSPINNAKER|R0.1beta-106-ge0bf1f6
ADANDOR3|R2-2-11-gb5a0d98
ADPERKINELMER|R2-9-6-gbbc467d
ADPROSILICA|R2-5
ADSIMDETECTOR|R2-10
ADPILATUS|R2-9
ADMERLIN|R4-1-4-gab6ec75
ADPOINTGREY|R2-9
ADDEXELA|R2-3
ADURL|R2-2-23-g031794e


