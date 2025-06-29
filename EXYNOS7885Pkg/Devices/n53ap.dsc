[Defines]
  PLATFORM_NAME                  = EXYNOS7885Pkg
  PLATFORM_GUID                  = 28f1a3bf-193a-47e3-a7b9-5a435eaab2ee
  PLATFORM_VERSION               = 0.1
  DSC_SPECIFICATION              = 0x00010019
  OUTPUT_DIRECTORY               = Build/$(PLATFORM_NAME)
  SUPPORTED_ARCHITECTURES        = AARCH64
  BUILD_TARGETS                  = DEBUG|RELEASE
  SKUID_IDENTIFIER               = DEFAULT
  FLASH_DEFINITION               = EXYNOS7885Pkg/EXYNOS7885Pkg.fdf

!include EXYNOS7885Pkg/EXYNOS7885Pkg.dsc

[PcdsFixedAtBuild.common]
  # System Memory (1GB)
  gArmTokenSpaceGuid.PcdSystemMemoryBase|0x800000000
  gArmTokenSpaceGuid.PcdSystemMemorySize|0x40000000
  gEXYNOS7885PkgTokenSpaceGuid.PcdPrePiStackBase|0x800600000
  gEmbeddedTokenSpaceGuid.PcdPrePiStackSize|0x00040000      # 256K stack
  gArmTokenSpaceGuid.PcdCpuVectorBaseAddress|0x800640000
  gEXYNOS7885PkgTokenSpaceGuid.PcdUefiMemPoolBase|0x800850000         # DXE Heap base address
  gEXYNOS7885PkgTokenSpaceGuid.PcdUefiMemPoolSize|0x003300000         # UefiMemorySize, DXE heap size

  # Framebuffer (720x1280)
  gEXYNOS7885PkgTokenSpaceGuid.PcdMipiFrameBufferAddress|0x83ee00000
  gEXYNOS7885PkgTokenSpaceGuid.PcdMipiFrameBufferWidth|640
  gEXYNOS7885PkgTokenSpaceGuid.PcdMipiFrameBufferHeight|1136
  gEXYNOS7885PkgTokenSpaceGuid.PcdMipiFrameBufferVisibleWidth|640
  gEXYNOS7885PkgTokenSpaceGuid.PcdMipiFrameBufferVisibleHeight|1136
