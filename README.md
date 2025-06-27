Attempt to create a minimal EDK2 for the iPhone 5s

## Status
Gets stuck in DxeMain at line 336: PERF_CROSSMODULE_END ("PEI");

### Building
Tested on Ubuntu 24.04.

First, clone EDK2.

```
cd ..
git clone https://github.com/tianocore/edk2 --recursive -b edk2-stable202302
git clone https://github.com/tianocore/edk2-platforms.git
```

You should have all three directories side by side.

Next, install dependencies:

24.04:

```
sudo apt install build-essential uuid-dev iasl git nasm python3-distutils gcc-aarch64-linux-gnu
```

Also see [EDK2 website](https://github.com/tianocore/tianocore.github.io/wiki/Using-EDK-II-with-Native-GCC#Install_required_software_from_apt)

### Running EDK2 in your 5s

Grab PongoOS from my repo, boot the UEFI image in workspace/UEFI from pongo.

# Credits

SimpleFbDxe screen driver is from imbushuo's [Lumia950XLPkg](https://github.com/WOA-Project/Lumia950XLPkg).

Zhuowei for making edk2-pixel3

All the people in ``EDKII pain and misery, struggles and disappointment`` on Discord.
