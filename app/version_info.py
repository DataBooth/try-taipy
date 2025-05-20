import sys
import platform
from typing import Dict

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


class VersionInfo:
    """
    Collects and exposes information about the Python runtime, Taipy version, and operating system.
    """

    def __init__(self) -> None:
        self.python_version: str = sys.version.split()[0]
        if platform.system() == "Darwin":
            self.os_name: str = "macOS"
            self.os_version: str = platform.mac_ver()[0]  # User-facing version
        else:
            self.os_name: str = platform.system()
            self.os_version: str = platform.release()
        try:
            self.taipy_version: str = version("taipy")
        except PackageNotFoundError:
            try:
                self.taipy_version = version("taipy-gui")
            except PackageNotFoundError:
                self.taipy_version = "unknown"

    @property
    def os_full(self) -> str:
        return f"{self.os_name} {self.os_version}"

    def as_dict(self) -> Dict[str, str]:
        return {
            "python_version": self.python_version,
            "taipy_version": self.taipy_version,
            "os_name": self.os_name,
            "os_version": self.os_version,
            "os_full": self.os_full,
        }
