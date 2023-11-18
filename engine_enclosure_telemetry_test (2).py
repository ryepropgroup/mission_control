import sys
import time
from labjack import ljm

handle = ljm.openS("ANY", "ANY", "ANY")
info = ljm.getHandleInfo(handle)

CJ_TEMP_CORRECTION = 0.0

#neg = ljm.eWriteName(handle, "AIN10_NEGATIVE_CH", 11)
neg = ljm.eWriteName(handle, "AIN2_NEGATIVE_CH", 3)


#for thermocouple voltage ranges 
#inj_1_range = ljm.eWriteName(handle, "AIN8_RANGE", 0.1)
#inj_2_range = ljm.eWriteName(handle, "AIN6_RANGE", 0.1)
#ign_range = ljm.eWriteName(handle, "AIN4_RANGE", 0.1)

try:
    while True:

        #AIN voltage grabs
        LoadCellVolts = ljm.eReadName(handle, "AIN2")
        # LoadCellVolts = ljm.eReadName(handle, "AIN12")
        inj_1_volts = ljm.eReadName(handle, "AIN5")
        inj_2_volts = ljm.eReadName(handle, "AIN6")
        ign_volts = ljm.eReadName(handle, "AIN4")
        cj_volts = ljm.eReadName(handle, "AIN14") # change if you're retarded
        p20_volts = ljm.eReadName(handle, "AIN1")
        p30_volts = ljm.eReadName(handle, "AIN7")
        # p_inj_volts = ljm.eReadName(handle, "AIN0")

        #thermocouple volts -> celsius conversion calcs 
        CJTempK = (cj_volts* -92.6 + 467.6)

      #  inj_1_TempK = ljm.tcVoltsToTemp(6004, inj_1_volts, CJTempK + CJ_TEMP_CORRECTION)
       # inj_2_TempK = ljm.tcVoltsToTemp(6004, inj_2_volts, CJTempK + CJ_TEMP_CORRECTION)
        # ign_TempK = ljm.tcVoltsToTemp(6004, ign_volts, CJTempK + CJ_TEMP_CORRECTION)

        #prints
        print("lode cell -> ",abs((LoadCellVolts*200)), "lbs", " ->",LoadCellVolts," volts")
        #print(abs((LoadCellVolts*100000)), "lbs")
      #  print("t1-> ",(inj_1_TempK -273), "Degrees C")
       # print("t2-> ",(inj_2_TempK -273), "Degrees C")
        # print("ign-> ",(ign_TempK - 273), "Degrees C")
        print("p20 ->",(p20_volts*300), "psi")
        print("p30 ->",(p30_volts*300), "psi")
        # print((p_inj_volts*300), "psi\n")

        time.sleep(0.5)
except KeyboardInterrupt:
    pass

ljm.close(handle)