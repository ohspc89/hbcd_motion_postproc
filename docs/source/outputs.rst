Outputs
=======


The application outputs will generally mirror the structure
of the inputs. The overall output folder structure can be seen
below: ::

    <output_dir>/sub-<label>/ses-<label>/motion/

Within this folder, the following can be found: ::

    (a) sub-<label>_ses-<label>_leg-left_desc-calibrated_recording-20_motion.tsv
    (b) sub-<label>_ses-<label>_leg-right_desc-calibrated_recording-20_motion.tsv
    (c) sub-<label>_ses-<label>_leg-left_desc-calibrated_recording-25_motion.tsv
    (d) sub-<label>_ses-<label>_leg-right_desc-calibrated_recording-25_motion.tsv
    (e) /Kinematics/sub-<label>_ses-<label>_desc-kinematics_recording-20_motion.json
    (f) /Kinematics/sub-<label>_ses-<label>_desc-kinematics_recording-25_motion.json
    (g) /PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_LOG.txt
    (h) /PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_BOUTS.tsv
    (i) /PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_RAW.tsv
    (j) /PA/sub-<label>_ses-<label>_leg-<label>_desc-<label>PA_SUMMARY.json
    (k) PARAMETERS.json

(a, b) are 72 hour left and right leg movement data calibrated using
*/bids_dir/sub-<label>/ses-<label>/motion/sub-<label>_ses-<label>_task-LeftLegMovement_tracksys-imu_acq-calibration_motion.tsv*
and
*/bids_dir/sub-<label>/ses-<label>/motion/sub-<label>_ses-<label>_task-RightLegMovement_tracksys-imu_acq-calibration_motion.tsv*
and resampled at 20 Hz.

(c, d) are similar data without resampling.

(e, f) contain summary kinematic measures based on the 72 hour leg movement
data calibrated. (e) is based on the resampled data , or (a) & (b),
and (f) is based on the non-resampled data, or (c) & (d). Measures include
*threshold values*, *movement rates*, *total movement counts*, *sleep times*,
*average acceleration medians*, *peak acceleration medians*,
*movement duration medians*, and *entropy* values of the left and the right leg
movement datasets.

(g) lists the parameters provided to process data and generate {*}PA_RAW.json,
{*}PA_SUMMARY.json, and {*}PA_BOUTS.tsv ("*" denotes wildcard). In addition,
the content of {*}PA_SUMMARY.json is available in this file.

(h) lists bouts of activity as they occur over time. There are 4 columns of data:
[start time of a bout, end time of a bout, duration of a bout, and classification
of a bout]. The unit for time is seconds. The first line contains the headings,
and the rest contain the data. Classification of bouts is [0: sedentary, 3: light activity,
6: moderate-to-vigorous (MV) activity, 999: undefined (could not be computed)].

(i) lists instantaneous levels of avtivity as they occur over time.
There are 2 columns of data, separated by commas: Unix epoch time (in seconds)
at each instance, and classification at each instance. Classification of instance is
[0: sedentary, 3: light activity, 6: moderate-to-vigorous (MV) activity, 999: undefined
(could not be computed)].

(j) provides the overall summary of physical activity in terms of 3 different measures:
counts (instances) recorded, in terms of percentage time spent, and in terms of
actual time spent in minutes. For each measure, values will be listed for the total,
sedentary, light, and moderate-to-vigorous (MV) activity. The fifth label, "undefined",
can be ignored.

(k) lists the parameters provided when using the docker container. Items include
[bids_dir, output_dir, analysis_level, participant_label, session_id, interval,
pa_measure, pa_side, entropy_type, entropy_measure]. Please refer to :ref:`command-line-args`
in the usage documentation for more details.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
