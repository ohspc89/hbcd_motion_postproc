Expected Formatting of Inputs
=============================

BIDS directory
--------------

The BIDS directory should have one folder for each subject
whose session data will be processed.

Each subject's folder should contain raw data files, along
with metadata files. The expected names of the files (with \"\*\"
denoting wildcard) are as follows: ::

    /bids_dir/sub-<label>/ses-<label>/motion/sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_channels.json
    /bids_dir/sub-<label>/ses-<label>/motion/sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_channels.tsv
    /bids_dir/sub-<label>/ses-<label>/motion/sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_motion.json
    /bids_dir/sub-<label>/ses-<label>/motion/sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_motion.tsv

Possible labels for the 'task' are 'LeftLegMovement or 'RightLegMovement'.
Possible labels for the 'acq' are 'calibration' or 'primary'.
Therefore, for each combination (ex. LeftLegMovement & calibration) there
will be 4 associated files. In total, 16 files are expected.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
