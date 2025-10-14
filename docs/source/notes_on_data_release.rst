.. _notes-data-release:


Notes on released data
======================

Here we summarize the *issues* (human errors and technical glitches) identified in the released movement sensor data for each release. The purpose of sharing these notes is to inform researchers who plan to conduct their own analyses using the released data.
Release notes are available at `<https://docs.hbcdstudy.org>`_. As of Oct 10, 2025, V02 data are available in "derivatives:hbcd_motion", and the data review is done on V02 data.

Issue Types
-----------

A. Unexpected Movement Sensor Recording Onsets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
According to the Standard Operating Procedure (SOP) for movement sensor configuration, sensors are expected to start recording at 7 PT / 8 MT / 9 CT / 10 ET. However, several sensors were found to have started recording at times not designated by the SOP.

B. Incorrect Sampling Rate
^^^^^^^^^^^^^^^^^^^^^^^^^^
Sensors are supposed to be recording at 25Hz. There were recordings prepared at frequencies other than this value.

C. Sensor Recording Onsets Differed by More Than a Minute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Although minor differences in sensor start times are expected (e.g., less than one minute), several cases showed discrepancies exceeding one minute.

D. Recordings Shorter or Longer Than 72 Hours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some recordings were substantially shorter or longer than the expected 72-hour duration, with differences greater than two hours.

E. Static Calibration Datasets Not Prepared
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SOP requires a calibration dataset to be prepared by recording each of the six axis/orientation combinations for 10 seconds on a flat surface. Some calibration datasets were missing or only partially prepared.

F. Sensor Saturation
^^^^^^^^^^^^^^^^^^^^
In some instances, sensors experienced saturation (i.e., measuring signals that exceeded their dynamic range: +/- 16g).

G. Sensor Measurement Variability Beyond Static Calibration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Although certain sensors were calibrated using the required datasets, residual measurement errors were observed. These errors may have been due to misalignment of the measurement axes or other factors not addressed by static calibration.

Data Releases
-------------

.. collapse:: **Release 1.0** (data released August, 2025)

    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | Subject ID        | Session ID | Issue(s)   | Note                                                                             |
    +===================+============+============+==================================================================================+
    | sub-1288135064    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-1380991861    | ses-V02    | A, C       | Sensors started at 10:57 and 10:58                                               |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-1789538106    | ses-V02    | B          | Sensors recorded at 100Hz                                                        |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-1871369569    | ses-V02    | G          |                                                                                  |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-2494615241    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-2648528961    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-2686683014    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-2900929757    | ses-V02    | A          | Sensors started at 17:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-2974711882    | ses-V02    | A, C, D    | Sensors started at 12:53 and 12:56; sensors recorded for 243.41 and 215.57 hours |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-3258020230    | ses-V02    | G          |                                                                                  |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4012525125    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4012579197    | ses-V02    | A          | Sensors started at 12:37                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4157643370    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4281785287    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4505920019    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4539220581    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4773377295    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4802490613    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-4901969500    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-5616768535    | ses-V02    | E          |                                                                                  |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-5787518911    | ses-V02    | A, C, D    | Sensors started at 09:16 and 09:08; sensors recorded for 237.69 and 204.75 hours |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-6482681015    | ses-V02    | A          | Sensors started at 16:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-6643221141    | ses-V02    | G          |                                                                                  |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-7675591543    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-7714541303    | ses-V02    | A          | Sensors started at 10:42                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-7847021066    | ses-V02    | A, C, D, E | Sensors started at 17:38 and 17:44; sensors recorded for 197.27 and 201.15 hours |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-8041662653    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-8082300310    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-8154737565    | ses-V02    | A, G       | Sensors started at 10:52                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-8300473690    | ses-V02    | E          |                                                                                  |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-9175945343    | ses-V02    | F          |                                                                                  |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-9218723155    | ses-V02    | A, C, D    | Sensors started at 14:00 and 13:49; sensors recorded for 239.71 and 228.84 hours |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+
    | sub-9418870066    | ses-V02    | A          | Sensors started at 20:00                                                         |
    +-------------------+------------+------------+----------------------------------------------------------------------------------+


.. toctree::
   :maxdepth: 2
   :caption: Contents:
