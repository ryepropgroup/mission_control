from labjack import ljm
from time import sleep, time
sensor_name = input("Enter test name: ").upper()

handle = ljm.openS("ANY", "ANY", "ANY")

info = ljm.getHandleInfo(handle)
print(
    "Opened a LabJack with Device type: %i, Connection type: %i,\n"
    "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i"
    % (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5])
)

# Setup and call eReadName to read from AIN0 on the LabJack.
handles = ["AIN0","AIN2","AIN4","AIN6","AIN8"]
names = {"AIN0":["AIN0_NEGATIVE_CH", "AIN0_RANGE"],
         "AIN2":["AIN2_NEGATIVE_CH", "AIN2_RANGE"],
         "AIN4":["AIN4_NEGATIVE_CH", "AIN4_RANGE"],
         "AIN6":["AIN6_NEGATIVE_CH", "AIN6_RANGE"],
         "AIN8":["AIN8_NEGATIVE_CH", "AIN8_RANGE"]
}
values = [0,0,0,0,0]
ljm.eWriteNames(handle, len(names[handles[0]]), names[handles[0]], [1.0, 0.1])
ljm.eWriteNames(handle, len(names[handles[1]]),names[handles[1]], [3.0, 0.1])
ljm.eWriteNames(handle, len(names[handles[2]]),names[handles[2]] ,[5.0, 0.1])
ljm.eWriteNames(handle, len(names[handles[3]]),names[handles[3]],[7.0, 0.1])
ljm.eWriteNames(handle, len(names[handles[4]]),names[handles[4]] ,[9.0, 0.1])
with open(f"{sensor_name}.txt", "w+") as f:
#with open(f"logs/{sensor_name}_{int(time.time())}.txt", "w+") as f:
    while True:
        sleep(0.001)
        for i in range(len(values)):
            values[i] = ljm.eReadName(handle, handles[i])*25000
            
        for i in range(len(handles)):
            print("\n%s P%d : %f" % (handles[i],i+1, values[i]))
        f.write(f"{time()},{values[0]},{values[1]},{values[2]},{values[3]},{values[4]}\n")