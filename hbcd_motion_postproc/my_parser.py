#!/usr/bin/python3
import argparse


def build_parser():
    # Configure the commands that can be fed to the command line
    help_msg = """Data files (.tsv) in `bids_dir` will be analyzed and \
    the outputs are stored in `output_dir`. `participant_label` and `session_id` \
    can be provided to process specific participant / session data. \
    For other arguments, unless a default value is set, all possible choices \
    will be processed.
    """
    parser = argparse.ArgumentParser(description=help_msg,
                                     epilog="Prepared by Jinseok Oh, Ph.D.")
    parser.add_argument("bids_dir", help="The path to the BIDS directory for your study (this is the same for all subjects)", type=str)
    parser.add_argument("output_dir", help="The path to the folder where outputs will be stored (this is the same for all subjects)", type=str)
    parser.add_argument("analysis_level", help="Should always be **participant**", type=str)
    # (7/18/24) dropping `study_tz`
    # parser.add_argument("study_tz", help="Timezone of the site where sensors were configured (ex. US/Pacific)", type=str)

    parser.add_argument('--participant_label', '--participant-label',
                        help="(optional) The label of the subject to be processed (ex. sub-XXXXX)", type=str)
    parser.add_argument('--session_id', '--session-id',
                        help="(optional) The label of the session to be processed (ex. ses-V02)", type=str)
    parser.add_argument('--interval',
                        help="(optional) The label to correct or not the uneven sampling interval",
                        type=str, choices=['raw', 'corrected'], default='raw')
    parser.add_argument('--pa_measure', '--pa-measure',
                        help="(optional) The computedQttyOption value",
                        type=str, choices=['acceleration', 'jerk'])
    parser.add_argument('--pa_side', '--pa-side',
                        help="(optional) which leg to calculate the physical activity level",
                        type=str, choices=['Left', 'L', 'Right', 'R'])
    parser.add_argument('--entropy_type', '--entropy-type',
                        help="(optional) Entropy type",
                        type=str, choices=['SampEn', 'FuzzEn'])
    parser.add_argument('--entropy_measure', '--entropy-measure',
                        help="(optional) Measure to calculate an entropy",
                        type=str, choices=['avgacc', 'pkacc'])
    parser.add_argument('--stop_on_error', '--stop-on-error ',
                        help="(optional) If activated, the code will try to exit if an error is encountered.", action='store_true')

    return parser
