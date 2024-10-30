.. _inputs:

Data inputs to the container: raw BIDS files
============================================

This page provides details on the raw sensor data in BIDS format
for the calibration and 72-hour files for the right leg and the left leg,
which are provided as data inputs to the processing container.

BIDS directory
--------------

The BIDS directory should have one folder for each subject
whose session data will be processed.

Each subject's folder should contain raw data files, along
with metadata files. The expected names of the files (with \*\
denoting wildcard) are as follows: ::

    bids_dir/
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

*sub-<label>_ses-<label>_scans.tsv* will have the age of the subject at the data collection.
The age is in years (represented up to 3 decimal places).

Possible labels for the `task` are **LeftLegMovement** or **RightLegMovement**.
Possible labels for the `acq` are **calibration** or **primary**.
Therefore, for each combination (ex. LeftLegMovement & calibration) there
will be 4 associated files. In total, **16 files** are expected.

*\*\_motion.tsv* is a recording of either calibration dataset or 72 hours of leg movement.
There should be four \*\_motion.tsv files::

    a] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibration_motion.tsv
    b] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibration_motion.tsv
    c] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-primary_motion.tsv
    d] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-primary_motion.tsv

Each \*\_motion.tsv file will have seven columns:

+--------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+
| t\ :sub:`0`\ | a\ :sub:`x`\ (t\ :sub:`0`\ ) | a\ :sub:`y`\ (t\ :sub:`0`\ ) | a\ :sub:`z`\ (t\ :sub:`0`\ ) | ω\ :sub:`x`\ (t\ :sub:`0`\ ) | ω\ :sub:`y`\ (t\ :sub:`0`\ ) | ω\ :sub:`z`\ (t\ :sub:`0`\ ) |
+--------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+
| t\ :sub:`1`\ | a\ :sub:`x`\ (t\ :sub:`1`\ ) | a\ :sub:`y`\ (t\ :sub:`1`\ ) | a\ :sub:`z`\ (t\ :sub:`1`\ ) | ω\ :sub:`x`\ (t\ :sub:`1`\ ) | ω\ :sub:`y`\ (t\ :sub:`1`\ ) | ω\ :sub:`z`\ (t\ :sub:`1`\ ) |
+--------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+
| ...          | ...                          | ...                          | ...                          | ...                          | ...                          | ...                          |
+--------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+
| t\ :sub:`N`\ | a\ :sub:`x`\ (t\ :sub:`N`\ ) | a\ :sub:`y`\ (t\ :sub:`N`\ ) | a\ :sub:`z`\ (t\ :sub:`N`\ ) | ω\ :sub:`x`\ (t\ :sub:`N`\ ) | ω\ :sub:`y`\ (t\ :sub:`N`\ ) | ω\ :sub:`z`\ (t\ :sub:`N`\ ) |
+--------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+------------------------------+

t\ :sub:`i`\  is the elapsed time from the start of a recording. i is the index of a data point.
a\ :sub:`x`\ (t\ :sub:`i`\ ), a\ :sub:`y`\ (t\ :sub:`i`\ ),
a\ :sub:`z`\ (t\ :sub:`i`\ ) are the accelerometer readings at time t\ :sub:`i`\ , 
along the three measurement axes. ω\ :sub:`x`\ (t\ :sub:`i`\ ), ω\ :sub:`y`\ (t\ :sub:`i`\ ),
ω\ :sub:`z`\ (t\ :sub:`i`\ ) are the gyroscope readings at time t\ :sub:`i`\ , 
along the three measurement axes. 
Further information about each column can be found in *\*\_channels.tsv*. 
a] and b] are ~1 minute long (calibration files) and 
c] and d] are 72 hours long (raw movement recording files)

.. note::

   Users interested in conducting their own analysesand not using the processing container 
   first need to calibrate c] and d] using a] and b], respectively. They can then use
   *calibrated* c] and d] to proceed with their custom analyses.


*\*\_motion.json* is the metadata of a recording. There should be four \*\_motion.json files::

    e] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibration_motion.json
    f] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibration_motion.json
    g] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-primary_motion.json
    h] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-primary_motion.json

Items listed in each file are:

* sampling frequency
* effective sampling frequency
* task name (primary or calibration)
* task description
* tracking system name
* recording duration
* accelerometer channel count
* gyroscope channel count
* latency channel count
* manufacturer
* sensor name
* sensor serial number

*\*\_channels.tsv* provides details about each column of *\*\_motion.tsv*. 
There should be four \*\_channels.tsv files::

    i] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibratioin_channels.tsv
    j] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibratioin_channels.tsv
    k] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-primary_channels.tsv
    l] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-primary_channels.tsv

Each \*\_channels.tsv file will have seven columns. For example, i] for one subject is:

+-------------------+-----------+---------+---------------+---------+--------------------+-----------------+
| name              | component | type    | tracked_point | units   | sampling_frequency | reference_frame |
+===================+===========+=========+===============+=========+====================+=================+
| imu_latency       | n/a       | LATENCY | n/a           | seconds | 25.70383751213197  | local           |
+-------------------+-----------+---------+---------------+---------+--------------------+-----------------+
| LeftAnkle_ACCEL_x | x         | ACCEL   | LeftAnkle     | m/s^2   | 25.70383751213197  | local           |
+-------------------+-----------+---------+---------------+---------+--------------------+-----------------+
| ...               | ...       | ...     | ...           | ...     | ...                | ...             |
+-------------------+-----------+---------+---------------+---------+--------------------+-----------------+
| LeftAnkle_GYRO_x  | z         | GYRO    | LeftAnkle     | rad/s   | 25.70383751213197  | local           |
+-------------------+-----------+---------+---------------+---------+--------------------+-----------------+


* name: the description of each column
* component: the measurement axis (x, y, or z)
* type: the type of sensor (LATENCY, ACCEL, or GYRO)
* tracked_point: the location of the sensor (LeftAnkle or RightAnkle)
* units: measurement unit (seconds, m/s^2 or rad/s)
* sampling_frequency: effective sampling frequency in Hz
* reference_frame: local (sensor-oriented)

*\*\_channels.json* describes the reference frame in which the channels of the 
Inertial Measurement Unit (IMU) sensor used to prepare sensor movement dataset are represented.
Positive X, Y, and Z sensor axes correspond to anterior, right, superior, respectively.
There should be four \*\_channels.json files::

    m] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibratioin_channels.json
    n] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibratioin_channels.json
    o] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-primary_channels.json
    p] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-primary_channels.json


.. toctree::
   :maxdepth: 2
   :caption: Contents:
