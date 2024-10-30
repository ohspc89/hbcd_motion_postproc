.. _outputs:


Processed data outputs
======================

The application outputs will generally mirror the structure
of the inputs. The overall output folder structure can be seen
below: ::

    <output_dir>/sub-<label>/ses-<label>/motion/

Within this folder, the following can be found: ::

    a] PARAMETERS.json
    b] sub-<label>_ses-<label>_leg-left_desc-calibrated_recording-20_motion.tsv
    c] sub-<label>_ses-<label>_leg-right_desc-calibrated_recording-20_motion.tsv
    d] Kinematics/sub-<label>_ses-<label>_desc-kinematics_recording-20_motion.json
    e] Kinematics/sub-<label>_ses-<label>_desc-kinematics_recording-25_motion.json
    f] PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_LOG.txt
    g] PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_BOUTS.tsv
    h] PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_RAW.tsv
    i] PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_SUMMARY.json
    j] LOG.txt

Intermediate data files: a] ~ c]
--------------------------------
a] lists the parameters provided when using the docker container. 

* bids_dir
* output_dir
* analysis_level
* participant_label
* session_id
* interval
* pa_measure
* pa_side
* entropy_type
* entropy_measure

Please refer to :ref:`command-line-args` in the usage documentation for see possible
choices for each parameter.

b] and c] are 72 hour left and right leg movement data. They are first calibrated using
(found in */bids_dir/sub-<label>/ses-<label>/motion/*):

* *sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibration_motion.tsv*
* *sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibration_motion.tsv*

and then resampled at 20 Hz. These files are required for the estimation of physical activity levels (f] - i]).

Processed data outputs: d] ~ i]
-------------------------------
d] and e] contain summary kinematic measures based on the 72 hour leg movement
data. d] is based on the resampled data, a] and b],
and e] is based on the non-resampled data (No intermediate data files exist). 
Please refer to the table below to understand what each measure is about: 

+--------------------------------+-----------------------------------------------------------------------------+
| measure                        | description                                                                 |
+================================+=============================================================================+
| Participant_id                 | <label> of sub-<label>                                                      |
+--------------------------------+-----------------------------------------------------------------------------+
| Session_id                     | <label> of ses-<label>                                                      |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_positive_threshold        | a positive acceleration magnitude threshold to identify left leg movements  |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_positive_threshold       | a positive acceleration magnitude threshold to identify right leg movements |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_negative_threshold        | a negative acceleration magnitude threshold to identify left leg movements  |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_positive_threshold        | a negative cceleration magnitude threshold to identify right leg movements  |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_total_count               | the total left leg movement count                                           |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_total_count              | the total right leg movement count                                          |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_movement_rate             | left leg movement rate per hour awake                                       |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_movement_rate            | right leg movement rate per hour awake                                      |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_sleep_time                | time estimated to be asleep from the left leg movement data                 |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_sleep_time               | time estimated to be asleep from the right leg movement data                |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_average_acc_median        | median of the average accelerations of left leg movements                   |
+--------------------------------+-----------------------------------------------------------------------------+
| Left average_acc_iqr           | inter-quartile-range of the average accelerations of left leg movements     |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_peak_acc_median           | median of the peak accelerations of left leg movements                      |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_peak_acc_iqr              | inter-quartile-range of the peak accelerations of left leg movements        |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_movement_duration_median  | median of the durations of left leg movements                               |
+--------------------------------+-----------------------------------------------------------------------------+
| Left_movement_duration_iqr     | inter-quartile-range of the durations of the left leg movements             |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_average_acc_median       | median of the average accelerations of left leg movements                   |
+--------------------------------+-----------------------------------------------------------------------------+
| Right average_acc_iqr          | inter-quartile-range of the average accelerations of left leg movements     |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_peak_acc_median          | median of the peak accelerations of left leg movements                      |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_peak_acc_iqr             | inter-quartile-range of the peak accelerations of left leg movements        |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_movement_duration_median | median of the durations of left leg movements                               |
+--------------------------------+-----------------------------------------------------------------------------+
| Right_movement_duration_iqr    | inter-quartile-range of the durations of the left leg movements             |
+--------------------------------+-----------------------------------------------------------------------------+
| entropies                      | sample entropy (SampEn) and/or fuzzy entropy (FuzzEn) of a time series      |
|                                | (average_acc or peak_acc)                                                   |
+--------------------------------+-----------------------------------------------------------------------------+


f] lists the parameters provided to process data and generate \*\PA_RAW.json,
\*\PA_SUMMARY.json, and \*\PA_BOUTS.tsv (\*\ denotes wildcard). In addition,
the content of \*\PA_SUMMARY.json is available in this file.

g] saves bouts of activity as they occur over time. There are 4 columns of data.

+----------------------+--------------------+--------------------+--------------------------+
| start time of a bout | end time of a bout | duration of a bout | classification of a bout |
+======================+====================+====================+==========================+
|           ...        |         ...        |         ...        |            ...           |
+----------------------+--------------------+--------------------+--------------------------+

The unit for time is seconds. The first line contains the headings,
and the rest contain the data. Classification of bouts is:

+-------+--------------------------------------+
| value |             classification           |
+=======+======================================+
|   0   |               sedentary              |
+-------+--------------------------------------+
|   3   |             light activity           |
+-------+--------------------------------------+
|   6   |  moderate-to-vigorous (MV) activity  |
+-------+--------------------------------------+
|  999  |   undefined (could not be computed)  |
+-------+--------------------------------------+

h] lists instantaneous levels of avtivity as they occur over time.
There are 2 columns of data, separated by commas: Unix epoch time (in seconds)
at each instance, and classification at each instance. Classification of instance is
described in g].

i] provides the overall summary of physical activity in terms of 3 different measures:
counts (instances) recorded, in terms of percentage time spent, and in terms of
actual time spent in minutes. For each measure, values will be listed for the total,
sedentary, light, and moderate-to-vigorous (MV) activity. The fifth label, "undefined",
can be ignored.


Error log: j]
-------------
j] will be created only if data are not processed by the pipeline.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
