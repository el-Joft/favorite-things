from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

message = b'gAAAAABdL2VTBe7-FwabXxhGB3PYX_G1qbsDtFDj8_Tsm76tN7GGa67ogiZFzZFFcclAtIGRU5mwB60UnepzC-E7nYWA5FA4ATP8iTnGeE4XCbqP20BTQ05CppfdEGME43E5RhTcxAhDcDPujbh1VTYL86sTA2xhfXrfLZHFWBJtm9PnQXYjWM0='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
  main()
