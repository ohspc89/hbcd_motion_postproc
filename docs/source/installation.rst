Installation
============

The intended use of this pipeline is through the use of `Singularity <https://docs.sylabs.io/guides/3.7/user-guide/index.html>`_
or `Docker <https://docs.docker.com/get-started/>`_ image.

.. note::
   Please refer to `Docker Desktop license agreement <https://docs.docker.com/subscription/desktop-license/>`_ 
   if you are using :ref:`option2-docker`. 
   Basically, if you are working at a research institute that has more than 250 employees AND
   more than $10 million in annual revenue, you need a paid subscription to use the service.

.. _option1-singularity:

Option 1: Singularity
---------------------
If you are new to it, start by installing ``SingularityCE`` following this
`instructions <https://docs.sylabs.io/guides/4.2/user-guide/quick_start.html#quick-installation-steps>`_ .
This page assumes users to install SingularityCE 4.2, the latest version as of Dec 18, 2024.

As the guide specifies, SingularityCE cannot run natively on Windows or Mac.

On a Windows Machine
^^^^^^^^^^^^^^^^^^^^
Please refer to this `blog <https://www.blopig.com/blog/2021/09/using-singularity-on-windows-with-wsl2/>`_
to install ``Windows System for Linux (WSL2)`` and then install SingularityCE.

.. note::
   Ubuntu 22.04.5 (LTS) has been tested instead of 20.04 (LTS) showcased in the blog post.
   Also, you may need to install more dependencies than what's described in the blog post.
   Prioritize this `page <https://docs.sylabs.io/guides/4.2/admin-guide/installation.html#install-dependencies>`_
   when installing system dependencies.

On a Mac Machine
^^^^^^^^^^^^^^^^
Please refer to this `guide <https://docs.sylabs.io/guides/latest/admin-guide/installation.html#mac>`_ to install SingularityCE with ``lima``.

Your institution's firewall setting may interfere with the installation. Then an alternative option is to use `vagrant <https://pawseysc.github.io/singularity-containers/44-setup-singularity/index.html>`_. Again if your institution's firewall setting is strict, please download the virtual box using ``--insecure`` argument (check the accepted answer to this `posting <https://stackoverflow.com/questions/42718527/vagrant-up-command-throwing-ssl-error>`_).

Then use the following command to pull the docker image as a ``Singularity``: ::
        
        singularity pull docker://inclab/hbcd_motion_postproc:<version_num>

where ``version_num`` denotes the specific version of the container. All available
versions of the container can be found `here <https://hub.docker.com/r/inclab/hbcd_motion_postproc/tags>`_.
If you are unsure of which version to use, use the tag: ``latest``.

The full usage details can be seen under the :ref:`usage` section, but
the basic command to run the container using ``Singularity`` is as follows: ::

        bids_dir=/path/to/bids_dir
        output_dir=/path/to/output_dir
        container=/path/to/container
        analysis_level=participant

        singularity run -B $bids_dir:/bids \
        -B $output_dir:/out \
        $container /bids /out $analysis_level

where the following folder hierarchy is assumed in this case: ::

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

.. note::
   Please create your ``output_dir`` before running Singularity if you are running WSL2.

.. _option2-docker:

Option 2: Docker
----------------
Again, if you are new, start by getting ``Docker Desktop`` using
this `link <https://docs.docker.com/get-started/introduction/get-docker-desktop/>`_ .

If you are a Mac user, refer this `website <https://docs.cse.lehigh.edu/determine-mac-architecture/>`_ to
determine the architecture of your machine (Apple silicon vs. Intel chip).

After installing ``Docker Desktop``, run the application. This will launch the
Docker Daemon and you will be able to use the ``docker pull`` command 
described at the top of this page.

Use the following command to pull the docker image. Again, if unsure of the version to use,
use the tag: ``latest``. ::

        docker pull inclab/hbcd_motion_postproc:<version_num>

Building the image from the scratch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The image can be built using the ``Dockerfile`` found in the `repository <https://github.com/Infant-Neuromotor-Control-Lab/hbcd_motion_postproc>`_.

Running the container using ``Docker`` is similar to doing so with ``Singularity``. Here is the basic command::

        bids_dir=/path/to/bids_dir
        output_dir=/path/to/output_dir
        analysis_level=participant

        docker run -it -v $bids_dir:/bids_dir \
        inclab/hbcd_motion_postproc:<version_num> \
        /bids_dir /output_dir $analysis_level

Both ``bids_dir`` and ``output_dir`` should be provided as *absolute paths*

(ex. "/Users/user1/Documents/DATA", "/home/user1/Documents/DATA" or "C:/Documents/DATA")

