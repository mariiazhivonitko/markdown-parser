import re
import pandas as pd

# The text containing the table
text = """
Here are the proposed headers, possible units, and data types for the columns:

| Header | Possible Units | Data Type |
| --- | --- | --- |
| Date | YYYY-MM-DD, DD-MM-YYYY, MM-DD-YY | date |
| Time | HH:MM:SS, HHMMSS | time |
| Distance | meters, kilometers, miles | float |
| Speed | km/h, mph, m/s | float |
| Pace | minutes per kilometer, minutes per mile, seconds per meter | float |
| Cadence | steps per minute, revolutions per minute | float |
| Power | watts | float |
| Heart Rate | beats per minute | int |
| Activity Type | walking, running, cycling | string |
| User Name | text | string |

Please note that the above headers are just proposed and may need to be adjusted based on the specific requirements of your data analysis.
"""

match = re.search(r"(\|[^\n]+\|\n(?:\|[^\n]+\|\n?)+)", text)
table_text = match.group(1)

table_lines = table_text.strip().split("\n")

cleaned_lines = [line.strip("|") for line in table_lines]




print(cleaned_lines)

