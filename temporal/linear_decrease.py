import json
from collections.abc import Mapping
from numbers import Number
from typing import Any, Union

import bw_temporalis as bwt
import numpy as np


class LinearDecreaseOverTime(bwt.TDAware):
    # Make sure that we control multiplication
    _mul_comes_first = True

    def __init__(
        self,
        start_dt: str,
        start_value: Number,
        end_dt: str,
        end_value: Number,
        **kwargs: Any,
    ):
        self._start_str = start_dt
        self._end_str = end_dt

        self.start = np.array(start_dt, dtype="datetime64[s]").astype(int)
        self.end = np.array(end_dt, dtype="datetime64[s]").astype(int)
        if not self.end > self.start:
            raise ValueError("`start` must come before `end`")

        self.a, self.b = float(start_value), float(end_value)

    def __mul__(
        self, other: Union[bwt.TemporalDistribution, Number]
    ) -> Union[bwt.TemporalDistribution, "LinearDecreaseOverTime"]:
        if isinstance(other, bwt.TDAware):
            raise ValueError("Can't multiply two dynamic functions")
        elif isinstance(other, Number):
            return LinearDecreaseOverTime(
                start_dt=self._start_str,
                start_value=self.a * other,
                end_dt=self._end_str,
                end_value=self.b * other,
            )
        elif isinstance(other, bwt.TemporalDistribution):
            if not other.base_time_type == bwt.temporal_distribution.datetime_type:
                raise ValueError("Can't multiply by relative distribution")
            new_data = np.array(
                [
                    self.value_at_time(value=what, dt=when)
                    for what, when in zip(other.amount, other.date.astype(int))
                ]
            )
            return bwt.TemporalDistribution(date=other.date, amount=new_data)
        else:
            raise ValueError(
                "Can't multiply `LinearDecreaseOverTime` and {}".format(type(other))
            )

    def value_at_time(self, value: Number, dt: np.timedelta64) -> float:
        if dt <= self.start:
            return self.a
        elif dt >= self.end:
            return self.b
        else:
            fraction = (self.end - dt) / (self.end - self.start)
            return min(self.a, self.b) + abs(self.a - self.b) * fraction

    def to_json(self) -> str:
        return json.dumps(
            {
                "__loader__": "LinearDecreaseOverTime",
                "start_dt": self._start_str,
                "end_dt": self._end_str,
                "start_value": self.a,
                "end_value": self.b,
            }
        )

    @classmethod
    def from_json(cls, json_obj):
        if isinstance(json_obj, Mapping):
            data = json_obj
        elif isinstance(json_obj, str):
            data = json.loads(json_obj)
        else:
            raise ValueError(f"Can't understand `from_json` input object {json_obj}")
        return cls(**data)


bwt.loader_registry["LinearDecreaseOverTime"] = LinearDecreaseOverTime.from_json
