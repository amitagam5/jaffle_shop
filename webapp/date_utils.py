import datetime as dt
from typing import Optional

import dateutil.parser


def get_date_from_str(value: Optional[str]) -> Optional[dt.date]:
    try:
        return dateutil.parser.parse(value)
    except (dateutil.parser.ParserError, TypeError):
        return None
