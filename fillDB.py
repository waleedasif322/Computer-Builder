import sys
import os
import os.path

moboList = [
[" ASUS A55M-A FM2 AMD A55 (Hudson D2) HDMI Micro ATX Native HDMI/DVI Outputs AMD Motherboard With UEFI BIOS ", 59.99 ],
[" ASUS M5A78L-M LX PLUS AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 56.99 ],
[" ASRock AM1B-M AM1 SATA 6Gb/s USB 3.0 Micro ATX AMD Motherboard ", 33.99 ],
[" BIOSTAR A960D+ AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 69.49 ],
[" Open Box: ASUS M5A78L-M LX PLUS AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 59.99 ],
[" ECS A55F2-M4(1.0) FM2 AMD A55 (Hudson D2) Micro ATX AMD Motherboard ", 45.99 ],
[" ASUS A55BM-A/USB3 FM2+ / FM2 AMD A55 (Hudson D2) USB 3.0 HDMI Micro ATX AMD Motherboard ", 69.99 ],
[" ASUS A88XM-PLUS/CSM FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 89.99 ],
[" MSI A88X-G45 GAMING FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard (Assassins creed limited edition) ", 119.99 ],
[" ASRock AM1B-ITX AM1 SATA 6Gb/s USB 3.0 HDMI Mini ITX AMD Motherboard ", 39.99 ],
[" ASUS A55M-A/USB3 FM2 AMD A55 (Hudson D2) USB 3.0 HDMI Micro ATX USB 3.0 and Native HDMI/DVI Outputs AMD Motherboard With UEFI BIOS ", 69.99 ],
[" GIGABYTE GA-F2A55M-S1 FM2+ AMD A55 (Hudson D2) Micro ATX AMD Motherboard ", 49.99 ],
[" For arduino Nano 3.0 Atmel ATmega328 Mini-USB Board with USB Cable BEST PRICE ", 19.99 ],
[" BIOSTAR Hi-Fi A85W FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 79.99 ],
[" ASRock 970 Extreme3 R2.0 AM3+ AMD 970 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 94.99 ],
[" MSI 990FXA-GD80 V2 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 169.09 ],
[" ASUS A55BM-PLUS/CSM FM2+ / FM2 AMD A55 (Hudson D2) USB 3.0 HDMI Micro ATX AMD Motherboard ", 69.89 ],
[" ECS A75F2-M FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 69.99 ],
[" ASRock FM2A75 PRO4+ FM2+ / FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 74.99 ],
[" ECS A75F2-M2(1.0A) FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 65.99 ],
[" ASUS A88X-PRO FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI AMD Motherboard ", 128.99 ],
[" MSI A88X-G41 PC Mate FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 72.99 ],
[" MSI A88XM GAMING FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 109.99 ],
[" GIGABYTE GA-F2A55M-HD2 FM2 AMD A55 (Hudson D2) HDMI Micro ATX AMD Motherboard ", 59.99 ],
[" ASUS M5A99X EVO R2.0 AM3+ AMD 990X + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 139.99 ],
[" GIGABYTE GA-970A-D3P AM3+/AM3 AMD 970 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 94.99 ],
[" GIGABYTE GA-78LMT-S2 AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 47.99 ],
[" ASRock A785GM-LE AM3/AM2+/AM2 AMD 785G + SB710 Micro ATX AMD Motherboard ", 58.99 ],
[" MSI A88XM-E35 FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 67.99 ],
[" ASRock FM2A88M-HD+ FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 69.29 ],
[" GIGABYTE GA-F2A88XM-HD3 FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 72.79 ],
[" Open Box: ASUS M5A78L-M/USB3 AM3+ AMD 760G + SB710 USB 3.0 HDMI uATX AMD Motherboard ", 76.49 ],
[" GIGABYTE GA-F2A88XM-D3H FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 84.99 ],
[" ASRock FM2A88M Extreme4+ FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 84.99 ],
[" ASRock AM1H-ITX AM1 HDMI SATA 6Gb/s USB 3.0 DC-In/ATX Power Input Mini ITX AMD Motherboard ", 58.99 ],
[" GIGABYTE GA-F2A88X-UP4 FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 109.99 ],
[" BIOSTAR A780L3C AM3 Micro ATX AMD Motherboard ", 37.89 ],
[" ASRock 880GM-LE FX AM3+ AMD 880G + SB710 Micro ATX AMD Motherboard ", 58.99 ],
[" ASUS AM1M-A AM1 SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 49.99 ],
[" ASUS A55M-E FM2 AMD A55 (Hudson D2) Micro ATX AMD Motherboard With UEFI BIOS ", 54.99 ],
[" BIOSTAR TA970 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 79.99 ],
[" MSI A55M-E35 FM2+ / FM2 AMD A55 (Hudson D2) HDMI Micro ATX AMD Motherboard ", 52.79 ],
[" GIGABYTE GA-A75-UD4H FM1 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 109.69 ],
[" ASUS F2A85-M PRO FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 94.99 ],
[" ASRock 990FX Extreme3 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 119.99 ],
[" GIGABYTE GA-990FXA-UD3 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 148.0 ],
[" ECS A55F2-M3(1.0) FM2 AMD A55 (Hudson D2) HDMI Micro ATX AMD Motherboard ", 48.99 ],
[" MSI A88XI AC FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Mini ITX AMD Motherboard ", 99.99 ],
[" GIGABYTE GA-F2A88XN-WIFI FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Mini ITX AMD Motherboard ", 109.69 ],
[" Open Box: ASUS Crosshair V Formula-Z AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Gaming Motherboard with 3-Way SLI/CrossFireX Support and UEFI BIOS ", 239.99 ],
[" ASUS A55BM-K FM2+ AMD A55 (Hudson D2) Micro ATX AMD Motherboard ", 54.49 ],
[" GIGABYTE GA-AM1M-S2H AM1 SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 34.99 ],
[" ASRock 990FX Extreme9 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 189.99 ],
[" GIGABYTE GA-F2A78M-HD2 FM2+ AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 62.99 ],
[" MSI 760GM-P23 (FX) AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 50.02 ],
[" ASRock FM2A78M-ITX+ FM2+ / FM2 AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Mini ITX AMD Motherboard ", 94.99 ],
[" MSI 970A-G46 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 79.99 ],
[" ASUS M5A78L-M/USB3 AM3+ AMD 760G + SB710 USB 3.0 HDMI uATX AMD Motherboard ", 64.79 ],
[" ASRock Fatal1ty 990FX Killer AM3+ AMD 990FX SATA 6Gb/s USB 3.0 ATX AMD Gaming Motherboard ", 144.99 ],
[" ASRock 980DE3/U3S3 AM3+ AMD RX881/760G SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 69.99 ],
[" ASUS SABERTOOTH 990FX R2.0 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 184.49 ],
[" GIGABYTE GA-G1.Sniper A88X FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 114.99 ],
[" MSI A55M-P33 FM1 AMD A55 (Hudson D2) Micro ATX AMD Motherboard with UEFI BIOS ", 47.99 ],
[" ASRock 960GM/U3S3 FX AM3+ AMD 760G + SB710 SATA 6Gb/s USB 3.0 Micro ATX AMD Motherboard ", 59.99 ],
[" ASUS A55BM-E FM2+ / FM2 AMD A55 (Hudson D2) Micro ATX AMD Motherboard ", 59.99 ],
[" GIGABYTE GA-78LMT-S2P(rev 5.0) AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 57.79 ],
[" ASRock FM2A55M-VG3+ FM2+ 95W / FM2 100W AMD A55 (Hudson D2) Micro ATX AMD Motherboard with UEFI BIOS ", 42.99 ],
[" MSI 990FXA-GD65V2 Desktop Motherboard - AMD 990FX Chipset - Socket AM3+ ", 132.99 ],
[" ASRock FM2A78M-HD+ FM2+ / FM2 AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 59.99 ],
[" Open Box: ASUS A55BM-PLUS/CSM FM2+ / FM2 AMD A55 (Hudson D2) USB 3.0 HDMI Micro ATX AMD Motherboard ", 59.49 ],
[" ASUS M5A97 LE R2.0 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 89.99 ],
[" ASUS A88XM-A FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard with UEFI BIOS ", 84.99 ],
[" BIOSTAR TA75M+ FM1 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 74.99 ],
[" ASRock FM2A75M Pro4+ FM2+ / FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 74.99 ],
[" BIOSTAR AM1ML AM1 SATA 6Gb/s USB 3.0 Micro ATX AMD Motherboard ", 32.99 ],
[" ASRock 970 EXTREME4 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 99.49 ],
[" ASRock FM2A88X Extreme6+ FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 114.79 ],
[" ASRock Fatal1ty FM2A88X+ Killer FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Gaming Motherboard ", 109.99 ],
[" Open Box: ASUS F2A55-M/CSM FM2 AMD A55 (Hudson D2) USB 3.0 HDMI Micro ATX AMD Motherboard with UEFI BIOS ", 84.99 ],
[" ASRock FM2A88X Extreme4+ FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 84.99 ],
[" ASUS Crosshair V Formula-Z AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Gaming Motherboard with 3-Way SLI/CrossFireX Support and UEFI BIOS ", 239.99 ],
[" ASRock A55M-VS FM1 AMD A55 (Hudson D2) Micro ATX AMD Motherboard ", 46.99 ],
[" ASUS A78M-A FM2+ AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 69.79 ],
[" ASUS M5A99FX PRO R2.0 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 149.99 ],
[" GIGABYTE GA-78LMT-USB3 AM3+ AMD 760G + SB710 USB 3.0 HDMI Micro ATX AMD Motherboard ", 68.29 ],
[" BIOSTAR A88M FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 Micro ATX AMD Motherboard ", 64.99 ],
[" GIGABYTE GA-970A-UD3P AM3+ AMD 970 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 109.99 ],
[" GIGABYTE GA-F2A55M-DS2 FM2 AMD A55 (Hudson D2) Micro ATX AMD Motherboard with UEFI BIOS ", 57.99 ],
[" MSI A88X-G43 FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 82.99 ],
[" MSI A78M-E45 FM2+ / FM2 AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 67.99 ],
[" GIGABYTE GA-990FXA-UD7 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 Extended ATX AMD Motherboard ", 249.99 ],
[" ASRock 970 PRO3 R2.0 AM3+ AMD 970 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 74.99 ],
[" GIGABYTE GA-970A-DS3P AM3+ AMD 970 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 79.99 ],
[" ECS A960M-MV(1.0A) AM3+ AMD 760G HDMI Micro ATX AMD Motherboard ", 44.49 ],
[" ASRock 960GC-GS FX AM3+/AM3/AM2+ AMD 760G Micro ATX AMD Motherboard ", 49.99 ],
[" MSI A88XM-E45 FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 72.99 ],
[" ASRock FM2A88X-ITX+ FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Mini ITX AMD Motherboard ", 98.99 ],
[" MSI A55M-E33 FM2+ / FM2 AMD A55 (Hudson D2) HDMI Micro ATX AMD Motherboard ", 49.99 ],
[" MSI 970A-G43 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 69.99 ],
[" BIOSTAR Hi-Fi A85S3 FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 69.99 ],
[" GIGABYTE GA-990FXA-UD5 AM3+ AMD 990FX SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 174.79 ],
[" GIGABYTE GA-F2A78M-D3H FM2+ / FM2 AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 74.09 ],
[" Open Box: ASUS F2A85-V FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard with UEFI BIOS ", 119.99 ],
[" ASUS A88X-PLUS FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 104.49 ],
[" Open Box: ASRock Fatal1ty 990FX Killer AM3+ AMD 990FX SATA 6Gb/s USB 3.0 ATX AMD Gaming Motherboard ", 114.74 ],
[" BIOSTAR AM1MHP AM1 SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 34.99 ],
[" GIGABYTE GA-F2A88X-D3H FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 87.49 ],
[" MSI A78M-E35 FM2+ / FM2 AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 62.99 ],
[" ASRock FM2A55M-HD+ FM2+ / FM2 AMD A55 (Hudson D2) HDMI Micro ATX AMD Motherboard ", 49.99 ],
[" GIGABYTE GA-F2A88XM-DS2 FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 Micro ATX AMD Motherboard ", 79.99 ],
[" Open Box: ASUS A78M-A FM2+ AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 59.32 ],
[" Open Box: ASUS F2A85-M PRO FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 129.99 ],
[" ASUS AM1I-A AM1 SATA 6Gb/s USB 3.0 HDMI Mini ITX AMD Motherboard ", 54.99 ],
[" ASUS M5A97 R2.0 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 99.79 ],
[" MSI 760GM-P34 (FX) AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 52.99 ]]


cpuList = [
[" AMD A6-6400K Richland 3.9GHz Socket FM2 65W Desktop Processor - Black Edition AMD Radeon HD AD640KOKHLBOX ", 64.99 ],
[" AMD Athlon X2 370K Richland 4.0GHz Socket FM2 65W Desktop Processor AD370KOKHLBOX ", 58.99 ],
[" AMD A4-6320 Richland 3.8GHz Socket FM2 65W Desktop Processor AMD Radeon HD8000 Series AD6320OKHLBOX ", 59.99 ],
[" AMD A4-4000 Richland 3.2GHz Socket FM2 65W Desktop Processor AD4000OKHLBOX ", 44.99 ],
[" Intel Core i7-4930K Ivy Bridge-E 3.4GHz LGA 2011 130W Desktop Processor BX80633i74930K ", 579.99 ],
[" AMD A8-5600K Trinity 3.6GHz (3.9GHz Turbo) Socket FM2 100W Desktop APU (CPU + GPU) with DirectX 11 Graphic AMD Radeon HD 7560D AD560KWOHJBOX ", 99.99 ],
[" AMD Athlon X4 740 Trinity 3.2GHz Socket FM2 65W Desktop Processor AD740XOKHJBOX ", 74.99 ],
[" Intel Core i3-4340 Haswell 3.6GHz LGA 1150 54W Desktop Processor Intel HD Graphics 4600 BX80646I34340 ", 159.99 ],
[" AMD A4-4020 Richland 3.2GHz Socket FM2 65W Desktop Processor AMD Radeon HD7000 Series AD4020OKHLBOX ", 49.99 ],
[" AMD FX-6350 Vishera 3.9GHz Socket AM3+ 125W Desktop Processor FD6350FRHKBOX ", 139.99 ],
[" Intel Core i7-3930K Sandy Bridge-E 3.2GHz (3.8GHz Turbo) LGA 2011 130W Desktop Processor BX80619i73930K ", 589.99 ],
[" Intel Pentium G2030 Ivy Bridge 3.0GHz LGA 1155 55W Desktop Processor Intel HD Graphics BX80637G2030 ", 69.99 ],
[" AMD FX-9370 Vishera 4.4GHz Socket AM3+ 220W Desktop Processor - Black Edition FD9370FHHKWOF ", 249.99 ],
[" Intel Core i7-4820K Ivy Bridge-E 3.7GHz (Turbo 3.9GHz) LGA 2011 130W Desktop Processor BX80633i74820K ", 324.99 ],
[" Intel Core i3-2120 Sandy Bridge 3.3GHz LGA 1155 65W Desktop Processor Intel HD Graphics 2000 BX80623I32120 ", 124.99 ],
[" Intel Core i5 3470S Ivy Bridge 2.9GHz LGA 1155 65W Desktop Processor Intel HD Graphics 2500 BX80637I53470S ", 204.99 ],
[" AMD A4-5300 Trinity 3.4GHz (3.6GHz Turbo) Socket FM2 65W Desktop APU (CPU + GPU) with DirectX 11 Graphic AMD Radeon HD 7480D AD5300OKHJBOX ", 54.99 ],
[" Intel Pentium G3420 Haswell 3.2GHz LGA 1150 54W Desktop Processor Intel HD Graphics BX80646G3420 ", 74.99 ],
[" AMD FX-6300 Vishera 3.5GHz (4.1GHz Turbo) Socket AM3+ 95W Desktop Processor FD6300WMHKBOX ", 119.99 ],
[" Intel Core i3-3225 Ivy Bridge 3.3GHz LGA 1155 55W Desktop Processor                                                                                   Intel HD Graphics 4000 BX80637I33225 ", 139.99 ],
[" AMD A10-5800K Trinity 3.8GHz (4.2GHz Turbo) Socket FM2 100W Desktop APU (CPU + GPU) with DirectX 11 Graphic AMD Radeon HD 7660D AD580KWOHJBOX ", 119.99 ],
[" AMD FX-4350 Vishera 4.2GHz Socket AM3+ 125W Desktop Processor FD4350FRHKBOX ", 139.99 ],
[" AMD A6-5400K Trinity 3.6GHz (3.8GHz Turbo) Socket FM2 65W Desktop APU (CPU + GPU) with DirectX 11 Graphic AMD Radeon HD 7540D AD540KOKHJBOX ", 64.99 ],
[" AMD FX-8320 Vishera 3.5GHz (4.0GHz Turbo) Socket AM3+ 125W Desktop Processor FD8320FRHKBOX ", 159.99 ],
[" AMD A4-3300 Llano 2.5GHz Socket FM1 65W Desktop APU (CPU + GPU) with DirectX 11 Graphic AMD Radeon HD 6410D AD3300OJHXBOX ", 44.99 ],
[" Intel Core i5-4440S Haswell 2.8GHz (3.3GHz Turbo) LGA 1150 65W Desktop Processor Intel HD Graphics 4600 BX80646I54440S ", 199.99 ],
[" Intel Core i5-3570 Ivy Bridge 3.4GHz (3.8GHz Turbo Boost) LGA 1155 77W Desktop Processor Intel HD Graphics 2500 BX80637i53570 ", 209.99 ],
[" Intel Core i5-4670K Haswell 3.4GHz LGA 1150 84W Desktop Processor Intel HD Graphics BX80646I54670K ", 249.99 ],
[" AMD Athlon X2 340 Trinity 3.2GHz Socket FM2 65W Desktop Processor AD340XOKHJBOX ", 44.99 ],
[" Intel Core i5-3470 Ivy Bridge 3.2GHz (3.6GHz Turbo Boost) LGA 1155 77W Desktop Processor Intel HD Graphics 2500 BX80637i53470 ", 189.99 ],
[" Intel Core i7-4770 Haswell 3.4GHz LGA 1150 84W Desktop Processor Intel HD Graphics BX80646I74770 ", 309.99 ],
[" AMD A10-6800K Richland 4.1GHz (4.4GHz Turbo) Socket FM2 100W Quad-Core Desktop Processor - Black Edition AMD Radeon HD 8670D ", 139.99 ],
[" Intel Core i3-4330 Haswell 3.5GHz LGA 1150 54W Desktop Processor Intel HD Graphics 4600 BX80646I34330 ", 139.99 ],
[" Intel Core i7-3770 Ivy Bridge 3.4GHz (3.9GHz Turbo) LGA 1155 77W Desktop Processor Intel HD Graphics 4000 BX80637I73770 ", 299.99 ],
[" AMD Athlon 5350 Kabini 2.05GHz Socket AM1 25W Desktop Processor AMD Radeon HD 8400 AD5350JAHMBOX ", 64.99 ],
[" Intel Celeron G540 Sandy Bridge 2.5GHz LGA 1155 65W Desktop Processor Intel HD Graphics BX80623G540 ", 49.99 ],
[" Intel Core i7-4770K Haswell 3.5GHz LGA 1150 84W Desktop Processor Intel HD Graphics BX80646I74770K ", 349.99 ],
[" AMD Sempron 2650 Kabini 1.4GHz Socket AM1 25W Desktop Processor AMD Radeon HD 8240 SD2650JAHMBOX ", 39.99 ],
[" AMD A8-5500 Trinity 3.2GHz (3.7GHz Turbo) Socket FM2 65W Desktop APU (CPU + GPU) with DirectX 11 Graphic AMD Radeon HD 7560D AD5500OKHJBOX ", 98.99 ],
[" Intel Core i3-2105 Sandy Bridge 3.1GHz LGA 1155 65W Desktop Processor Intel HD Graphics 3000 BX80623I32105 ", 145.99 ],
[" Intel Core i3-4130 Haswell 3.4GHz LGA 1150 54W Desktop Processor Intel HD Graphics 4400 BX80646I34130 ", 124.99 ],
[" Intel Celeron G1830 Haswell 2.8GHz LGA 1150 54W Desktop Processor Intel HD Graphics BX80646G1830 ", 59.99 ],
[" AMD Athlon 5150 Kabini 1.6GHz Socket AM1 25W Desktop Processor AMD Radeon HD 8400 AD5150JAHMBOX ", 54.99 ],
[" Intel Pentium G2130 Ivy Bridge 3.2GHz LGA 1155 55W Desktop Processor BX80637G2130 ", 72.99 ]]

memList = [
[" 1GB RAM Memory Dell Inspiron 530 PC2-6400 DDR2 ", 18.86 ],
[" 2GB (2X1GB) DDR Memory Acer AcerPower S285 Series ", 32.45 ],
[" 2GB (2X1GB) DDR Memory ASUS PC-DL Deluxe ", 32.45 ],
[" 4GB 4x1GB IBM Intellistation M Pro Type 6230 Memory ", 61.07 ],
[" HyperX Predator Series 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2666 Desktop Memory Model KHX26C11T2K2/8X ", 107.99 ],
[" Team Vulcan 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model TLD316G2133HC10QDC01 ", 159.99 ],
[" Team Vulcan 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model TLD316G2400HC11CDC01 ", 139.99 ],
[" SUPER TALENT 512MB 184-Pin DDR SDRAM DDR 400 (PC 3200) System Memory Model D32PA512N ", 48.63 ],
[" CORSAIR Vengeance 32GB (4 x 8GB) 240-Pin DDR3 SDRAM DDR3 1866 Desktop Memory Model CMZ32GX3M4X1866C10 ", 349.99 ],
[" SUPER TALENT 512MB 184-Pin DDR SDRAM DDR 400 (PC 3200) Desktop Memory Model D32PA12H ", 49.63 ],
[" Patriot Signature 8GB 240-Pin DDR3 SDRAM DDR3 1333 (PC3 10600) Desktop Memory Model PSD38G13332 ", 74.99 ],
[" CORSAIR XMS3 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2000 (PC3 16000) Desktop Memory Model CMX8GX3M2A2000C9 ", 119.99 ],
[" CORSAIR XMS 8GB 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CMX8GX3M1A1600C11 ", 89.99 ],
[" Team Vulcan 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model TLAD316G2400HC11CDC01 ", 154.99 ],
[" Crucial 2GB 240-Pin DDR2 SDRAM DDR2 1066 (PC2 8500) Desktop Memory Model CT25664AA1067 ", 45.99 ],
[" HyperX Black 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model KHX16C10B1BK2/16X ", 179.99 ],
[" 2GB MEMORY 256X64 PC3-8500 1066MHZ 1.5V NON ECC DDR3 240 PIN DIMM ", 30.0 ],
[" Kingston Kvr400D2E3/512 Ddr2-400 512Mb Ecc Cl3 Server Memory Module ", 39.17 ],
[" HyperX Blu 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1333 Desktop Memory Model KHX13C9B1K2/16 ", 176.99 ],
[" SUPER TALENT 512MB 184-Pin DDR SDRAM DDR 333 (PC 2700) System Memory Model D27PA512N ", 49.97 ],
[" HyperX Blu 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1333 Desktop Memory Model KHX1333C9D3B1K2/8G ", 84.99 ],
[" Ddr3-1600 Sodimm 4Gb/512Mx8 Notebook Memory ", 71.85 ],
[" Crucial Ballistix 4GB 240-Pin DDR3 SDRAM DDR3 1866 (PC3 14900) Desktop Memory Model BLE4G3D1869DE1TX0 ", 64.68 ],
[" CORSAIR Vengeance 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 (PC3 15000) Desktop Memory Model CMZ8GX3M2A1866C9R ", 86.99 ],
[" G.SKILL Ripjaws Z Series 64GB (8 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model F3-12800CL10Q2-64GBZL ", 599.99 ],
[" Visiontek 4GB 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model 900383 ", 54.99 ],
[" Mushkin Enhanced Redline 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model 997084 ", 89.99 ],
[" 8GB (4X2GB) DDR2 MEMORY RAM PC2-5300 ECC FBDIMM 240 PIN ", 44.99 ],
[" CORSAIR Vengeance 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 (PC3 15000) Desktop Memory Model CMZ8GX3M2A1866C9 ", 88.99 ],
[" AllComponents 2GB 240-Pin DDR2 SDRAM DDR2 667 (PC2 5300) Desktop Memory Model AC2/667X64/2048 ", 28.99 ],
[" CORSAIR XMS3 4GB 240-Pin DDR3 SDRAM DDR3 1600 Desktop Memory Model CMX4GX3M1A1600C9 ", 43.99 ],
[" G.SKILL Trident X Series 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model F3-2400C9D-8GTXD ", 134.99 ],
[" Mushkin Enhanced Blackline 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model 997092 ", 79.99 ],
[" New 8GB 4x2GB Dell OptiPlex 745 Mini Tower Memory DDR2 ", 124.99 ],
[" G.SKILL Trident X Series 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 2666 (PC3 21300) Desktop Memory Model F3-2666C11D-16GTXD ", 259.99 ],
[" CORSAIR Vengeance 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CML16GX3M2A1600C10R ", 149.99 ],
[" Crucial 4GB Kit 2x 2GB DDR3 1333MHz PC3-10600 Non ECC Desktop Memory RAM 1333 ", 71.04 ],
[" G.SKILL Ripjaws Z Series 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model F3-2133C9Q-16GZH ", 179.99 ],
[" HyperX 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 Desktop Memory Model KHX16LC10K2/16X ", 143.99 ],
[" SUPER TALENT 1GB 240-Pin DDR2 SDRAM DDR2 667 (PC2 5300) Desktop Memory Model T667UA1GV ", 52.52 ],
[" G.SKILL Ripjaws Series 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1066 (PC3 8500) Desktop Memory Model F3-8500CL7D-8GBRL ", 74.99 ],
[" G.SKILL Value Series 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1333 (PC3 10600) Desktop Memory Model F3-10600CL9D-16GBNT ", 124.99 ],
[" ADATA XPG V2 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model AX3U1600W4G9-DMV ", 79.99 ],
[" CORSAIR 8GB 240-Pin DDR3 SDRAM DDR3 1333 Desktop Memory Model CMV8GX3M1A1333C9 ", 73.99 ],
[" PNY 2GB (2 x 1GB) 240-Pin DDR2 SDRAM DDR2 667 (PC2 5300) Dual Channel Kit Desktop Memory Model MD2048KD2-667 ", 45.19 ],
[" CORSAIR Vengeance 64GB (8 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 Desktop Memory Model CMZ64GX3M8A1600C9 ", 624.99 ],
[" Mushkin Enhanced Blackline RADIOACTIVE 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2666 (PC3 21300) Desktop Memory Model 997127Y ", 142.99 ],
[" G.SKILL Ripjaws X Series 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1333 (PC3 10666) Desktop Memory Model F3-10666CL9Q-16GBXL ", 152.99 ],
[" Visiontek 8GB 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Black Label Memory Model 900667 ", 97.99 ],
[" Crucial Ballistix Sport VLP 16GB Kit 2x 8GB DDR3 Memory 1600 MHz 1.35V PC3-12800 ", 202.93 ],
[" CORSAIR Dominator Platinum 32GB (4 x 8GB) 240-Pin DDR3 SDRAM DDR3 2133 Desktop Memory Model CMD32GX3M4A2133C9 ", 439.99 ],
[" Mushkin Enhanced Redline 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model 994084 ", 184.99 ],
[" Ddr3-1333 Sodimm 8Gb/512X8 Cl9 Micron Chip Notebook Memory ", 113.78 ],
[" Mushkin Enhanced Blackline 32GB (4 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model 994110 ", 339.99 ],
[" Crucial Ballistix Tactical 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Low Profile Desktop Memory Model BLT4K4G3D1608ET3LX0 ", 174.99 ],
[" Crucial Ballistix 12GB (3 x 4GB) 240-Pin DDR3 SDRAM DDR3 1333 (PC3 10600) Desktop Memory Model BLT3KIT4G3D1337DT1TX0 ", 129.99 ],
[" Crucial 4GB 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CT51264BA160BJ ", 39.99 ],
[" CORSAIR Vengeance 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CML8GX3M2A1600C9R ", 79.99 ],
[" CORSAIR Vengeance 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CMZ8GX3M2A1600C9B ", 84.99 ],
[" 2GB (2X1GB) MEMORY 128X72 168 PIN PC133 6NS 3.3V ECC REG SDRAM RAM DIMM ", 72.5 ],
[" 8GB (2X4GB) MEMORY 512X72 PC3-10600 1333MHZ 1.5V ECC REG DDR3 240 PIN DIMM 2RX4 ", 72.49 ],
[" 2GB (2X1GB) MEMORY FOR DELL PRECISION 450 450N 650 650N ", 36.25 ],
[" Ddr2-667 1Gb Memory, Oem ", 53.89 ],
[" Ddr3-1600 4Gb Ecc Server Memory (New Item!) ", 242.78 ],
[" HyperX Beast Series 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 Desktop Memory Model KHX18C10T3K4/16 ", 179.99 ],
[" 2GB (2X1GB) DDR Memory ASRock P4I65G ", 32.45 ],
[" Mushkin Enhanced Essentials 4GB 240-Pin DDR3 SDRAM DDR3 1333 (PC3 10666) Desktop Memory Model 991769 ", 40.99 ],
[" Team Vulcan 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model TLYD38G2133HC10QDC01 ", 72.99 ],
[" New 16GB KIT 8X2GB HP Hewlett Packard Compaq PC2-5300 DDR2 ECC FB DIMM RAM MEMORY ", 65.99 ],
[" HyperX Blu 4GB 240-Pin DDR3 SDRAM DDR3 1333 Desktop Memory Model KHX1333C9D3B1/4G ", 49.99 ],
[" Apotop Altair Pro over clock 8GB (2 X 4GB) 240-Pin DDR3 SDRAM DDR3-1600 CL9 Dual Channel Kit Desktop Memory ", 74.99 ],
[" HyperX Beast 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model KHX16C9T3K4/16X ", 188.99 ],
[" SUPER TALENT 2GB 240-Pin DDR2 SDRAM DDR2 800 (PC2 6400) Desktop Memory Model T800UB2GV ", 69.68 ],
[" CORSAIR Vengeance 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1866 Desktop Memory Model CMZ16GX3M2A1866C10 ", 168.99 ],
[" Super Talent Ddr3-1333 2Gb/256Mx8 Ecc/Reg Cl9 Micron Chip Vlp Server Memory ", 60.52 ],
[" 2GB MEMORY 256X64 PC2-6400 800MHZ 1.8V NON ECC DDR2 240 PIN DIMM ", 40.6 ],
[" 256MB (2X128MB) MEMORY 16X64 168 PIN NON PARITY FPM 60NS 5V BUFFERED RAM DIMM ", 28.5 ],
[" Hyperx Khx1600C9D3Lk2/8Gx Ddr3-1600 8Gb(2X4Gb) Cl9 Memory Kit ", 136.85 ],
[" CORSAIR 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1333 Desktop Memory Model CMV8GX3M2A1333C9 ", 71.99 ],
[" G.SKILL Ripjaws X Series 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model F3-2133C9D-16GXH ", 189.99 ],
[" Generic Ddr2-667 512Mb Memory, Oem ", 36.79 ],
[" 8GB (2X4GB) MEMORY 512X64 PC2-6400 800MHZ 1.8V NON ECC DDR2 240 PIN DIMM ", 240.0 ],
[" Mushkin Enhanced Blackline 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 2666 (PC3 21300) Desktop Memory Model 994127R ", 309.99 ],
[" Patriot Viper 3 Low Profile Black 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model PVL316G213C1K ", 179.99 ],
[" G.SKILL 4GB (2 x 2GB) 240-Pin DDR2 SDRAM DDR2 800 (PC2 6400) Dual Channel Kit Desktop Memory Model F2-6400CL4D-4GBPK ", 74.99 ],
[" CORSAIR Vengeance 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CMZ8GX3M2A1600C8R ", 96.99 ],
[" G.SKILL Sniper Gaming Series 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model F3-17000CL9Q-16GBSR ", 169.99 ],
[" 4GB (2X2GB) MEMORY 256X64 PC2-4200 533MHZ 1.8V NON ECC DDR2 240 PIN DIMM ", 63.8 ],
[" New 8GB 4x2GB 667MHz DDR2 ECC Fully Buffered FB-DIMM Memory for MA356LL/A Mac Pro ", 43.99 ],
[" GeIL EVO CORSA Series 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model GOC316GB1600C9DC ", 142.99 ],
[" Ddr3-1600 2Gb/256Mx8 Ecc/Reg Cl11 Samsung Chip Server Memory ", 64.56 ],
[" CORSAIR XMS 64GB (8 x 8GB) 240-Pin DDR3 SDRAM DDR3 1333 Desktop Memory Model CMX64GX3M8A1333C9 ", 574.99 ],
[" Team Vulcan 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model TLYD38G2400HC11CDC01 ", 81.99 ],
[" G.SKILL Ripjaws Z Series 64GB (8 x 8GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model F3-2133C10Q2-64GZM ", 629.99 ],
[" Visiontek Performance 4GB DDR3 SDRAM Memory Module ", 53.99 ],
[" CORSAIR Vengeance Pro 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 Desktop Memory Model CMY8GX3M2A1866C9B (Blue) ", 89.99 ],
[" 8GB 4X2GB KIT DELL FBDIMM PowerEdge 2900 M600 2950 III 2900 R900 T110 RAM MEMORY ", 30.45 ],
[" CORSAIR Vengeance 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CML16GX3M4A1600C9B ", 179.99 ],
[" HyperX 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 Desktop Memory Model KHX18C10K4/16 ", 189.99 ],
[" Ddr3-1333 8Gb/1Gx72 Ecc/Reg Hynix Chip Server Memory ", 136.65 ],
[" AVEXIR Standard Series 16GB SDRAM (2 x 8GB) Dual Channel CL10 240-pin DDR3 1600 (PC3 12800) Desktop Memory Module Model AVD3U16001008G-2SW ", 159.99 ],
[" AllComponents 2GB (2 x 1GB) 240-Pin DDR2 SDRAM DDR2 800 (PC2 6400) Dual Channel kit Desktop Memory Model AC2/800X64/2048-kit ", 26.99 ],
[" Ballistix Sport XT 32GB (4 x 8GB) 240-Pin DDR3 SDRAM DDR3 1866 (PC3 14900) Desktop Memory Model BLS4K8G3D18ADS3 ", 319.99 ],
[" G.SKILL 2GB 240-Pin DDR2 SDRAM DDR2 667 (PC2 5300) Desktop Memory Model F2-5300CL4S-2GBPQ ", 30.99 ],
[" CORSAIR Vengeance Pro 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CMY16GX3M2A1600C9B (Blue) ", 159.99 ],
[" SUPER TALENT 512MB 240-Pin DDR2 SDRAM DDR2 533 (PC2 4300) System Memory Model T533UA512B ", 43.56 ],
[" 8GB DDR3 1600MHz PC3-12800 240 pin DESKTOP Memory RAM Non ECC 1600 Low Density ", 98.59 ],
[" CORSAIR DOMINATOR GT 12GB (3 x 4GB) 240-Pin DDR3 SDRAM DDR3 2000 (PC3 16000) Desktop Memory with Air Fan Model CMT12GX3M3A2000C9 ", 168.99 ],
[" Crucial Ballistix Sport 16GB Kit 8GB x2 DDR3 1333 MHz PC3-10600 CL9 1.5V Memory ", 200.09 ],
[" Crucial 512MB 184-Pin DDR SDRAM DDR 333 (PC 2700) Desktop Memory Model CT6464Z335 - OEM ", 18.99 ],
[" G.SKILL 2GB 240-Pin DDR2 SDRAM DDR2 800 (PC2 6400) Desktop Memory Model F2-6400CL5S-2GBPQ ", 39.99 ],
[" CORSAIR Dominator Platinum 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 2666 Desktop Memory Model CMD16GX3M4A2666C12 ", 304.99 ],
[" G.SKILL Sniper Series 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1866 (PC3 14900) Desktop Memory Model F3-1866C9D-16GSR ", 149.99 ],
[" Ddr3-1600 8Gb 1Gx72 Ecc/Reg Cl11 Server Memory ", 132.14 ],
[" Crucial 2GB (2 x 1GB) 184-Pin DDR SDRAM DDR 400 (PC 3200) Dual Channel Kit Desktop Memory Model CT2KIT12864Z40B - OEM ", 54.99 ],
[" 8GB (2X4GB) FOR ASUS DSBV-D (G1) DSBV-DX/C DSBV-DX/SAS DSEB-D16/SAS DSEB-DG/SAS ", 72.49 ],
[" CORSAIR Vengeance 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 Desktop Memory Model CMZ16GX3M4X1866C9R ", 184.99 ],
[" G.SKILL Trident X Series 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2800 (PC3 22400) Desktop Memory Model F3-2800C11D-8GTXDG ", 329.99 ],
[" Mushkin Enhanced STEALTH 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model 996995S ", 92.99 ],
[" Mushkin Enhanced Blackline 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2400 (PC3 19200) Desktop Memory Model 997093 ", 96.99 ],
[" Super Talent Ddr3-1333 2Gb/256X4 Ecc/Reg Hynix Chip Server Memory ", 57.47 ],
[" CORSAIR Dominator Platinum 32GB (4 x 8GB) 240-Pin DDR3 SDRAM DDR3 2400 Desktop Memory Model CMD32GX3M4A2400C10 ", 589.99 ],
[" Team Vulcan 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory (Yellow Heat Spreader) Model TLYD316G1600HC10ADC01 ", 154.99 ],
[" New 16GB (4X4GB) DDR3 MEMORY RAM PC3-10600 ECC REG DIMM ", 149.99 ],
[" 4GB MEMORY 512X72 PC3-10600 1333MHZ 1.5V ECC REG DDR3 240 PIN DIMM 2RX4 ", 36.24 ],
[" G.SKILL Trident X Series 32GB (4 x 8GB) 240-Pin DDR3 SDRAM DDR3 2666 (PC3 21300) Desktop Memory Model F3-2666C11Q-32GTXD ", 549.99 ],
[" CORSAIR Vengeance 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CMZ16GX3M4X1600C9G ", 169.99 ],
[" Super Talent Ddr3-1066 Sodimm 2Gb/256X8 Notebook Memory ", 56.68 ],
[" Mushkin Enhanced Redline 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 (PC3 14900) Desktop Memory Model 997051 ", 89.99 ],
[" CORSAIR Vengeance LP 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CML16GX3M2A1600C9 ", 159.99 ],
[" 16GB (4X4GB) DDR2 MEMORY RAM PC2-5300 ECC FBDIMM DIMM ", 109.49 ],
[" 16GB (4X4GB) FOR DELL PRECISION 490 690 690 (750W CHASSIS) 690N R5400 T5400 ", 144.99 ],
[" Super Talent Ddr3-1333 1Gb/128X8 Cl9 Value Memory ", 47.63 ],
[" EDGE Tech 2GB DDR2 SDRAM Memory Module ", 34.99 ],
[" Crucial 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model CT2KIT51264BA160BJ ", 84.99 ],
[" 4GB MEMORY 512X64 PC3-6400 800MHZ 1.5V NON ECC DDR3 240 PIN DIMM ", 52.5 ],
[" HyperX Black Series 8GB 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model KHX16C10B1B/8 ", 84.99 ],
[" ADATA XPG V1.0 8GB 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model AX3U1600W8G9-RB ", 72.99 ],
[" G.SKILL AEGIS 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1333 (PC3 10600) Desktop Memory Model F3-1333C9D-8GISL ", 69.99 ],
[" G.SKILL Ares Series 4GB 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model F3-1600C9S-4GAB ", 40.99 ],
[" HyperX 4GB 240-Pin DDR3 SDRAM DDR3 1333 Desktop Memory HyperX Blu Model KHX13C9B1/4R ", 46.99 ],
[" G.SKILL Ripjaws Z Series 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1866 (PC3 14900) Desktop Memory Model F3-14900CL9Q-16GBZL ", 154.99 ],
[" 8GB 2x 4GB DDR3 1333MHz PC3-10600 DESKTOP Memory Non ECC 1333 Low Density RAM 8G ", 97.88 ],
[" G.SKILL Trident X Series 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 2800 (PC3 22400) Desktop Memory Model F3-2800C12D-16GTXDG ", 579.99 ],
[" Mushkin Enhanced Blackline 16GB (2 x 8GB) 240-Pin DDR3 SDRAM DDR3 1600 (PC3 12800) Desktop Memory Model 997050 ", 159.99 ],
[" CORSAIR Dominator Platinum 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 2400 Desktop Memory Model CMD8GX3M2A2400C10 ", 159.99 ],
[" 16GB (4X4GB) MEMORY PC2-5300 667MHZ 1.8V ECC FULLYBUFFERED DDR2 QUAD RANK 240PIN ", 109.49 ],
[" 8GB (2X4GB) DDR2 MEMORY RAM PC2-5300 ECC FBDIMM DIMM ", 72.49 ],
[" Kingston Valueram Kvr16N11K2/16 Ddr3-1600 16Gb(2X 8Gb)/1Gx64 Cl11 Memory Kit ", 208.99 ],
[" G.SKILL Ares Series 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model F3-2133C11Q-16GAO ", 159.99 ],
[" Mushkin Enhanced Essentials 8GB (2 x 4GB) 240-Pin DDR3 SDRAM DDR3 1333 (PC3 10666) Desktop Memory Model 996769 ", 72.99 ],
[" SUPER TALENT 1GB 184-Pin DDR SDRAM DDR 333 (PC 2700) System Memory Model D27PB1GN ", 55.41 ],
[" HyperX Blu Red Series 8GB 240-Pin DDR3 SDRAM DDR3 1600 Desktop Memory Model KHX16C10B1R/8 ", 89.99 ],
[" Patriot Viper 3 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 2133 (PC3 17000) Desktop Memory Model PV316G213C1QKRD ", 199.99 ],
[" G.SKILL Ripjaws Series 16GB (4 x 4GB) 240-Pin DDR3 SDRAM DDR3 1066 (PC3 8500) Desktop Memory Model F3-8500CL7Q-16GBRL ", 159.99 ],
[" 512MB (2X256MB) MEMORY 32X64 168 PIN PC100 8NS 3.3V NON ECC SDRAM RAM DIMM ", 17.0 ]]

gpuList = [[" GIGABYTE GV-N660OC-2GD GeForce GTX 660 2GB 192-bit GDDR5 PCI Express 3.0 x16 HDCP Ready SLI Support Video Card ", 209.99 ],
[" PNY VCGGTX750T2XPB GeForce GTX 750 Ti 2GB 128-Bit GDDR5 PCI Express 3.0 x16 Video Card ", 159.99 ],
[" PowerColor AXR7 250 2GBD5-4DL Radeon R7 250 2GB 128-Bit GDDR5 PCI Express 3.0 CrossFireX Support Low Profile Ready Eyefinity 4 LP Edition Video Card ", 139.99 ],
[" nVIDIA GeForce GT 610 1GB PCI Express PCI-E x16 Single Slot Video Graphics Card ", 85.49 ],
[" Inno3D nVidia GeForce 1GB DDR3 VGA/DVI/HDMI PCI-Express x 16 Video graphics Card ", 55.09 ],
[" XFX Double Dissipation R9-290X-EDFD Radeon R9 290X 4GB 512-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 629.99 ],
[" HIS iCooler Boost H240F2G Radeon R7 240 2GB 128-Bit DDR3 PCI Express 3.0 x16 CrossFireX Support Video Card ", 79.99 ],
[" JATON Video-PX369-QUAD Radeon HD 6570 1GB 128-Bit DDR3 PCI Express x16 Low Profile Ready Video Card ", 184.99 ],
[" MSI GAMING N750Ti TF 2GD5/OC GeForce GTX 750 Ti 2GB 128-Bit GDDR5 HDCP Ready Video Card ", 179.99 ],
[" Low Profile Half Height nVIDIA GeForce 1GB PCI Express x16 Video Graphics Card ", 89.99 ],
[" GIGABYTE GV-N650OC-2GI GeForce GTX 650 2GB 128-bit GDDR5 PCI Express 3.0 x16 HDCP Ready Video Card ", 139.99 ],
[" EVGA 512-P3-1300-LR GeForce 8400 GS 512MB 32-Bit DDR3 PCI Express 2.0 x16 HDCP Ready Low Profile Video Card ", 32.99 ],
[" New GPU 128Bit ATI 2G 2GB Hd6570 DDR3 PCI-E Graphics Card for VGA,DVI,HDMI ", 80.11 ],
[" ASUS GT640-2GD3 GeForce GT 640 2GB 128-bit DDR3 PCI Express 3.0 x16 HDCP Ready Video Card ", 99.99 ],
[" VisionTek 900653 Radeon R9 290 4GB 512-Bit GDDR5 PCI Express 3.0 CrossFireX Support Video Card ", 479.99 ],
[" INNO3D NVIDIA Geforce GT 630 4GB PCI Express x16 Video Graphics Card HMDI ", 125.8 ],
[" JATON VIDEO-348PCI-LP GeForce 6200 512MB 64-bit DDR2 PCI Low Profile Ready Video Card ", 89.99 ],
[" MSI R6450-MD1GD3/LP Radeon HD 6450 1GB 64-Bit DDR3 PCI Express 2.1 x16 HDCP Ready Low Profile Ready Video Card ", 39.99 ],
[" Low Profile Half Height AMD Radeon HD 1024MB 1GB PCI-E x16 Video Graphics Card ", 82.49 ],
[" GIGABYTE GV-R929OC-4GD Radeon R9 290 4GB 512-Bit GDDR5 PCI Express 3.0 HDCP Ready Video Card ", 449.99 ],
[" PNY VCGGTX7501XPB GeForce GTX 750 1GB 128-Bit GDDR5 PCI Express 3.0 x16 Video Card ", 129.99 ],
[" VisionTek 900276 Radeon HD 4650 1GB 128-bit DDR2 PCI Express 2.0 x16 HDCP Ready Low Profile Ready Video Card ", 134.99 ],
[" XFX One ON-XFX1-DLX2 Radeon HD 5450 2GB 64-bit DDR3 PCI-Express Low Profile Ready Video Card ", 44.99 ],
[" PowerColor AXR7 250 1GBD5-HLE Radeon R7 250 1GB 128-Bit GDDR5 PCI Express 3.0 CrossFireX Support Low Profile Ready Video Card ", 119.99 ],
[" PNY Commercial Series VCGGT5201XPB-CG GeForce GT 520 (Fermi) 1GB 64-Bit DDR3 PCI Express 2.0 x16 HDCP Ready Low Profile Video Card ", 59.99 ],
[" Asus GT640-DCSL-2GD3 GeForce GT 640 Graphic Card - 1 GPUs - 901 MHz Core - 2 GB GDDR3 SDRAM - PCI-Express 3.0 x16 ", 113.99 ],
[" EVGA 02G-P4-2770-KR GeForce GTX 770 2GB 256-Bit GDDR5 PCI Express 3.0 SLI Support Video Card ", 349.99 ],
[" ASUS GTX760-DC2OC-2GD5 GeForce GTX 760 2GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready SLI Support Video Card ", 269.99 ],
[" GIGABYTE GV-R645-1GI REV2.0 Radeon HD 6450 1GB 64-bit DDR3 PCI Express 2.1 HDCP Ready Low Profile Ready Video Card ", 39.99 ],
[" HIS iCooler Turbo H260XFT1GD Radeon R7 260X 1GB 128-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 129.99 ],
[" nVIDIA GeForce 2GB PCI-E x16 Single Slot HDMI+DVI Gaming HD Video Graphics Card ", 104.99 ],
[" PNY VCGGTX7602XPB GeForce GTX 760 2GB 256-bit GDDR5 PCI Express 3.0 SLI Support Video Card ", 259.99 ],
[" NVIDIA Geforce GT 630 2GB 128 bit DDR3 PCI Express Video Graphics Card HMDI DVI ", 118.49 ],
[" NVIDIA GeForce GF FX 5500 FX5500 256 MB PCI Desktop Video Graphics Card Vga +TvO ", 40.17 ],
[" AMD ATI Radeon 2GB DDR3 PCI Express Video Graphics Card HMDI windows 7/vista/xp ", 101.43 ],
[" MSI N640GT-MD2GD3 GeForce GT 640 2GB 128-Bit DDR3 PCI Express 3.0 x16 HDCP Ready Video Card ", 99.99 ],
[" 1GB 1024MB nVIDIA GeForce Single Slot PCI Express PCI-E x16 Video Graphics Card ", 74.99 ],
[" ASUS EAH5450 SILENT/DI/1GD3(LP) Radeon HD 5450 1GB DDR3 PCI Express 2.1 x16 HDCP Ready Low Profile Ready Video Card ", 35.99 ],
[" EVGA 01G-P3-1302-LR GeForce 8400 GS 1GB 64-Bit DDR3 PCI Express 2.0 x16 HDCP Ready Low Profile Ready Video Card ", 29.99 ],
[" JATON 3DForce6200Twin GeForce 6200 256MB 64-bit DDR AGP 4X/8X Video Card ", 59.99 ],
[" NVIDIA GeForce 2GB Low Profile Half Height PCI Express x16 Video Graphics Card ", 121.73 ],
[" PowerColor TurboDuo AXR9 280X 3GBD5-T2DHE/OC Radeon R9 280X 3GB 384-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card ", 329.99 ],
[" XFX Double Dissipation R9-290A-EDFD Radeon R9 290 4GB 512-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 499.99 ],
[" VisionTek 900270 Radeon HD 4350 512MB 64-Bit DDR2 PCI Express 2.0 x16 Low Profile Ready Video Card ", 44.99 ],
[" ASUS R9290X-DC2OC-4GD5 Radeon R9 290X 4GB 512-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card ", 629.99 ],
[" MSI N650-2GD5/OC GeForce GTX 650 2GB 128-Bit GDDR5 PCI Express 3.0 HDCP Ready Video Card ", 119.99 ],
[" Zotac ZT-60607-10L GeForce GT 610 Graphic Card - 810 MHz Core - 1 GB DDR3 SDRAM - PCI Express 3.0 ", 49.99 ],
[" XFX Core Edition R7-250A-ELF4 Radeon R7 250 4GB 128-Bit DDR3 PCI Express 3.0 HDCP Ready CrossFireX Support Low Profile Ready Video Card ", 109.99 ],
[" SAPPHIRE Ultimate 100368USR Radeon R7 250 1GB 128-Bit GDDR5 PCI Express 3.0 Video Card ", 99.99 ],
[" ASUS GTX650-E-2GD5 GeForce GTX 650 2GB 128-bit GDDR5 PCI Express 3.0 HDCP Ready Video Card ", 139.99 ],
[" ZOTAC ZONE Edition ZT-60603-20L GeForce GT 610 1GB 64-bit DDR3 PCI Express 2.0 x16 HDCP Ready Video Card ", 48.99 ],
[" EVGA 01G-P3-2632-KR GeForce GT 630 1GB 128-Bit GDDR5 PCI Express 2.0 x16 HDCP Ready Video Card ", 64.99 ],
[" XFX FX775AZNJ4 Radeon HD 7750 1GB DDR5 CI-Express 3.0 x16 Video Card ", 109.99 ],
[" HIS iCooler Boost Clock H250F1G Radeon R7 250 1GB 128-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 89.99 ],
[" EVGA 04G-P4-3776-KR GeForce GTX 770 4GB 256-Bit GDDR5 PCI Express 3.0 SLI Support FTW 4GB Dual w/ EVGA ACX Cooler Video Card ", 429.99 ],
[" VisionTek 900506 Radeon HD 7870 GHz Edition 2GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 229.99 ],
[" 2GB Half Height Small Form Factor PC Single Slot PCI-E x16 Video Graphics Card ", 97.49 ],
[" MSI NVIDIA GeForce 210 1GB GDDR3 HDMI Low Profile PCI-E Video Card ", 60.87 ],
[" NVIDIA Geforce 9 PCI Express Video Graphics Card HDMI ", 139.13 ],
[" JATON Video-228PCI-Twin GeForce FX 5200 128MB 64-bit DDR PCI Video Card ", 74.99 ],
[" MSI N750TI-2GD5/OC GeForce GTX 750 Ti 2GB 128-Bit GDDR5 PCI Express 3.0 Video Card ", 159.99 ],
[" 512MB nVIDIA GeForce AGP 4X 8X Dual Monitor Display View Video Graphics VGA Card ", 97.49 ],
[" GIGABYTE GV-N650OC-1GI GeForce GTX 650 1GB 128-bit GDDR5 PCI Express 3.0 x16 HDCP Ready Video Card ", 108.99 ],
[" PNY VCGGT6302XPB GeForce GT 630 2GB 128-Bit DDR3 PCI Express 2.0 x16 HDCP Ready Video Card ", 58.99 ],
[" JATON VIDEO-228PCI-DVI GeForce FX 5200 128MB 64-bit DDR PCI Low Profile Ready Video Card ", 79.99 ],
[" EVGA 512-P3-1310-LR GeForce 210 512MB 32-Bit DDR3 PCI Express 2.0 x16 HDCP Ready Low Profile Video Card ", 32.99 ],
[" EVGA SuperClocked 02G-P4-2762-KR GeForce GTX 760 2GB 256-bit GDDR5 PCI Express 3.0 SLI Support Video Card ", 259.99 ],
[" ASUS HD6670-2GD3 Radeon HD 6670 2GB 128-Bit DDR3 PCI Express 2.1 x16 HDCP Ready Video Card ", 79.99 ],
[" GIGABYTE GV-N770OC-4GD GeForce GTX 770 4GB 256-bit GDDR5 PCI Express 3.0 HDCP Ready WindForce 3X 450W Video Card ", 399.99 ],
[" VisionTek 900652 Radeon R9 280X 3GB 384-Bit GDDR5 PCI Express 3.0 CrossFireX Support Video Card ", 329.99 ],
[" AMD ATI Radeon 2GB PCI Express x 16 Video Graphics Card HMDI windows 7/vista/xp ", 101.93 ],
[" ZOTAC Synergy Edition ZT-60413-10L GeForce GT 630 4GB 128-bit DDR3 PCI Express 2.0 x16 HDCP Ready Video Card ", 79.99 ],
[" NVIDIA GeForce GF FX 5500 FX5500 256 MB PCI 3D Video Graphics Card Vga +Tv Out ", 40.17 ],
[" AMD ATI PCI-Express x16 1GB 64 bit DDR3 HDMi DVI VGA Video Graphics Card  ", 57.64 ],
[" JATON 3DFORCE6200Twin-LP GeForce 6200 256MB 64-Bit DDR2 AGP 4X/8X Low Profile Ready Video Card ", 49.99 ],
[" VisionTek 900366 Radeon HD 5570 1GB DDR3 PCI Express 2.0 x16 Low Profile Ready Video Card ", 184.99 ],
[" 2GB Half Height Low Profile SFF Dual Monitor Display View HD Video Graphics Card ", 104.99 ],
[" Sapphire AMD Radeon HD5450 1GB GDDR3 VGA/DVI/HDMI 64bit PCI-E Graphic Video Card ", 56.52 ],
[" AMD ATI Radeon 2GB PCI Express x 16 Video Graphics Card HMDI windows 7/vista/xp ", 98.53 ],
[" SAPPHIRE 100364-4GL Radeon R9 270X 4GB GDDR5 Video Card ", 229.99 ],
[" AMD ATI PCI-Express x16 1GB 64 bit DDR3 HDMi DVI VGA Video Graphics Card  ", 59.63 ],
[" EVGA SuperClocked 02G-P4-2765-KR GeForce GTX 760 2GB 256-bit GDDR5 PCI Express 3.0 SLI Support w/ EVGA ACX Cooler Video Card ", 259.99 ],
[" VisionTek 900370 Radeon HD 6570 1GB DDR3 PCI Express 2.1 x16 HDCP Ready Video Card ", 79.99 ],
[" GIGABYTE GV-R725O5-2GI Radeon R7 250 2GB 128-Bit GDDR5 PCI Express 3.0 HDCP Ready Video Card ", 99.99 ],
[" Sapphire Radeon R9 290 4GB GDDR5 DUAL DVI-D/HDMI/DP TRI-X OC Version PCI-Express Graphics Card ", 895.69 ],
[" NVIDIA Geforce GT 2GB DDR3 PCI Express Video Graphics Card HMDI DVI VGA 2 gb ", 101.14 ],
[" GIGABYTE AMD Radeon HD 5450 1GB DDR3 VGA/DVI/HDMI Low Profile V-R545-1GI REV2.0 ", 47.84 ],
[" XFX R7-240A-CLH4 Radeon R7 240 2GB 128-Bit DDR3 PCI Express 3.0 CrossFireX Support Low Profile Video Card ", 69.99 ],
[" nVIDIA GeForce 512MB AGP 4X 8X Single Slot Video Graphics VGA Card VGA+DVI+HDTV ", 97.49 ],
[" HIS H290F4GD Radeon R9 290 4GB 512-Bit GDDR5 PCI Express 3.0 x16 Video Card ", 799.69 ],
[" PNY GeForce GT 640 Graphic Card - 900 MHz Core - 2 GB DDR3 SDRAM - PCI Express 3.0 x16 - Low-profile ", 90.99 ],
[" NVIDIA Geforce GT 2GB 64 bit PCI Express Video Graphics Card HMDI DVI VGA 2 gb ", 116.63 ],
[" HIS H435F512HA Radeon HD 4350 512MB 64-Bit DDR3 AGP 4X/8X HDCP Ready Low Profile Ready Video Card ", 59.99 ],
[" EVGA 02G-P4-3751-KR GeForce GTX 750 Ti 2GB 128-Bit GDDR5 PCI Express 3.0 Video Card ", 149.99 ],
[" 512MB nVIDIA GeForce Single Slot PCI Express PCI-E x16 Video Graphics VGA Card ", 68.14 ],
[" MSI N640-4GD3 GeForce GT 640 4GB 128-Bit GDDR3 PCI Express 3.0 x16 HDCP Ready Video Card ", 104.99 ],
[" ASUS DirectCU II R9270X-DC2T-4GD5 Radeon R9 270X 4GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card ", 299.99 ],
[" EVGA 02G-P3-2629-KR GeForce GT 620 2GB 64-Bit DDR3 PCI Express 2.0 x16 HDCP Ready Video Card ", 59.99 ],
[" ATI Radeon 2GB DDR3 PCI-Express Video Graphics Card HMDI Windows 7/Vista/XP NEW ", 74.99 ],
[" JATON Video-339PCI-HLX Radeon HD 5450 512MB 64-Bit DDR3 PCI HDCP Ready Low Profile Ready Video Card ", 84.99 ],
[" EVGA nVidia GeForce 8400GS 1GB DDR3 VGA/DVI/HDMI PCI-E Video Card ", 60.45 ],
[" GIGABYTE GV-N750OC-1GI GeForce GTX 750 1GB 128-Bit GDDR5 PCI Express 3.0 Video Card ", 129.99 ],
[" PowerColor DEVIL AXR9 270X 2GBD5-A2DHE Radeon R9 270X 2GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card ", 239.99 ],
[" MSI Radeon R9 290X GAMING 4GB 512-bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 649.99 ],
[" PNY VCGG2101D3XPB GeForce 210 1GB 64-Bit DDR3 PCI Express 2.0 x16 HDCP Ready Low Profile Ready Video Card ", 39.99 ],
[" SAPPHIRE 100367L Radeon R7 250X 1GB 128-Bit GDDR5 PCI Express 3.0 CrossFireX Support Video Card ", 99.99 ],
[" VisionTek 900292 Radeon HD 3450 512MB 64-Bit DDR2 PCI Low Profile Ready Video Card ", 124.99 ],
[" XFX Double D R9-270A-CDFC Radeon R9 270 2GB GDDR5 PCI Express 3.0 CrossFireX Support Video Card ", 199.99 ],
[" HP GeForce GT 630 Graphic Card - 2 GB DDR3 SDRAM - PCI Express x16 ", 151.99 ],
[" Sapphire DUAL-X AMD Radeon R9 270X OC 2GB GDDR5 2DVI/HDMI/DisplayPort PCI-Express Video Card w/ Boost ", 399.95 ],
[" 1GB nVIDIA GeForce PCI-E x16 Dual Monitor Display View Video Graphics VGA Card ", 82.64 ],
[" MSI R7 260 1GD5 OC 1GB 128-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 129.99 ],
[" PowerColor AXR7 240 2GBK3-HV2E/OC Radeon R7 240 2GB 128-Bit DDR3 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card ", 69.99 ],
[" ASUS DirectCU II OC R9290-DC2OC-4GD5 Radeon R9 290 4GB 512-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card ", 499.99 ],
[" HIS H295LF8G4M Radeon R9 295x2 8GB 1024 (512 x 2)-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 1499.99 ],
[" ASUS R9270X-DC2T-2GD5 Radeon R9 270X 2GB 256-bit GDDR5 PCI Express 3.0 CrossFireX Support Video Card ", 259.99 ],
[" nVIDIA 2GB Windows 8 7 Vista XP Linux PCI-E x16 VGA+HDMI+DVI Video Graphics Card ", 104.99 ],
[" EVGA nVidia GeForce 8400GS 1GB DDR3 VGA/DVI/HDMI PCI-Express Video Card ", 60.89 ],
[" EVGA 512-A8-N403-LR GeForce 6200 512MB 64-Bit GDDR2 AGP 8X Video Card ", 42.99 ],
[" MSI N660 TF 2GD5/OC GeForce GTX 660 2GB 192-bit GDDR5 PCI Express 3.0 x16 HDCP Ready SLI Support Video Card ", 209.99 ],
[" INNO3D NVIDIA Geforce 4GB PCI Express x16 Video Graphics Card HMDI Low profile ", 135.95 ],
[" SAPPHIRE 100363L Radeon R9 280X 3GB 384-bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 359.99 ],
[" EVGA SuperClocked w/ ACX Cooling 02G-P4-2774-KR GeForce GTX 770 2GB 256-bit GDDR5 PCI Express 3.0 SLI Support Video Card ", 369.99 ],
[" SAPPHIRE VAPOR-X 100363VX-2SR Radeon R9 280X PCI Express 3.0 TRI-X OC w/ Boost Video Card (UEFI) ", 389.99 ],
[" HIS iCooler H250XF1G Radeon R7 250X 1GB 128-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card ", 109.99 ],
[" VisionTek 900669 Radeon HD 7750 1GB 128-Bit DDR3 PCI Express 3.0 Video Card ", 189.99 ],
[" EVGA 03G-P4-2884-KR GeForce GTX 780 Ti Superclocked 3GB 384-Bit GDDR5 PCI Express 3.0 SLI Support w/EVGA ACX Cooler Video Card ", 729.99 ],
[" SAPPHIRE Radeon HD 6450 1GB 64-bit DDR3 PCI Express 2.1 x16 HDCP Ready  Video Card    ( 100322L) ", 39.99 ],
[" GeForce HD 512MB PCI-E x16 Windows 8 7 Vista XP Linux Video Graphics VGA Card ", 68.14 ],
[" XFX One ON-XFX1-PLS2 Radeon HD 5450 1GB 64-Bit DDR3 PCI Express 2.1 x16 HDCP Ready Low Profile Ready Video Card ", 34.99 ],
[" NVIDIA Geforce GT 2GB DDR3 PCI Express Video Graphics Card HMDI DVI VGA 2 gb ", 104.63 ],
[" ASUS R7240-2GD3-L Radeon R7 240 2GB 128-Bit DDR3 PCI Express 3.0 HDCP Ready Low Profile Video Card ", 69.99 ],
[" VisionTek 900231 Radeon HD 3450 512MB 64-bit GDDR2 PCI Express 2.0 x16 HDCP Ready CrossFireX Support Video Card ", 59.99 ],
[" ASUS GTX660-DC2O-2GD5 GeForce GTX 660 2GB 192-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready SLI Support Video Card ", 219.99 ],
[" Low Profile Half Height 1GB HD PCI Express PCI-E x1 Video Graphics Card DVI+HDMI ", 144.99 ],
[" EVGA 03G-P4-2667-KR GeForce GTX 660 FTW Signature 2 3GB 192-bit GDDR5 PCI Express 3.0 x16 HDCP Ready SLI Support Video Card ", 249.99 ],
[" PNY VCGGT630SLXPB GeForce GT 630 1GB 64-bit DDR3 PCI Express 2.0 x16 Low Profile Ready Video Card ", 69.99 ]]

hdList = [[" Mushkin Enhanced Chronos MKNSSDCR480GB-7 2.5\" 480GB SATA III 7mm Internal Solid State Drive (SSD) ", 359.99 ],
[" SAMSUNG 840 EVO MZ-7TE250LW 2.5\" TLC Internal Solid State Drive (SSD) With Notebook Bundle Kit ", 274.99 ],
[" Intel DC S3500  Series SSDSC2BB240G401 2.5\" 240GB SATA III MLC Internal Solid State Drive (SSD) - OEM ", 299.99 ],
[" Mushkin Enhanced Atlas Series MKNSSDAT30GB-DX 30GB Mini-SATA (mSATA) Synchronous MLC Internal Solid State Drive (SSD) ", 64.99 ],
[" Kingston SS200S3/30G 2.5\" 30GB SATA III Internal Solid State Drive (SSD) ", 79.0 ],
[" Kingston HyperX 3K SH103S3/240G 2.5\" 240GB SATA III MLC Internal Solid State Drive (SSD) (Stand-Alone Drive) ", 209.99 ],
[" Corsair Force LS Series CSSD-F60GBLS 2.5\" 60GB SATA III MLC Internal Solid State Drive (SSD) ", 79.99 ],
[" Intel 330 Series Maple Crest SSDSC2CT120A3K5 2.5\" 120GB SATA III MLC Internal Solid State Drive (SSD) ", 259.99 ],
[" Corsair Force Series GS CSSD-F128GBGS-BK 2.5\" 128GB SATA III Internal Solid State Drive (SSD) ", 139.99 ],
[" SAMSUNG 830 Series MZ-7PC256B/WW 2.5\" 256GB SATA III MLC Internal Solid State Drive (SSD) ", 493.0 ],
[" SAMSUNG 830 Series MZ-7PC128B/WW 2.5\" 128GB SATA III MLC Internal Solid State Drive (SSD) ", 192.29 ],
[" PNY Prevail SSD9SC240GCDA-PB 2.5\" 240GB SATA III Internal Solid State Drive (SSD) ", 429.99 ],
[" SAMSUNG 840 EVO MZ-7TE500LW 2.5\" TLC Internal Solid State Drive (SSD) With Notebook Bundle Kit ", 349.99 ],
[" Corsair Force LS Series CSSD-F240GBLS 2.5\" 240GB SATA III MLC Internal Solid State Drive (SSD) ", 229.99 ],
[" Intel SSD DC S3500 Series SSDSC2BB600G401 2.5\" 600GB SATA III MLC Internal Solid State Drive (SSD) - OEM ", 699.99 ],
[" OCZ Vertex 3.20 VTX3-25SAT3-120G.20 2.5\" 120GB SATA III MLC Internal Solid State Drive (SSD) ", 184.95 ],
[" Intel 530 Series SSDSCKGW180A401 M.2 180GB SATA 6Gb/s MLC Internal Solid State Drive (SSD) - OEM ", 199.99 ],
[" OCZ Vector Series VTR1-25SAT3-128G 2.5\" 128GB SATA III MLC ", 151.59 ],
[" Mushkin Enhanced Chronos MKNSSDCR60GB-7 2.5\" 60GB SATA III 7mm Internal Solid State Drive (SSD) ", 143.0 ],
[" Kingston SSDNow V300 Series SV300S37A/480G 2.5\" 480GB SATA III Internal Solid State Drive (SSD) w/Adapter  ", 399.99 ],
[" Corsair Force Series GS CSSD-F480GBGS-BK 2.5\" 480GB SATA III Internal Solid State Drive (SSD) ", 449.99 ],
[" ADATA XPG SX900 ASX900S3-64GM-C 2.5\" 64GB SATA III MLC Internal Solid State Drive (SSD) ", 169.95 ],
[" SanDisk Ultra Plus SDSSDHP-064G-G26 2.5\" 64GB SATA III MLC Internal Solid State Drive (SSD) for Desktop ", 79.99 ],
[" Mushkin Enhanced Chronos MKNSSDCR240GB-7 2.5\" 7mm Internal Solid State Drive (SSD) ", 123.95 ],
[" Kingston SSDNow V300 Series SV300S37A/60G 2.5\" 60GB SATA III Internal Solid State Drive (SSD) ", 69.99 ],
[" Transcend SSD 720 2.5\" 512GB SATA III Internal Solid State Drive (SSD) with Desktop Upgrade Kit ", 506.13 ]]


caseList = [[" Cooler Master HAF X Blue Edition - High Air Flow Full Tower Computer Case with Windowed Side Panel and USB 3.0 ", 219.99 ],
[" ZALMAN ZM-T2 Black Steel / Plastic MicroATX Mini Tower Computer Case ", 39.99 ],
[" CM Storm Enforcer - Gaming Mid Tower Computer Case with USB 3.0 and Water Cooling Support ", 89.99 ],
[" Antec P100 Black Computer Case ", 99.99 ],
[" Details about  AeroCool Strike X GT Black ATX Tower Case - NEW ", 159.36 ],
[" XION Gaming Series XON-980-BK Black with RED LED Light Steel / Plastic ATX Mid Tower Computer Case ", 89.99 ],
[" Brand NEW APEX MI-008 250W Mini-ITX Case ", 80.75 ],
[" Cooler Master Elite 350 - Mid Tower Computer Case with 500W Power Supply and Blue LED Light Strip ", 59.99 ],
[" NZXT Phantom 820 Series CA-PH820-W1 White Steel / Plastic ATX Full Tower Computer Case ", 249.99 ],
[" ZALMAN Z3 Plus ATX Mid-Tower PC Case, Optimum Multi-Fan system cooling, Wide band front mesh ventilation, Acrylic side panel, multiple dust filters, VF multi-guide for VGA support, USB 3.0  ", 64.99 ],
[" APEVIA X-CRUISER3 X-CRUISER3-GN Black Steel ATX Mid Tower Computer Case w/ Side Window-Green ", 89.99 ],
[" NZXT Guardian 921 RB 921RB-001-RD Black SECC steel chassis Computer Case ", 69.99 ],
[" Rosewill BLACKHAWK Gaming ATX Mid Tower Computer Case, come with Five Fans, window side panel, top HDD dock  ", 99.99 ],
[" Cooler Master Elite 311 - Mid Tower Computer Case with Windowed Side Panel and Blue Trim ", 49.99 ],
[" Ark Technology PN03 mATX Mini-Tower PC Case with 500W PSU 2x 5.25in Bays (Black) ", 66.61 ],
[" Corsair Carbide Series 500R Black Steel structure with molded ABS plastic accent pieces ATX Mid Tower Computer Case ", 149.99 ],
[" Thermaltake V3 Black AMD Edition VL800P1W2N Black / Red SECC / Plastic ATX Mid Tower Computer Case ", 59.99 ],
[" BitFenix Phenom BFC-PHE-300-WWXKK-RP No Power Supply Mini-ITX Tower Case (White) ", 125.99 ],
[" Antec Twelve Hundred V3 Black Steel ATX Full Tower Unbeatable Gaming Case ", 179.99 ],
[" Thermaltake Commander MS-I Epic Edition Black / Red SECC ATX Mid Tower Computer Case ", 69.99 ],
[" RAIDMAX Agusta ATX-605BT Black/Titanium Steel / Plastic ATX Full Tower Computer Case ", 109.99 ],
[" IN WIN H-Frame Mini Green Aluminum Mini-ITX Computer Case 180W Power Supply ", 194.99 ],
[" Corsair Graphite Series 230T CC-9011038-WW Orange on Black with ORANGE LED fans ATX Mid Tower Computer Case ", 79.99 ],
[" Cooler Master Force 500 - Mid Tower Computer Case with USB 3.0 and Included 500W Power Supply ", 79.99 ],
[" ZALMAN Z3 Plus White ATX Mid-Tower PC Case, Optimum Multi-Fan system cooling, Wide band front mesh ventilation, Acrylic side panel, multiple dust filters, VF multi-guide for VGA support, USB 3.0 - Ret ", 69.99 ],
[" Antec NSK 4482B Black 0.8mm cold rolled steel ATX Mid Tower Computer Case 380W Power Supply ", 99.99 ],
[" Details about  HEC Blitz PC Computer Case Black/Steel ATX mATX Mid Tower - NEW ", 115.91 ],
[" SilverStone DS380B Black Aluminum front door, SECC body NAS chassis Premium 8-bay Small Form Factor NAS Chassis SFX PSU (sold separately) Power Supply ", 159.99 ],
[" Rosewill QN100 Dual Fans ATX Mid Tower Computer Case, come with 1x Front 120mm Fan, 1x Rear 120mm Fan  ", 39.99 ],
[" EVGA Hadron Hydro Mini-ITX Chassis Black with 500W 80Plus Gold Power Supply (110-MW-1002-K1) ", 189.99 ],
[" New Black ATX Mid Tower Front LED Fan Gaming PC Screwless Hot-Swap Computer Case ", 112.47 ],
[" RAIDMAX Cobra Z ATX-502WBU Black/Blue Steel / Plastic MicroATX Mid Tower Computer Case ", 69.99 ],
[" Rosewill R103A Black Steel ATX Mid Tower Computer Case with 350W 20+4 pin connector Power Supply ", 49.99 ],
[" LIAN LI PC-A75WX Black ATX Full Tower Computer Case ", 229.99 ],
[" 350W MicroATX Tower Case (Black/Silver) ", 82.2 ],
[" USB 3.0 2.5\" HDD Hard Disk Drive External Enclosure Case Box Laptop Blue ", 10.16 ],
[" Fractal Design Define R4 with Window Titanium Grey Silent ATX Mid Tower Case ", 119.99 ],
[" RAIDMAX Altas ATX-295WU Blue / Black Steel / Plastic ATX Mid Tower Computer Case ", 49.99 ],
[" Corsair Graphite Series 600T CC600TM Graphite Grey Mid-Tower Gaming Case ", 169.99 ],
[" NEW Mid Tower Case w/ Docking Station Black ", 104.39 ],
[" ENERMAX OSTROG ECA3253-BW Black / White SGCC / SECC ATX Mid Tower Computer Case ", 49.99 ],
[" iMicro CA-IM1205B 400W 20+4pin Mini ATX Mini Tower Case (Black) ", 52.04 ],
[" APEVIA X-Hermes X-HERMES-BL Black/Blue Steel ATX Mid Tower Computer Case w/ Side Window-Blue ", 79.99 ],
[" BitFenix Comrade BFC-COM-100-KKXS1-RP Black ATX Computer Case ", 49.0 ],
[" Corsair Graphite Series 760T Black Steel / Plastic ATX Full Tower Windowed Gaming Case with two 140mm red LED fans ", 179.99 ],
[" LIAN LI PC-V700B Black Aluminum ATX Mid Tower Computer Case ", 219.99 ],
[" Raidmax Vortex ATX-402WB No Power Supply ATX Mid Tower Gaming Case (Black) ", 75.24 ],
[" NZXT Crafted Series Tempest 410 Black Steel / Plastic ATX Mid Tower Computer Case ", 69.99 ],
[" APEVIA X-CRUISER3 X-CRUISER3-BL Black Steel ATX Mid Tower Computer Case w/ Side Window-Blue ", 89.99 ],
[" NZXT Guardian 921 RB 921RB-001-BL Black SECC Steel, ABS Plastic ATX Mid Tower Computer Case ", 69.99 ],
[" Rosewill RANGER-M Dual Fans MicroATX Mini Tower Computer Case ", 49.99 ],
[" LOGISYS Computer CS206BK Black Steel ATX Mid Tower Computer SOHO Case 480W Power Supply ", 44.99 ],
[" LIAN LI PC-A75 Black Aluminum ATX Full Tower Computer Case ", 189.99 ],
[" Antec Gaming Series One Black Steel ATX Mid Tower Computer Case ", 59.99 ],
[" Cooler Master Cosmos II - Ultra Tower Computer Case with Metal Body and Hinged Side Panels ", 349.99 ],
[" Sentey Slim 2422 Slim Flex Case w/Power Supply	LCD DISPLAY SECC 0.7mm 2x USB/1x Fan/Micro ATX-ITX ", 59.99 ],
[" NZXT Phantom 630 Windowed Edition Gunmetal Steel / Plastic ATX Full Tower Computer Case ", 179.99 ]]


if __name__ == "__main__":
    # Change this to your own directory if this file doesnt work
    #PWD = os.path.dirname(os.path.dirname(__file__ ))
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    #sys.path.append(PWD)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "computerbuilder.settings")

    from parts.models import MoboListing, CpuListing, GpuListing, CaseListing, MemListing, HdListing

    mobo = MoboListing.objects.all()
    print mobo


def populate_mobo():
    """
    This function starts by taking the global list of mobo parts and then inserts them into the database
    """
    global MoboListing
    
    for item in moboList:
        mobo = "%s" % item[0]
        price = "%s" % item[1]
         
        try:
           MoboListing.objects.get(moboList = mobo, moboPrice = price)
        
        except MoboListing.DoesNotExist:
           print mobo
           mydb = MoboListing.objects.create(moboList = mobo, moboPrice = price)
           print mydb
           mydb.save()

def populate_cpu():
    """
    This function starts by taking the global list of cpu parts and then inserts them into the database
    """
    global CpuListing
    for item in cpuList:
        cpu = "%s" % item[0]
        price = "%s" %item[1]
        
        try:
           CpuListing.objects.get(cpuList = cpu, cpuPrice = price)
        
        except CpuListing.DoesNotExist:
           print cpu
           mydb = CpuListing.objects.create(cpuList = cpu, cpuPrice = price)
           mydb.save()

def populate_gpu():
    """
    This function starts by taking the global list of gpu parts and then inserts them into the database
    """
    global GpuListing
    for item in gpuList:
        gpu = "%s" % item[0]
        price = "%s" % item[1]
        
        try:
           GpuListing.objects.get(gpuList = gpu, gpuPrice = price)
        
        except GpuListing.DoesNotExist:
           print gpu
           mydb = GpuListing.objects.create(gpuList = gpu, gpuPrice = price)
           mydb.save()
           print mydb
        

def populate_cases():
    """
    This function starts by taking the global list of case parts and then inserts them into the database
    """
    global CaseListing
    for item in caseList:
        case  = "%s" % item[0]
        price = "%s" % item[1]
        
        try:
           CaseListing.objects.get(caseList = case, casePrice = price)
        
        except CaseListing.DoesNotExist:
           print case
           mydb = CaseListing.objects.create(caseList = case, casePrice = price)
           print mydb
           mydb.save()

def populate_mem():
    """
    This function starts by taking the global list of ram parts and then inserts them into the database
    """
    global MemListing
    for item in memList:
        mem = "%s" % item[0]
        price = "%s" % item[1]
     
        try:
           MemListing.objects.get(memList = mem, memPrice = price)
        
        except MemListing.DoesNotExist:
           print mem
           mydb = MemListing.objects.create(memList = mem, memPrice = price)
           print mydb
           mydb.save()

def populate_hd():
    """
    This function starts by taking the global list of hdd parts and then inserts them into the database
    """
    global HdListing
    for item in hdList:
        hd = "%s" % item[0]
        price = "%s" % item[1]
        
        try:
           HdListing.objects.get(hdList = hd, hdPrice = price)
        
        except HdListing.DoesNotExist:
           print hd
           mydb = HdListing.objects.create(hdList = hd, hdPrice = price)
           print mydb
           mydb.save()
      

"""
We Now call all of our fill Db function to fill the database with the parts listed above.
"""
populate_mobo()
populate_cpu()
populate_gpu()
populate_cases()
populate_mem()
populate_hd()
