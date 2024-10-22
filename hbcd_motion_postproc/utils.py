"""
utils.py currently saves three functions:
    - get_age_from_tsv
    - get_age_units
    - age_to_months

These functions are ALL from the NiBabies package
(https://github.com/nipreps/nibabies/tree/master)

Only the original `_get_age_from_tsv` is modified
so that it will search for rows with the filenames
starting with 'motion'.
"""
from pathlib import Path
import json
import typing as ty
import pandas as pd

SUPPORTED_AGE_UNITS = (
        'weeks',
        'months',
        'years',
        )


def get_age_from_tsv(
        bids_tsv: Path,
        index_column: str | None = None,
        index_value: str | None = None,
        ) -> float | None:
    """
    Parameters
    ----------
    bids_tsv: pathlib.Path object
        sub-{label}_ses-{label}_scans.tsv file

    index_column: str
        "filename", the column that lists the name of the files

    index_value: str
        r'^motion.*', the prefix of the motion related files

    Returns
    -------
    age_months: int
        age in months, output of `age_to_months()`
    """

    df = pd.read_csv(str(bids_tsv), sep='\t')
    age_col = None

    for column in ('age_years', 'age'):
        if column in df.columns:
            age_col = column
            break

    if age_col is None:
        return

    df = df[df[index_column].str.fullmatch(index_value)]
    # One more time! Only 'primary'
    df = df[df[index_column].str.endswith('primary_motion.tsv')]

    try:
        # extract age value from row
        # the age must be from the 'primary' file
        age = float(df.loc[df.index[0], age_col].item())
    except:
        return

    if age_col == 'age':
        # verify age is in months
        bids_json = bids_tsv.with_suffix('.json')
        age_units = _get_age_units(bids_json)
        if age_units is False:
            raise FileNotFoundError(
                    f'Could not verify age unit for {bids_tsv.name} - ensure a sidecar JSON '
                    'describing column `age` units is available.'
                    )
    else:
        age_units = age_col.split('_')[-1]

    age_months = age_to_months(age, units=age_units)
    return age_months


def _get_age_units(bids_json: Path) -> ty.Literal['weeks', 'months', 'years', False]:
    """
    Get the unit of the measure `age` from sub-{label}_ses-{label}_scans.json

    A typical json file will have an item:
    
        ...
        "age": {
            "Description": "Age (in years) of the candidate at the time of the scan",
            "Units": "years"
        },
        ...
    """
    try:
        data = json.loads(bids_json.read_text())
    except (json.JSONDecodeError, OSError):
        return False

    units = data.get('age', {}).get('Units', '')
    if not isinstance(units, str):
        # Multiple units confuse us
        return False

    if units.lower() in SUPPORTED_AGE_UNITS:
        return units.lower()
    return False


def age_to_months(age: int | float, units: ty.Literal['weeks', 'months', 'years']) -> int:
    """
    Convert a given age, in either "weeks", "months", or "years", into months.

    >>> age_to_months(1, 'years')
    12
    >>> age_to_months(0.5, 'years')
    6
    >>> age_to_months(2, 'weeks')
    0
    >>> age_to_months(3, 'weeks')
    1
    >>> age_to_months(8, 'months')
    8
    """
    WEEKS_TO_MONTH = 0.230137
    YEARS_TO_MONTH = 12

    if units == 'weeks':
        age *= WEEKS_TO_MONTH
    elif units == 'years':
        age *= YEARS_TO_MONTH
    return int(round(age))
