import sys
import os


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
[" MSI 760GM-P34 (FX) AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 52.99 ],
[" Open Box: ASUS SABERTOOTH 990FX R2.0 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 179.49 ],
[" Open Box: ASUS A55BM-A/USB3 FM2+ / FM2 AMD A55 (Hudson D2) USB 3.0 HDMI Micro ATX AMD Motherboard ", 59.49 ],
[" Open Box: ASUS A88X-PRO FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI AMD Motherboard ", 109.64 ],
[" Open Box: ASRock FM2A85X Extreme4 FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 76.49 ],
[" Open Box: GIGABYTE GA-A75-UD4H FM1 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 129.99 ],
[" Open Box: GIGABYTE GA-F2A85XM-D3H FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 73.94 ],
[" Open Box: ASUS M5A99FX PRO R2.0 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 159.99 ],
[" Open Box: GIGABYTE GA-F2A55M-DS2 FM2 AMD A55 (Hudson D2) Micro ATX AMD Motherboard with UEFI BIOS ", 55.24 ],
[" Open Box: ASRock 960GC-GS FX AM3+/AM3/AM2+ AMD 760G Micro ATX AMD Motherboard ", 46.49 ],
[" Open Box: ASUS A88XM-PLUS/CSM FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 78.45 ],
[" Open Box: ASUS M5A99X EVO R2.0 AM3+ AMD 990X + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 139.99 ],
[" Open Box: GIGABYTE GA-78LMT-S2 AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ", 54.99 ],
[" Open Box: ASRock 990FX Extreme3 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 139.99 ],
[" Open Box: ASRock 990FX Extreme9 AM3+ AMD 990FX + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 161.49 ],
[" Open Box: ASRock 980DE3/U3S3 AM3+ AMD RX881/760G SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 59.49 ],
[" Open Box: ASUS M5A97 LE R2.0 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 89.99 ],
[" Open Box: ASUS A88XM-A FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard with UEFI BIOS ", 72.24 ],
[" Open Box: ASRock 970 EXTREME4 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 114.99 ],
[" Open Box: ASUS A88X-PLUS FM2+ / FM2 AMD A88X (Bolton D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 92.39 ],
[" Open Box: ASUS M5A97 R2.0 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard with UEFI BIOS ", 99.99 ],
[" MSI FM2-A75MA-E35 FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 59.79 ],
[" ASUS F2A55-M/CSM FM2 AMD A55 (Hudson D2) USB 3.0 HDMI Micro ATX AMD Motherboard with UEFI BIOS ", 69.99 ],
[" ASRock FM2A78M-HD+ FM2+ / FM2 AMD A78 (Bolton D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 59.99 ],
[" ECS A75F2-A2(1.0) FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 69.99 ],
[" ASUS F2A85-V PRO FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 129.99 ],
[" MSI AM1I AM1 SATA 6Gb/s USB 3.0 HDMI Mini ITX AMD Motherboard ", 35.99 ],
[" GIGABYTE GA-F2A75M-HD2 (rev. 3.0) FM2+ AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 64.99 ],
[" MSI 760GMA-P34(FX) AM3+ AMD 760G SATA 6Gb/s USB 3.0 Micro ATX AMD Motherboard ", 59.99 ],
[" ECS A55F-M4 (V2.0) FM1 AMD A55 (Hudson D2) HDMI Micro ATX AMD Motherboard ", 49.99 ],
[" ASRock FM2A75M-HD+ FM2+ / FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 59.99 ],
[" ECS A970M-A DELUXE v1.0 AM3+ AMD 970 + SB950 SATA 6Gb/s USB 3.0 ATX AMD Motherboard ", 74.99 ],
[" ASUS A85XM-A FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 75.99 ],
[" Refurbished: ASUS F2A85-M PRO FM2 AMD A85X (Hudson D4) SATA 6Gb/s USB 3.0 HDMI Micro ATX AMD Motherboard ", 129.99 ],
[" Open Box: ASRock FM2A75 Pro4 FM2 AMD A75 (Hudson D3) SATA 6Gb/s USB 3.0 HDMI ATX AMD Motherboard ", 67.99 ]]

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "computerbuilder.settings")

    from builds.models import BuildsTable

    mobo = BuildsTable.objects.all()
    print mobo

#moboDB = open("db.txt", "r")
#lines = moboDB.read().split('\",')
#print lines

def main():
    global lines
    global BuildsTable
    
    for item in moboList:
        try:
            mobo = "%s" % item[0]
            #mobo = BuildsTable(moboListing="%s" % item[0])
        except BuildsTable.DoesNotExist:
            mobo = 1
        try:
            price = "%s" % item[1]
            #price_local = BuildsTable(moboListing="%s" % item[1])
        except BuildsTable.DoesNotExist:
            price_local = 1
        """    
        if(BuildsTable.objects.filter(
            moboListing = mobo, price = price_local).exists() == False):
        """
        print mobo
        mydb = BuildsTable.objects.create(moboListing = mobo, price = price_local)
        
        print mydb
        mydb.save()
                    
main()
