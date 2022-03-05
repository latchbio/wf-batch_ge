BATCH-GE hosted with the Latch SDK 
---

This is an implementation of the BATCH-GE gene editing analysis tool using the
[Latch SDK](https://docs.latch.bio).

> BATCH-GE detects and reports indel mutations and other precise genome editing
> events and calculates the corresponding mutagenesis efficiencies for a large
> number of samples in parallel.

- [Repo](https://github.com/WouterSteyaert/BATCH-GE)
- [Paper](https://www.nature.com/articles/srep30330)

## Uploading your own BATCH-GE

The contents of this repository were modified from the boilerplate provided by
`latch init`.

You can create your own workflow by 

You can replicate the contents of this repo by installing latch and creating
some boilerplate like so:

```
$ pip install latch
$ latch init wf-batch_ge
$ cd wf-batch_ge
```

You will notice the structure of your boilerplate repository is roughly the same
as this repository. Just modify the code in the `wf/__init__.py` and the
`Dockerfile`, run `latch register` and you should be able to upload your own
version of BATCH-GE.
