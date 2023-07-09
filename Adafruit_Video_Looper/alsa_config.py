import re
import pyalsa.alsacard

class AlsaConfig:
    # Return a device ID (hwid)
    def parse_device_name(searchName):
        for cardNo in pyalsa.alsacard.card_list():
            cardName = pyalsa.alsacard.card_get_name(cardNo)
            print("cardName = '{}', searchName = '{}'".format(cardName, searchName))
            if cardName == searchName:
                print("match! {}".format(cardNo))
                return cardNo
        print("No match :(")

    def parse_hw_device_tuple(s):
        if not s:
            return None

        m = re.match("^(\d+),(\d+)$", s)

        if m:
            return tuple(map(int, m.group(1, 2)))

        m = AlsaConfig.parse_device_name(s)
        if m is not None:
            return (m)
        else:
            raise RuntimeError('Invalid value for alsa hardware device: {}'.format(s))

    def parse_hw_device_str(s):
        if not s:
            return None

        print("===")
        m = re.match("^(\d+),(\d+)$", s)
        print(s)
        print(m)
        if m is not None and len(m.groups()) == 2:
            print("Match on hwid")
            return s

        m = AlsaConfig.parse_device_name(s)
        print("str(m) = {}".format(str(m)))
        if m is not None:
            print("Match on nice name: {}".format(str(m)))
            return str(m)
        else:
            raise RuntimeError('Invalid value for alsa hardware device: {}'.format(s))
