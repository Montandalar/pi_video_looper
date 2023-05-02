import re
import pyalsa.alsacard

# Return a device ID (hwid)
def parse_device_name(searchName):
    for cardNo in pyalsa.alsacard.card_list():
        cardName = pyalsa.alsacard.card_get_name(cardNo)
        if cardName == searchName:
            return cardNo

def parse_hw_device(s):
    if not s:
        return None

    m = re.match("^(\d+),(\d+)$", s)

    if not m:
        m = parse_device_name(s)
        if not m:
            raise RuntimeError('Invalid value for alsa hardware device: {}'.format(s))
    
    return tuple(map(int, m.group(1, 2)))
