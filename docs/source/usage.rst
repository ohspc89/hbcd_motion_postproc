.. _usage:

Usage
=====

There are primary inputs to the hbcd_motion_postproc tool.
In each case, the input is provided as a "study-wide" folder, such
that the tool can be run on multiple subjects at once. These three
directories include the BIDS directory, the relaxometry maps directory,
and the segmentation directory.

At the time this application is run, there should be subject (and session,
if sesired) specific folders for each subject you want to process. Processing
will iterate through each subject in the BIDS directory, find associated
sessions with the relevant data, and create the necessary folders and files
in the output directory. Processing is totally independent across subjects
and sessions, so that the results will be the same if the subjects are
processed in parallel or through a single call of this applcation.

The application assumes data prepared following
`motion-BIDS <https://doi.org/10.1038/s41597-024-03559-8>`_.
For more details on the extension, see the linked documentation.

As described in the installation section, this tool is meant to be
interacted with in containerized form. The example below shows the
general layout for how you may want to interact with the container
to conduct processing if you have the container downloaded as a
docker image: ::


        parent_dir=/parent/path/to/bids_dir (ex. /Users/joh/Downloads/hbcd)
        bids_dir=bids_dir_folder_name       (ex. motion_data)
        output_dir=output_dir_folder_name   (ex. motion_output)
        analysis_level=participant

        docker run -v $parent_dir:/HBCD \
            inclab/hbcd_motion_postproc \
            /HBCD/$bids_dir \
            /HBCD/$output_dir \
            $analysis_level


To see more specific information about how this tool expects
the inputs to be formatted (i.e. file naming conventions),
see the inputs formatting page.

.. _command-line-args:

Command-Line Arguments
----------------------
.. argparse::
    :ref: hbcd_motion_postproc.my_parser.build_parser
    :prog: hbcd_motion_postproc
    :nodefault:
    :nodefaultconst:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

