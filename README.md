# Assignments_46W38

My assignments for the DTU course **46W38 - Practical Programming for Wind Energy**.

**Author:** Sergio Correa

## A note about conda channels

I'm using the recommended setup for this course (Git, Miniconda and VS Code), but I install packages from **conda-forge** instead of Anaconda's default channels.

When I first ran `conda create`, it stopped and asked me to accept Anaconda's Terms of Service. Those default channels need a paid license for companies with more than 200 employees, and I'm working from a corporate laptop. conda-forge is a community channel without that restriction, and I understand that it has everything this course needs.

If you run into the same error, this is how I solved it:

    conda config --add channels conda-forge
    conda config --set channel_priority strict
    conda create -n 46W38 python=3.13 -c conda-forge --override-channels