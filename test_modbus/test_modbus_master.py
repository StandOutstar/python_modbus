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
            serial.Serial(port=PORT, baudrate=115200, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")

        # read holding registers
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0x0001, quantity_of_x=10))
        # write single register
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x1000, output_value=8))
        # read holding registers
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0x0100, quantity_of_x=4))
        # write multiple register
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2000, quantity_of_x=7, output_value={1, 2, 3, 4, 5, 6, 7}))
        # read holding registers
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0x001C, quantity_of_x=6))

    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

if __name__ == "__main__":
    main()
