import re
import pandas as pd
from io import StringIO

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
text2 = """got it
| Some Title | Some Description             | Some Number |
|------------|------------------------------|-------------|  
| Dark Souls | This is a fun game           | 5           |
| Bloodborne | This one is even better      | 2           |
| Sekiro     | This one is also pretty good | 110101      |
"""

match = re.search(r"(\|[^\n]+\|\n(?:\|[^\n]+\|\n?)+)", text)

table_text = match.group(1)
print("match:",match)
table_lines = table_text.strip().split("\n")


# Remove the markdown separator row (lines containing only dashes)
table_lines = [line for line in table_lines if not all(c == '-' or c == ' ' for c in line.strip())]



cleaned_lines = [line.strip("|").split("|") for line in table_lines]
cleaned_cells = [list(map(str.strip, line)) for line in cleaned_lines]

df = pd.DataFrame(cleaned_cells[1:], columns = cleaned_cells[0])



print(df)

