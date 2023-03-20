# Copyright 2023
# Author: Jason Bigelow
# License: GNU GPLv2, see LICENSE.txt
import pyudev

class USBDriveFinder:
    """Finds and returns USB drive partitions that are mountable. Should be a
        short-lived object"""

    def __init__(self, context):
        self._context = context

    def get_leaves(self):
        return [x.device_node for x in self._context.list_devices(subsystem='block')
                if  'ID_BUS' in x.properties
                and 'ID_FS_UUID' in x.properties
                and x.properties['ID_BUS'] == 'usb']
