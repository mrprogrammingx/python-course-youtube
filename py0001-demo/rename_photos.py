from pathlib import Path

photos = sorted(Path("trip_photos").glob("IMG_*.jpg"))
for number, photo in enumerate(photos, start=1):
    photo.rename(photo.with_name(f"trip-{number:04}.jpg"))
print(f"Renamed {len(photos)} files.")
