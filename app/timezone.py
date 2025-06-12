import pytz
from datetime import datetime

def convert_to_timezone(dt: datetime, tz_name: str) -> datetime:

    try:
        target_tz = pytz.timezone(tz_name)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"Invalid timezone: {tz_name}")

    if dt.tzinfo is None:
        dt = pytz.UTC.localize(dt)
    else:
        dt = dt.astimezone(pytz.UTC)

    return dt.astimezone(target_tz).isoformat()

