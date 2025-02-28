.. _usage:

Usage
=====

| There are three primary inputs to the hbcd_motion_postproc tool.
| In each case, the input is provided as a "study-wide" folder, such
  that the tool can be run on multiple subjects at once. These three
  inputs include the BIDS directory, the output directory,
  and the analysis level (e.g., ``participant``).

| At the time this application is run, there should be subject (and session,
  if desired) specific folders for each subject you want to process.
| Processing will iterate through each subject in the BIDS directory,
  find associated sessions with the relevant data, and create the necessary
  folders and files in the output directory.
| Processing is totally independent across subjects and sessions, so that
  the results will be the same if the subjects are processed in parallel
  or through a single call of this applcation.

The application assumes data prepared following
`motion-BIDS <https://doi.org/10.1038/s41597-024-03559-8>`_.
For more details on the extension, see the linked documentation.

As described in the installation section, this tool is meant to be
interacted with in containerized form. 
The example below shows the general layout for how you may want to
interact with the container to conduct processing if you have the
``Singularity`` container::

        bids_dir=/path/to/bids_dir
        output_dir=/path/to/output_dir
        container=/path/to/container
        analysis_level=participant

        singularity run -B $bids_dir:/bids \
        -B $output_dir:/out \
        $container /bids /out $analysis_level

If you use ``Docker`` instead, use the following command to interact::

        docker run -it -v $bids_dir:/bids_dir \
        inclab/hbcd_motion_postproc:<version_num> \
        /bids_dir $output_dir $analysis_level

where ``version_num`` is the specific tag of the image you pulled.

To see more specific information about how this tool expects
the inputs to be formatted (i.e. file naming conventions),
see :ref:`inputs`.

.. _command-line-args:

Command-Line Arguments
----------------------
.. argparse::
    :ref: hbcd_motion_postproc.my_parser.build_parser
    :prog: hbcd_motion_postproc

.. toctree::
   :maxdepth: 2
   :caption: Contents:

