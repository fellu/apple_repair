import subprocess
import logging
import json

from typing import Optional


class Idevice:
    """
    Python wrapper for idevice
    """

    def __init__(self, idevice_path="/usr/bin/"):
        self.log = logging.getLogger(__class__.__name__)
        self.id: Optional[str] = None
        self.idevice_path = idevice_path

    def list(self, via="usb"):
        """
        Returns list of idevices
        :param via: type of connected idevice, usb or network
        :return: dict with connected idevices
        """
        if via == "usb":
            param = "-l"
        elif via == "network":
            param = "-n"
        else:
            self.log.error(f"Unknown list type {via}")
            return

        cmd = [f"{self.idevice_path}/idevice_id", param]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output = process.communicate()[0].decode('utf8').split()
        process.wait()
        return output

