import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_rtu as modbus_rtu
import modbus_tk.hooks as hoook
import serial
import time
import array


def hookbefore_handle_request( requestpdu ):
    # request is a str like '\x01\x06\x00\x01\x00\x01\x19\xca'
    s = array.array('B',requestpdu[1])

    if s[0] == 0x01:
        print ("recievd ")
        if s[2] == 0x20:
            print ("multiple action")


hoook.install_hook("modbus.Server.before_handle_request", hookbefore_handle_request)

logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")
# create server
server = modbus_rtu.RtuServer(serial.Serial("COM10", baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
slaver = server.add_slave(1)

slaver.add_block("holdingResgiter", cst.HOLDING_REGISTERS, 0, 16383)
slaver.set_values("holdingResgiter", 0x2000, (2, 3, 4))

def loop():
    logger.info("running...")
    #start server
    server.start()
    print (slaver.get_values( "holdingResgiter", 0x2000, 3))
    while True:
        time.sleep(0.5)
def destory():
    logger.info("destory")
    #stop server
    server.stop()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destory()