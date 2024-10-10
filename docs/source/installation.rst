.. _usage:

Installation
============

The intended use of this pipeline is through the use of `Docker <https://docs.docker.com/get-started/>`_
image. The image can be built using the Dockerfile found in the `repository <https://github.com/Infant-Neuromotor-Control-Lab/hbcd_motion_postproc>`_,
or it can be pulled from DockerHub using the following command: ::

        docker pull inclab/hbcd_motion_postproc:<version_num>

where version_num denotes the specific version of the container. All available
versions of the container can be found `here <https://hub.docker.com/r/dcanumn/hbcd_motion_postproc/tags>`_.

After downloading the container, docker is the only other dependency needed
for processing. The full usage details can be seen under the :ref:`usage` section, but
the basic command to run the container is as follows ::

        parent_dir=/parent/path/to/bids_dir (ex. /Users/joh/Downloads/hbcd)
        bids_dir=bids_dir_folder_name       (ex. motion_data)
        output_dir=output_dir_folder_name   (ex. motion_output)
        analysis_level=participant

        docker run -v $parent_dir:/HBCD \
            inclab/hbcd_motion_postproc \
            /HBCD/$bids_dir \
            /HBCD/$output_dir \
            $analysis_level

where the following folder hierarchy is assumed in this case ::

        Users
        |-- joh
            |-- Downloads
                |-- hbcd
                    |-- motion_data
                        |-- sub-XXXXXX
                        |-- sub-YYYYYY
                        |-- sub-ZZZZZZ
                        |-- ...
