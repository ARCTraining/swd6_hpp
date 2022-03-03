#!/usr/bin/env python3
import dask.array as da
from dask_mpi import initialize
from dask.distributed import Client, performance_report

initialize()
client = Client()


def example_function():
    x = da.random.random(
        (100_000, 100_000, 10),
        chunks=(10_000, 10_000, 5))
    y = da.random.random(
        (100_000, 100_000, 10),
        chunks=(10_000, 10_000, 5))
    z = (da.arcsin(x) + da.arccos(y)).sum(axis=(1, 2))

    with performance_report(filename="dask-report_mpi.html"):
        result = z.compute()


if __name__ == "__main__":
    example_function()