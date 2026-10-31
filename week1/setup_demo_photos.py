"""Create 1,800 messy demo files for the PY-0001 screen recording.

Run it again before every take: it resets the folder.
Only files named IMG_*.jpg or trip-*.jpg inside trip_photos are ever deleted.
"""
from pathlib import Path

folder = Path("trip_photos")
folder.mkdir(exist_ok=True)

for old in [*folder.glob("IMG_*.jpg"), *folder.glob("trip-*.jpg")]:
    old.unlink()

for number in range(4821, 4821 + 1800):
    (folder / f"IMG_{number}.jpg").write_bytes(b"")

print(f"Ready: 1,800 messy files in {folder.resolve()}")
