# Copyright (c) 2026 Arthur Putnam
# MIT License - see LICENSE file for details

"""Install and verify the PlantUML runtime (JAR + Java) for the plantuml skill.

Usage:
    python install_plantuml.py [--dest <path>]

Exits with code 0 if PlantUML is ready to use, non-zero on failure.
"""

import argparse
import hashlib
import logging
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

PLANTUML_RELEASES_URL = "https://github.com/plantuml/plantuml/releases"
PLANTUML_DOWNLOAD_URL = (
    "https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar"
)
DEFAULT_DEST = Path(__file__).parent / "plantuml.jar"


def java_available() -> bool:
    """Check whether a Java runtime is available on PATH.

    Returns:
        True if `java` is found on PATH, False otherwise.
    """
    return shutil.which("java") is not None


def jar_works(jar_path: Path) -> bool:
    """Verify that the JAR at jar_path is executable by Java.

    Args:
        jar_path: Path to plantuml.jar.

    Returns:
        True if `java -jar <jar_path> -version` exits with code 0.
        False if Java is not found on PATH, the process times out,
        or the JAR exits with a non-zero code.
    """
    try:
        result = subprocess.run(
            ["java", "-jar", str(jar_path), "-version"],
            capture_output=True,
            timeout=15,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def sha256(path: Path) -> str:
    """Compute the SHA-256 hex digest of a file.

    Args:
        path: Path to the file to hash.

    Returns:
        Lowercase hex string of the SHA-256 digest.
    """
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def download_jar(dest: Path) -> None:
    """Download the latest plantuml.jar from GitHub releases.

    Args:
        dest: Destination path to write the JAR file.

    Raises:
        RuntimeError: If the download fails or the file cannot be written.
    """
    log.info(f"Downloading plantuml.jar to {dest} ...")
    try:
        urllib.request.urlretrieve(PLANTUML_DOWNLOAD_URL, dest)  # noqa: S310
    except Exception as e:
        raise RuntimeError(f"Download failed: {e}") from e
    log.info("Download complete.")
    log.info(f"SHA-256: {sha256(dest)}")
    log.info(f"Verify checksum against published values at {PLANTUML_RELEASES_URL}")


def main() -> None:
    """Ensure PlantUML is installed and working.

    Checks for Java, checks for an existing JAR, downloads if missing,
    and verifies the JAR runs correctly. Exits non-zero on any failure.
    """
    parser = argparse.ArgumentParser(description="Install and verify PlantUML runtime.")
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEFAULT_DEST,
        help=f"Where to save plantuml.jar (default: {DEFAULT_DEST})",
    )
    args = parser.parse_args()
    dest: Path = args.dest.resolve()

    if not java_available():
        log.error("Java is not installed or not on PATH.")
        log.error("Install Java 8+ from https://adoptium.net/ and re-run this script.")
        sys.exit(1)

    if dest.exists():
        log.info(f"Found existing JAR at {dest}")
        if jar_works(dest):
            log.info("PlantUML is ready.")
            sys.exit(0)
        log.warning("Existing JAR failed verification — re-downloading.")
        dest.unlink()

    try:
        download_jar(dest)
    except RuntimeError as e:
        log.error(str(e))
        sys.exit(1)

    if not jar_works(dest):
        log.error("Downloaded JAR failed verification. Check the file and your Java version.")
        sys.exit(1)

    log.info(f"PlantUML installed successfully at {dest}")
    log.info(f"Render a diagram with: java -jar {dest} diagram.puml")


if __name__ == "__main__":
    main()
