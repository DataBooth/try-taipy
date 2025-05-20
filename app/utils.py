import platform
import sys
from functools import cache
from pathlib import Path
from typing import Dict, Optional, Union

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  # type: ignore


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


class TaipyTemplateHelper:
    """
    Helper for loading and caching Taipy Markdown templates from file,
    supporting flexible path and base_dir types.
    """

    @staticmethod
    @cache
    def load(
        template_path: Union[str, Path],
        base_dir: Optional[Union[str, Path]] = None,
        encoding: str = "utf-8",
    ) -> str:
        """
        Load a template from file, resolving relative paths from base_dir or cwd.

        Args:
            template_path (str or Path): Filename or relative/absolute path of the template.
            base_dir (str or Path, optional): Base directory for relative paths. Defaults to current working directory.
            encoding (str): File encoding (default: 'utf-8').

        Returns:
            str: The template string.

        Raises:
            FileNotFoundError: If the file does not exist.
            OSError: For other file reading errors.
        """
        path = Path(template_path)
        if not path.is_absolute():
            base = Path(base_dir) if base_dir is not None else Path.cwd()
            path = (base / path).resolve()

        try:
            return path.read_text(encoding=encoding)
        except FileNotFoundError:
            print(f"[TaipyTemplateHelper] Template file not found: {path}")
            raise
        except Exception as e:
            print(f"[TaipyTemplateHelper] Error loading template '{path}': {e}")
            raise

    @staticmethod
    def clear_cache():
        """Clear the template cache."""
        TaipyTemplateHelper.load.cache_clear()
