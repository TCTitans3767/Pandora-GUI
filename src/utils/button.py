

class ButtonConfigByte:
    def __init__(self):
        self.isActive = False
        self.isSticky = False
        self.lightsUp = False
        self.returnsJoystickValue = False
        self.returnsPOVValue = False
        self.isSignalInverted = False
        self.buttonStartsActivated = False
        self.unused = False

    def toByte(self) -> int:
        byte = 0
        byte |= 0b00000001 if self.isActive else 0
        byte |= 0b00000010 if self.isSticky else 0
        byte |= 0b00000100 if self.lightsUp else 0
        byte |= 0b00001000 if self.returnsJoystickValue else 0
        byte |= 0b00010000 if self.returnsPOVValue else 0
        byte |= 0b00100000 if self.isSignalInverted else 0
        byte |= 0b01000000 if self.buttonStartsActivated else 0
        byte |= 0b10000000 if self.unused else 0
        return byte
    
    def hex(self) -> str:
        return hex(self.toByte())


class ButtonPayload:
    def __init__(self):
        self.buttonIDByteWidth: int
        self.groupIDByteWidth: int
        self.buttonID: int

        self.configByte = ButtonConfigByte()

    def __str__(self) -> str:
        ...



        


class Button:
    ...