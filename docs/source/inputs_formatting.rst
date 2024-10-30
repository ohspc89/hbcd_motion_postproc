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

*task* and *acq* have predetermined label choices.

+-------------------------------------------------------------------------------------------+
|                             | acq label                                                   |
|                             +------------------------------+------------------------------+
|                             | Calibration file             | 72-hour file                 |
+------------+----------------+------------------------------+------------------------------+
| task label | Left leg data  | task- **LeftLegMovement** &  | task- **LeftLegMovement** &  |
|            |                | acq- *Calibration*           | acq- *primary*               |
|            +----------------+------------------------------+------------------------------+
|            | Right leg data | task- **RightLegMovement** & | task- **RightLegMovement** & |
|            |                | acq- *Calibration*           | acq- *primary*               |
+------------+----------------+------------------------------+------------------------------+

For each combination (ex. task-LeftLegMovement & acq-Calibration) there will be 4 associated files. 
In total, **16 files** (4 combinations * 4 files) are expected.

Files: raw time-series data (\*\_motion.tsv)
--------------------------------------------

A *\*\_motion.tsv* is a recording of either calibration dataset or 72 hours of leg movement.
There should be four \*\_motion.tsv files::

    # Calibration files
    a] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibration_motion.tsv
    b] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibration_motion.tsv

    # Raw data, 72-hour files
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

t\ :sub:`i`\  is the elapsed time from the start of a recording, where i is the index of a data point.
a\ :sub:`x`\ (t\ :sub:`i`\ ), a\ :sub:`y`\ (t\ :sub:`i`\ ),
a\ :sub:`z`\ (t\ :sub:`i`\ ) are the accelerometer readings at time t\ :sub:`i`\ , 
along the three measurement axes, while ω\ :sub:`x`\ (t\ :sub:`i`\ ), ω\ :sub:`y`\ (t\ :sub:`i`\ ),
ω\ :sub:`z`\ (t\ :sub:`i`\ ) are the gyroscope readings at time t\ :sub:`i`\  
along its three measurement axes. 
Further information about each column can be found in *\*\_channels.tsv*. 

.. note::

   Users interested in conducting their own analysesand not using the processing container 
   first need to calibrate c] and d] using a] and b], respectively. They can then use
   *calibrated* c] and d] to proceed with their custom analyses.

Files: metadata to a specific tracking system (\*\_motion.json)
---------------------------------------------------------------

A *\*\_motion.json* contains metadata to the sensor used for preparing either a calibration file
or a 72-hour file. There should be four \*\_motion.json files::

    # Calibration files
    e] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibration_motion.json
    f] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibration_motion.json

    # Raw data, 72-hour files
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

Files: metadata to the recorded channels (\*\_channels.tsv)
-----------------------------------------------------------

A *\*\_channels.tsv* provides details about each column of *\*\_motion.tsv*. 
There should be four \*\_channels.tsv files::

    # Calibration files
    i] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibratioin_channels.tsv
    j] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibratioin_channels.tsv

    # Raw data, 72-hour files
    k] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-primary_channels.tsv
    l] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-primary_channels.tsv

Each \*\_channels.tsv file will have seven rows and seven columns. For example, i] for one subject is:

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

Columns
^^^^^^^

* name: the description of each column
* component: the measurement axis (x, y, or z)
* type: the type of sensor (LATENCY, ACCEL, or GYRO)
* tracked_point: the location of the sensor (LeftAnkle or RightAnkle)
* units: measurement unit (seconds, m/s^2 or rad/s)
* sampling_frequency: effective sampling frequency in Hz
* reference_frame: local (sensor-oriented)

Rows
^^^^
* imu_latency: latency information of the sensor used
* LeftAnkle (or RightAnkle) ACCEL_x: accelerometer's x-axis
* LeftAnkle (or RightAnkle) ACCEL_y: accelerometer's y-axis
* LeftAnkle (or RightAnkle) ACCEL_z: accelerometer's z-axis
* LeftAnkle (or RightAnkle) GYRO_x: gyroscope's x-axis
* LeftAnkle (or RightAnkle) GYRO_y: gyroscope's y-axis
* LeftAnkle (or RightAnkle) GYRO_z: gyroscope's z-axis

Files: complementing \*\_channels.tsv
-------------------------------------

A *\*\_channels.json* describes the spatial properties of the reference frame used to
prepare sensor movement dataset are represented.
Positive X, Y, and Z sensor axes correspond to anterior, right, superior, respectively.
There should be four \*\_channels.json files::

    # Calibration files
    m] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibratioin_channels.json
    n] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibratioin_channels.json

    # Raw data, 72-hour files
    o] sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-primary_channels.json
    p] sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-primary_channels.json


.. toctree::
   :maxdepth: 2
   :caption: Contents:
