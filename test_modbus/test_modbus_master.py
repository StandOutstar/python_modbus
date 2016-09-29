import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = "COM11"
def main():
    logger = modbus_tk.utils.create_logger("console")
    try:
        # Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")
        # write single register
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x2000, output_value=8))
        # read holding registers
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0x2000, 3))

    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

if __name__ == "__main__":
    main()