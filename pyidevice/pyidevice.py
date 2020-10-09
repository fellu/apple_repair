import subprocess
import logging

from typing import Optional


class Idevice:
    """
    Python wrapper for idevice
    """

    def __init__(self, idevice_path="/usr/bin/"):
        self.log = logging.getLogger(__class__.__name__)
        self.iid: Optional[str] = ""
        self.idevice_path = idevice_path

    def list(self, via: str = "usb"):
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

    def info(self) -> dict:
        """
        Fetches idevice info for active idevice
        :return: dict with ideviceinfo return values
        """
        cmd = [f"{self.idevice_path}/ideviceinfo", self.iid]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output = filter(None, process.communicate()[0].decode('utf8').split('\n'))
        output = dict(s.split(': ', 1) for s in output)
        process.wait()
        return output
