.. image:: https://img.shields.io/badge/docker-inclab/hbcd_motion_postproc-brightgreen.svg?logo=docker$style=flat
   :target: https://hub.docker.com/r/inclab/hbcd_motion_postproc/tags/
.. image:: https://readthedocs.org/projects/hbcd_motion_postproc/badge/?version=latest
   :target: https://hbcd-motion-postproc.readthedocs.io/en/latest/
.. image:: https://zenodo.org/badge/867238460.svg
   :target: https://doi.org/10.5281/zenodo.14200420

Introduction
============

In the HBCD study, `Axivity Ax6 <https://axivity.com/product/ax6>`_ sensors were used to record
infant leg movements across 72 continuous hours. Research
assistants of the study placed one sensor on the distal 
right ankle and another on the distal left ankle, using 
legwarmers with a pocket to hold the sensor.

Sensors were set to start recording at 10 a.m. eastern / 9 a.m.
central / 8 a.m. mountain / 7 a.m. pacific. Caregivers were
instructred to go about their typical activities in the natural
environment but to remove the sensors if the baby went into water 
(e.g., bathtub or pool) and replace them afterward.

Leg movement data recording occurred at **V02 (0-1 months of age)** and
at **V03 (3-8 months of age)**.

| The sensors were set to record accelerometer (acceleration,
  range of +/- 16g) and gyroscope (angular velocity, rate of rotation,
  +/- 2000 dps) data continuously at 25 samples per second.
| From this, we can estimate how frequently and how vigorously an infant
  is moving his or her legs, including an estimate of sedentary physical
  activity, light physical activity, moderate-to-vigorous activity,
  or asleep.

Before the 72 hours of data were collected, a calibration file was
collected for each sensor. Instructions for collection of the calibration
data were: "There are 6 flat surfaces of the sensor and we want to record
data with the sensor sitting still on each of its flat surfaces.
To do this: place the sensor on a level, flat surface (e.g., the surface
of a desk or table). Wait 10 seconds. Rotate it so that it is resting
on its next flat surface. Wait 10 seconds. You should put the sensor in 6
different positions and collect 10 seconds of data in each position,
so just over a minute of data in total (including the time to rotate it).
It does not matter what order you do this in."

Data files included in the data release are raw sensor data in `BIDS <https://bids.neuroimaging.io>`_
format for the calibration and 72-hour files for the right and the left leg
(:ref:`inputs`), as well as files containing processed data :ref:`outputs`. 

Key references
--------------

**Describing the protocol decision-making process**:
Pini, N., Fifer, W. P., Oh, J., Nebeker, C., Croff, J. M., Smith, B. A., &
Novel Technology/Wearable Sensors Working Group (2024). Remote data collection
of infant activity and sleep patterns via wearable sensors in the HEALthy
Brain and Child Development Study (HBCD).
*Developmental Cognitive Neuroscience, 69,* 101446.
https://doi.org/10.1016/j.dcn.2024.101446

**BIDS format for raw data files**:
Jeung, S., Cockx, H., Appelhoff, S., Berg, T., Gramann, K., Grothkopp, S.,
Warmerdam, E., Hansen, C., Oostenveld, R., BIDS Maintainers, & Welzel, J.
(2024). Motion-BIDS: an extension to the brain imaging data structure
to organize motion data for reproducible research. *Scientific Data, 11* (1),
716. https://doi.org/10.1038/s41597-024-03559-8

**Calibration process to prepare data for calculation of infant leg movement
characteristics**:
Oh, J., Loeb, G. E., & Smith, B. A. (2024). The Utility of Calibrating
Wearable Sensors before Quantifying Infant Leg Movements. *Sensors, 
24* (17), 5736. https://doi.org/10.3390/s24175736

**Algorithms to identify infant leg movement characteristics**:
Smith, B. A., Trujillo-Priego, I. A., Lane, C. J., Finley, J. M., 
& Horak, F. B. (2015). Daily Quantity of infant leg movement: Wearable sensor algorithm
and relationship to walking onset. *Sensors, 15* (8), 19006-19020.
https://doi.org/10.3390/s150819006

Trujillo-Priego, I. A., & Smith, B. A. (2017). Kinematic characteristics
of infant leg movements produced across a full day. *Journal of Rehabilitation
and Assistive Technologies Engineering, 4,* 2055668317717461.
https://doi.org/10.1177/2055668317717461

Trujillo-Priego, I. A., Zhou, J., Werner, I. F., Deng, W., & Smith, B. A. (2020).
Infant Leg Activity Intensity Before and After Naps. *Journal for the Measurement
of Physical Behaviour, 3* (2), 157-163. https://doi.org/10.1123/jmpb.2019-0011

Oh, J., Ordoñez, E. L. T., Velasquez, E., Mejía, M., Del Pilar Grazioso, M.,
Rohloff, P., & Smith, B. A. (2024). Associating neuromotor outcomes at 12 months
with wearable sensor measures collected during early infancy in rural Guatemala.
*Gait & Posture, 114,* 477-489. https://doi.org/10.1016/j.gaitpost.2024.08.005

**Algorithm to estimate intensity of infant physical activity**:
Ghazi, M. A., Zhou, J., Havens, K. L., & Smith, B. A. (2024). Accelerometer
Thresholds for Estimating Physical Activity Intensity Levels in Infants: A
Preliminary Study. *Sensors, 24* (14), 4436.
https://doi.org/10.3390/s24144436


Quality Control (QC) Processes
------------------------------

* **QC Procedures**: Some raw data files were checked for quality. Only a small 
  percentage of data files were randomly checked each week as the process was 
  manual and visual. When checked, calibration files were
  checked for presence of adequate data for each of 6 axes and 72-hour files were
  checked for the presence of data, labeling of right and left leg, and sampling
  rate used.

* **Common Issues Identified**: Common issues identified during the QC proceeses
  included inadequate data for each of the six axes in calibration files (human error),
  missing data for calibration files (due to human error or technical difficulties),
  missing data for 72 hours (due to human error, technical difficulties, or parent/
  legal guardian declining to participate in this aspect of the study), sensors
  being removed from prolonged periods during the 72 hours, or the use of incorrect 
  sampling rate during the 72 hour collection. If possible, errors were corrected (but
  this was not often possible). All issues occurred rarely overall and the majority
  of the data were judged to be present and correctly collected. If data from a 
  particular visit fell under any of the aforementioned scenarios, the preprocessing 
  pipeline would fail to process the data and generate an error log (LOG.txt).


Potential Issues Flagged by Subject Matter Experts
--------------------------------------------------

No issues were found.

| Users are reminded that accelerometer sensor timestamps drift over time, so even 
  though the right and the left leg sensors started recording at the same time and
  recorded for the same duration of the time at the same sampling rate,
  one cannot assume that the time specified matches exactly between the two sensors.
| By our estimates, Axivity Ax6 sensors recording at 25 samples/sec diverge from one
  another by a couple of seconds by the end of 72 hours, and the magnitude of this
  error increases over time. Further, offsets were diffrent between different sensors,
  so a calibration procedure was used to adjust for this (See Oh, J., Loeb, G. E., & Smith, B. A.
  (2024). The Utility of Calibrating Wearable Sensors before Quantifying Infant Leg Movements.
  *Sensors, 24* (17), 5736.).
