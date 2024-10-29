Installation
============

The intended use of this pipeline is through the use of `Docker <https://docs.docker.com/get-started/>`_
image. The image can be built using the Dockerfile found in the `repository <https://github.com/Infant-Neuromotor-Control-Lab/hbcd_motion_postproc>`_,
or it can be pulled from DockerHub using the following command: ::

        docker pull inclab/hbcd_motion_postproc:<version_num>

where version_num denotes the specific version of the container. All available
versions of the container can be found `here <https://hub.docker.com/r/inclab/hbcd_motion_postproc/tags>`_.

After downloading the container, docker is the only other dependency needed
for processing. The full usage details can be seen under the :ref:`usage` section, but
the basic command to run the container is as follows ::

        bids_dir=/path/to/bids_dir
        output_dir=/path/to/output_dir
        container=/path/to/container
        analysis_level=participant

        singularity run -B $bids_dir:/HBCD \
        -B $output_dir:/out \
        $container /bids /out $analysis_level

where the following folder hierarchy is assumed in this case ::

        bids_dir/
        |-- participants.tsv
        |-- participants.json
        |-- sub-<label>/
        |   |-- sub-<label>_sessions.tsv
        |   |-- sub-<label>_sessions.json
        |   |-- ses-<label>/
        |   |   |-- motion/
        |   |   |-- sub-<label>_ses-<label>_scans.tsv
        |   |   |-- sub-<label>_ses-<label>_scans.json
