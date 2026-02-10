from importlib.metadata import PackageNotFoundError, version

try:
    # PyPI distribution name (usually uses hyphens)
    __version__ = version("network-spatial-coherence")
except PackageNotFoundError:
    # Fallback for editable installs / source checkouts
    __version__ = "unknown"

