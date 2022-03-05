"""
Batch-GE
"""

import subprocess
from enum import Enum
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchDir, LatchFile


class Genome(Enum):
    danRer7 = "danRer7"


@small_task
def batch_ge_task(
    fastq_dir: LatchDir,
    sample_numbers: int,
    genome: Genome,
    cut_site: str,
    output_dir: LatchDir,
    cut_sites_file: LatchFile,
    repair_seq: str,
) -> LatchDir:

    exp_file = Path("/root/exp_file.csv")

    with open(exp_file, "w") as f:
        f.write(
            "FastqDir;SampleNumbers;Genome;CutSite;OutputDir;CutSitesFile;RepairSequence;"
        )
        f.write(
            f"{Path(fastq_dir).resolve()};{sample_numbers};{genome.value};{cutsite};{Path(output_dir).resolve()};{Path(cut_sites_file).resolve()};{repaire_seq};"
        )

    _batch_ge_subprocess = ["perl", "BATCH-GE.pl", "--ExperimentFile", str(exp_file)]

    subprocess.run(_batch_ge_subprocess, check=True)

    return output_dir


@workflow
def batch_ge(
    fastq_dir: LatchDir,
    sample_numbers: int,
    genome: Genome,
    cut_site: str,
    output_dir: LatchDir,
    cut_sites_file: LatchFile,
    repair_seq: str,
) -> LatchDir:
    """BATCH-GE detects and reports indel mutations and other precise genome editing events

    BATCH-GE
    ----

    BATCH-GE detects and reports indel mutations and other precise genome editing
    events and calculates the corresponding mutagenesis efficiencies for a large
    number of samples in parallel. Furthermore, this new tool provides flexibility
    by allowing the user to adapt a number of input variables.

    __metadata__:
        display_name: BATCH-GE
        author:
            name: Woutert Steyaert
            email:
            github:
        repository: https://github.com/WouterSteyaert/BATCH-GE
        license:
            id: MIT

    Args:

        fastq_dir:
          A directory with the FastQ files to be processed by BATCH-GE.

          __metadata__:
            display_name: FastQ Dir

        sample_numbers:
          I'm not actually sure, TBD

          __metadata__:
            display_name: Sample Number

        genome:
          Reference genome to use in analysis

          __metadata__:
            display_name: Reference Genome

        cut_site:
          The gene symbol for the cut site, eg. PLS3.

          __metadata__:
            display_name: Cut Site Gene Symbol

        output_dir:
          The directory where results will go.

          __metadata__:
            display_name: Output Directory

        cut_site_files:
          A BED file specifying cut sites.

          __metadata__:
            display_name: Cut Site BED File

        repair_seq:
          A string specifying the desired repair sequence.

          __metadata__:
            display_name: Repair Sequence

    """

    return batch_ge_task(
        fastq_dir=fastq_dir,
        sample_numbers=sample_numbers,
        genome=genome,
        cut_site=cut_site,
        output_dir=output_dir,
        cut_sites_file=cut_sites_file,
        repair_seq=repair_seq,
    )
