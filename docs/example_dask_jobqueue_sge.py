#!/usr/bin/env python3
import os
import dask.array as da
from dask_jobqueue import SGECluster
from dask.distributed import Client, performance_report


def setup_client_and_cluster(
    number_processes=1, number_jobs=1, walltime="00:01:00", memory=1
):
    """
    Setup Dask client and cluster.
    Ensure that the number of workers is the right amount
    for your job and will be fully utilised.
    """
    print("Setting up Dask client and cluster ...")
    # number of workers used for number of partitions
    number_workers = number_processes * number_jobs
    # these are the requirements for a single worker
    cluster = SGECluster(
        interface="ib0",
        walltime=walltime,
        memory=f"{memory} G",
        resource_spec=f"h_vmem={memory}G",
        scheduler_options={"dashboard_address": ":2727"},
        job_extra=[
            "-V",  # export all environment variables
            f"-pe smp {number_processes}",
            f"-l disk={memory}G",
        ],
        local_directory=os.sep.join([
            os.environ.get("PWD"),
            "dask-worker-space"]),
    )
    client = Client(cluster)
    cluster.scale(jobs=number_jobs)
    print("The resources of each worker are: ")
    print(cluster.job_script())
    return client, cluster


def example_function():
    x = da.random.random(
        (100_000, 100_000, 10),
        chunks=(10_000, 10_000, 5))
    y = da.random.random(
        (100_000, 100_000, 10),
        chunks=(10_000, 10_000, 5))
    z = (da.arcsin(x) + da.arccos(y)).sum(axis=(1, 2))

    with performance_report(filename="dask-report_jobqueue.html"):
        result = z.compute()


def main():
    client, cluster = setup_client_and_cluster(
        number_processes=1,
        number_jobs=8,
        walltime="01:00:00",
        memory=48,
    )

    print("Main processing ...")
    example_function()
    print("Finished processing.")

    client.close()
    cluster.close()
    print("Closed client and cluster.")


if __name__ == "__main__":
    main()
