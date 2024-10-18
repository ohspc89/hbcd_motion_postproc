Expected Formatting of Inputs
=============================

BIDS directory
--------------

The BIDS directory should have one folder for each subject
whose session data will be processed.

Each subject's folder should contain raw data files, along
with metadata files. The expected names of the files (with \"\*\"
denoting wildcard) are as follows: ::

    bids/
    |-- participants.tsv
    |-- participants.json
    |-- sub-<label>/
    |   |-- sub-<label>_sessions.tsv
    |   |-- sub-<label>_sessions.json
    |   |-- ses-<label>/
    |   |   |-- sub-<label>_ses-<label>_scans.tsv
    |   |   |-- sub-<label>_ses-<label>_scans.json
    |   |   |-- motion/
    |   |   |   |-- sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_motion.tsv
    |   |   |   |-- sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_motion.json
    |   |   |   |-- sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_channels.tsv
    |   |   |   |-- sub-<label>_ses-<label>_task-<label>_tracksys-imu_acq-<label>_channels.json

Possible labels for the 'task' are 'LeftLegMovement or 'RightLegMovement'.
Possible labels for the 'acq' are 'calibration' or 'primary'.
Therefore, for each combination (ex. LeftLegMovement & calibration) there
will be 4 associated files. In total, 16 files are expected.

'\*\_motion.tsv' is a recording of either calibration dataset or 72 hours of leg movement.
This file will have seven columns, and the details about each column can be found in '\*\_channels.tsv'.

'\*\_motion.json' is the metadata of a recording. Items listed are:

* sampling frequency
* effective sampling frequency
* task name ('primary' or 'calibration')
* task description
* tracking system name
* recording duration
* accelerometer channel count
* gyroscope channel count
* latency channel count
* manufacturer
* sensor name
* sensor serial number

'\*\_channels.tsv' provides details about each column of '\*\_motion.tsv'. Items listed are:

* Measurement axis (X, Y, or Z)
* Sensor type ('accelerometer' or 'gyroscope')
* Sensor position (ankle)
* Measurement unit (m/s^2, rad/s)
* Latency (seconds)
* Reference frame

'\*\_channels.json' describes the reference frame in which the channels of the 
Inertial Measurement Unit (IMU) sensor used to prepare sensor movement dataset are represented

.. toctree::
   :maxdepth: 2
   :caption: Contents:
